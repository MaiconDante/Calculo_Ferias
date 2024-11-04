# Importando Bibliotecas
import streamlit as st
from fpdf import FPDF
import pandas as pd

# Caminho para o logotipo no local
image_path = "/Volumes/Projects/Python/Calculo_Ferias/rh_logo.jpg" 

# Criação do container título e logotipo
frame_title = st.container(border=True)
with frame_title:
    # Criando duas colunas dentro do contêiner para imagem e título
    col1, col2 = st.columns([1, 3]) 

    # Inserindo a imagem na primeira coluna
    col1.image(image_path, width=150)

    # Inserindo o título na segunda coluna
    col2.markdown("## | Cálculo de Férias RH |")  # Título em markdown para ajustar tamanho

# Criação do container empresa e colaborador
frame_company = st.container(border=True)
with frame_company:
    st.markdown("Forneça os dados a seguir :")
    st.text_input(label="Empresa :", max_chars=50, placeholder="Digite aqui !!!")
    st.text_input(label="Colaborador :", max_chars=50, placeholder="Digite aqui !!!")