import streamlit as st

st.title('Escolha seu curso')


option = st.selectbox(
    "Escolha um curso",
    ["Culinaria", "Programaçao", "Eletronica"],
    index=None,
    
    
)

options = st.multiselect(
    "Quais horarios vc tem disponivel?",
    ["Manha", "Tarde", "Noite"],
    
)
