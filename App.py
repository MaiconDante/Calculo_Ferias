# Importando Bibliotecas
import streamlit as st
from fpdf import FPDF
import pandas as pd

# Caminho para o logotipo no local e rodapé
image_path = "/Volumes/Projects/Python/Calculo_Ferias/rh_logo.jpg"
image_end = "/Volumes/Projects/Python/Calculo_Ferias/rodape.png" 

# CSS para centralizar o título
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 40px;  
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Criação do container título e logotipo
frame_title = st.container(border=True)
with frame_title:
    # Criando duas colunas dentro do contêiner para imagem e título
    col1, col2 = st.columns([1, 3]) 

    # Inserindo a imagem na primeira coluna
    col1.image(image_path)

    # Inserindo o título na segunda coluna
    col2.markdown('<div class="centered-title">| Cálculo de Férias RH |</div>', unsafe_allow_html=True)  # Título em markdown para ajustar tamanho

# Criação do container empresa e colaborador
frame_company = st.container(border=True)
with frame_company:
    st.markdown("Forneça os dados a seguir :")
    company = st.text_input(label="Empresa :", max_chars=50, placeholder="Digite aqui !!!", key=("Empresa"))
    colaborater = st.text_input(label="Colaborador :", max_chars=50, placeholder="Digite aqui !!!", key=("Colaborador"))

# Criação do container salário e opções
frame_salary = st.container(border=True)
with frame_salary:
    # Criando duas colunas para salário e salário por dia
    col1, col2 = st.columns([8, 2])
    with col1:
        salary = st.number_input(label="Salário: ", min_value=0, key="Salário")
    with col2:
        day_salary = st.number_input(label="Salário/Dia: ")
    # Criando três colunas para os checkboxes do Abono Pecuniário, Adiantamento e quantidade de dias
    col1, col2, col3 = st.columns([2, 3, 3])
    with col1:
        st.write("Abono Pecuniário")
        yes_abono = st.checkbox(label="Sim", key="yes_abono")
        no_abono = st.checkbox(label="Não", key="no_abono")
    with col2:
        st.write("Adiantamento Décimo Terceiro")
        yes_decimo = st.checkbox(label="Sim", key="yes_decimo")
        no_decimo = st.checkbox(label="Não", key="no_decimo")
    with col3:
        days_monetary = st.number_input(label="Dias de Abono: ", min_value=0, max_value=10,placeholder="Preencha a quantidade de dias de abono", key="DiasAbono")

# Criação do container dos botões
frame_buttons = st.container(border=True)
with frame_buttons:
    # Criando botões calcular e gerar pdf
    col1, col2, col3 = st.columns([10, 40, 10])
    with col1:
        st.button(label="Calcular", key="calcular")
    with col2:
        bar_progress = st.progress(0, text="Ao clicar aguarde o processamento")
    with col3:
        st.button(label="Gerar PDF", key="gerarpdf")

# Criação do container rodapé
frame_end = st.container(border=True)
with frame_end:
    st.image(image_end)