import streamlit as st

st.title('ficha de cadastro')

nome = st.text_input('digite seu nome')
idade = st.number_input('digite sua idade')
termos = st.checkbox('voce aceita os termos de uso?')

def mostra():
    st.info(f"seu nome é  {nome}  sua idade é  {idade}  voce concordou com os termos  {termos}")


st.button('Enviar', on_click=mostra)


