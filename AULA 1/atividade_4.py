import streamlit as st
import pandas as pd

dados = pd.read_csv('vendas.csv')

st.title('Leitura de dados')

with st.expander('primeira tabela'):
    st.dataframe(dados)

with st.expander('segunda tabela'):
    st.table(dados)