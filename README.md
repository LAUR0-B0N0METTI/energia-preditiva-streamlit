
# 🔋 Previsão de Consumo de Energia Residencial - Alemanha 🇩🇪

Este projeto tem como objetivo realizar a análise e previsão do consumo de energia elétrica residencial na Alemanha utilizando técnicas de aprendizado de máquina, visualizações interativas e um modelo preditivo acessível por meio de uma aplicação web com Streamlit.

## 📌 Objetivo

Desenvolver uma solução analítica capaz de:
- Realizar o pré-processamento e limpeza dos dados.
- Explorar padrões de consumo com visualizações temporais.
- Treinar e avaliar um modelo preditivo de consumo energético.
- Apresentar os resultados de forma intuitiva e visual.

---

## 📈 Dataset

- **Fonte:** Open Power System Data (https://data.open-power-system-data.org)
- **Período:** 2015 a 2019
- **Frequência:** Horária
- **Variável alvo:** Consumo de energia (MW)

---

## ⚙️ Funcionalidades da Aplicação

A aplicação web apresenta as seguintes seções:

### 🧹 Pré-processamento
- Exibição de valores ausentes
- Verificação e padronização dos dados temporais

### 📊 Visualizações Interativas
- Consumo médio diário ao longo dos anos
- Padrão de consumo por hora do dia
- Padrão de consumo por dia da semana

### 🤖 Modelo Preditivo
- Previsão do consumo energético por hora
- Visualização comparativa entre consumo real e previsto
- Erro médio absoluto (MAE)

---

## 🧠 Técnicas Utilizadas

- `Python` • `Pandas` • `NumPy` • `Scikit-learn`
- `Streamlit` para a criação da interface web
- Visualizações com `Matplotlib` e `Seaborn`
- Modelo preditivo com regressão (ex: RandomForest, XGBoost, ou outro)

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação:
```bash
streamlit run app.py
```

---

## 🗂 Estrutura do Projeto

```
├── app.py
├── data/
│   └── consumo_energia.csv
├── models/
│   └── modelo_treinado.pkl
├── requirements.txt
└── README.md
```

---

## 📌 Resultados

- O modelo preditivo obteve um **erro médio absoluto de ~2726 MW**, com boa aderência aos dados reais.
- Os padrões temporais identificados auxiliam no entendimento de picos de demanda e otimização energética.

---

## 📌 Próximos Passos

- Adicionar variáveis externas como temperatura ou feriados.
- Testar modelos baseados em redes neurais (LSTM).
- Implementar atualização em tempo real com dados de API.

---

## ✨ Autor

- **Lauro Bonometti**
- https://www.linkedin.com/in/laurobonometti

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```# energia-preditiva-streamlit
Previsão de Consumo de Energia Residencial na Alemanha com Machine Learning.
