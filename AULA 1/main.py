import streamlit as st
import pandas as pd

dados = pd.read_csv('vendas.csv')

st.header('testando streamlit')
st.write ('outro teste')

n1 = st.number_input('digite um nomero:')
n2 = st.number_input('digite outro numero', value = 0.0)

soma_, div_, sub_, mult_ = st.columns(4)

if soma_.button('+'):
    soma = n1 + n2
    st.info(soma)
elif sub_.button('-'):
    sub = n1 - n2
    st.info(sub)
elif mult_.button('X'):
     mult = n1 * n2
     st.info(mult)
elif div_.button(':'):
    div = n1 / n2
    st.info(div)


st.header('ANALISE DE DADOS')

st.table(dados)

st.bar_chart(dados, x = 'ano' , y= 'lucro')
