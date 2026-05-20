import streamlit as st

# Abre o seu arquivo HTML e renderiza em tela cheia
st.components.v1.html(open("feminicidio_dados_pj.html", "r", encoding="utf-8").read(), height=1000, scrolling=True)