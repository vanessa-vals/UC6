import streamlit as st

st.title("Meu primeiro app!")
nome = st.text_input("Qual é o seu nome?")
if nome:
    st.write(f"Olá, {nome}! 👋")