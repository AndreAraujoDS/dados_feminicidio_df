import streamlit as st

# 1. Configura a página do Streamlit para usar a largura total da tela (Tira o visual espremido)
st.set_page_config(layout="wide", page_title="Relatório Feminicídio DF")

# 2. Remove as margens e paddings padrões do Streamlit para o HTML colar nas bordas corretamente
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        iframe {
            border: none;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Lê o seu arquivo HTML
with open("feminicidio_dados_pj.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# 4. Renderiza o HTML com altura automática adaptável (height=1400 cobre o painel inteiro sem scroll interno)
st.components.v1.html(html_code, height=1400, scrolling=False)