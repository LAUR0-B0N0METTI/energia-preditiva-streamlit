import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import os

# =========================
# 1. Carregamento e Exploração Inicial
# =========================
st.set_page_config(page_title="Previsão de Consumo de Energia", layout="wide")
st.title("🔌 Previsão de Consumo de Energia na Alemanha")

st.markdown("""
Projeto de análise e previsão de consumo energético baseado em dados da plataforma Open Power System Data.
""")

# Carregar dados diretamente do caminho local
caminho_dados = r"C:\\Users\\L\\Desktop\\Consumo_de_Energia\\opsd-time_series-2020-10-06\\time_series_60min_singleindex.csv"

try:
    df = pd.read_csv(caminho_dados, parse_dates=['utc_timestamp'])
    df.set_index('utc_timestamp', inplace=True)

    st.subheader("🔎 Visão Geral dos Dados")
    st.write(df.head())
    st.write(df.info())

    # =========================
    # 2. Pré-processamento
    # =========================
    st.subheader("🧹 Pré-processamento")
    coluna = 'DE_load_actual_entsoe_transparency'
    df = df[[coluna]].copy()
    df.rename(columns={coluna: 'consumo_MW'}, inplace=True)

    st.write("Valores ausentes:", df.isnull().sum().values[0])
    df.dropna(inplace=True)

    # Criar features de tempo
    df['hora'] = df.index.hour
    df['dia_semana'] = df.index.dayofweek
    df['mes'] = df.index.month

    # =========================
    # 3. Visualizações
    # =========================
    st.subheader("📊 Visualizações")

    st.write("Consumo médio diário:")
    st.line_chart(df['consumo_MW'].resample('D').mean(), use_container_width=True)

    st.write("Consumo médio por hora do dia:")
    hora_media = df.groupby('hora')['consumo_MW'].mean()
    st.bar_chart(hora_media)

    st.write("Consumo médio por dia da semana:")
    dia_semana = df.groupby('dia_semana')['consumo_MW'].mean()
    st.bar_chart(dia_semana)

    # =========================
    # 4. Modelagem Preditiva
    # =========================
    st.subheader("🤖 Modelo Preditivo")

    features = ['hora', 'dia_semana', 'mes']
    X = df[features]
    y = df['consumo_MW']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    previsoes = modelo.predict(X_test)

    erro = mean_absolute_error(y_test, previsoes)
    st.write(f"Erro médio absoluto: {erro:.2f} MW")

    # Comparação real vs previsto
    resultado = pd.DataFrame({
        'Real': y_test.values,
        'Previsto': previsoes
    }, index=y_test.index)
    st.line_chart(resultado.head(100))

    # =========================
    # 5. Exportar modelo e estrutura do projeto
    # =========================
    st.subheader("💾 Exportar Modelo")

    exportar = st.checkbox("Salvar modelo como .pkl")
    if exportar:
        if not os.path.exists("model"):
            os.makedirs("model")
        joblib.dump(modelo, "model/energy_model.pkl")
        st.success("Modelo salvo em: model/energy_model.pkl")

except FileNotFoundError:
    st.error("❌ Arquivo não encontrado. Verifique o caminho e tente novamente.")
