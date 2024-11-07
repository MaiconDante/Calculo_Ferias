# Importando Bibliotecas
import streamlit as st
from fpdf import FPDF
import pandas as pd
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Define o formato para o Brasil

# Funções calcular férias 
def days_vacation():
    return 30 - days_monetary

def value_vacation():
    return days_vacation() * salary_day

def one_third_vacation():
    return value_vacation() / 3

def abono_value(): 
    return days_monetary * salary_day

def one_third_abono():
    return abono_value() / 3

def decimo_value():
    return salary / 2

# Função imprimir recibo férias
def vacation_receipt():
    st.info(f"""| RECIBO DE FÉRIAS |
    
    | Empresa: {company}             |
    | Colaborador: {colaborater}               |
    | {days_vacation()} dias de Férias                    |
    | Salário R$ {salary}                   |
    | Férias R$ {value_vacation():.2f}                    |
    | 1/3 de Férias R$ {one_third_vacation():.2f}              |
    | Abono Pecuniário R$ {abono_value():.2f}           |
    | 1/3 Abono Pecuniário R$ {one_third_abono():.2f}       |
    """)

# Função para validar os campos
def click_calcular():
    valid = True

    if company.isdigit() or len(company) < 4:
        st.error("O nome da [EMPRESA] deve conter letras e ter mais de 4 caracteres !!!")
        valid = False
    else:
        st.success(f"Empresa |VÁLIDA|: {company}")
        
    if colaborater.isdigit() or len(colaborater) < 6:
        st.error("O nome do [COLABORADOR] deve conter letras e ter mais de 6 caracteres !!!")
        valid = False
    else:
        st.success(f"Colaborador |VÁLIDO|: {colaborater}")
        
    if salary <= 0:
        st.error("No campo salário digite apenas | NÚMEROS |")
        valid = False
    else:
        st.success(f"Salário |VÁLIDO|: {salary}")
    
    return valid

# Caminho para o logotipo e rodapé
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
    col1, col2 = st.columns([1, 3]) 
    col1.image(image_path)
    col2.markdown('<div class="centered-title">| Cálculo de Férias RH |</div>', unsafe_allow_html=True)

# Criação do container empresa e colaborador
frame_company = st.container(border=True)
with frame_company:
    st.markdown("Forneça os dados a seguir :")
    company = st.text_input("Empresa :", max_chars=50, placeholder="Digite aqui !!!", key="empresa")
    colaborater = st.text_input("Colaborador :", max_chars=50, placeholder="Digite aqui !!!", key="colaborador")

# Criação do container salário e opções
frame_salary = st.container(border=True)
with frame_salary:
    col1, col2 = st.columns([8, 2])
    with col1:
        salary = st.number_input("Salário:", min_value=0.0, format="%.2f", key="salario")
        salary_day = salary / 30 if salary > 0 else 0
    with col2:
        st.write("Salário/Dia:")
        st.info(f"R$ {salary_day:.2f}")

    col1, col2, col3 = st.columns([2, 3, 3])
    with col1:
        abono_option = st.radio("Abono Pecuniário:", ["Sim", "Não"], key="abono_option")
    with col2:
        decimo_option = st.radio("Adiantamento Décimo:", ["Sim", "Não"], key="decimo_option")
    with col3:
        days_monetary = st.number_input("Dias de Abono:", min_value=0, max_value=10, key="DiasAbono")

    # Inicializa a sessão de estado para controle do pop-up
    if "popup_open" not in st.session_state:
        st.session_state.popup_open = False

# Criação do container dos botões
frame_buttons = st.container(border=True)
with frame_buttons:
    col1, col2, col3 = st.columns([10, 40, 10])
    with col1:
        calculation = st.button("Calcular", key="calcular")
    with col2:
        bar_progress = st.progress(0, text="Ao clicar aguarde o processamento")
    with col3:
        generator_pdf = st.button("Gerar PDF", key="gerarpdf")

    if calculation:
        valid = click_calcular()
        if valid:
            st.session_state.popup_open = True

    if st.session_state.popup_open:
        vacation_receipt()

        col1, col2, col3 = st.columns([20, 20, 10])
        with col2:
            st.button("Fechar Pop-up", on_click=lambda: setattr(st.session_state, "popup_open", False), key="fechar")

# Criação do container rodapé
frame_end = st.container(border=True)
with frame_end:
    st.image(image_end)
