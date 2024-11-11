# Importando Bibliotecas
import streamlit as st
from fpdf import FPDF
import pandas as pd
import locale, time

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # Define o formato para o Brasil

# Inicializa a sessão de estado para controle do pop-up
if "popup_open" not in st.session_state:
    st.session_state.popup_open = False

# Funções calcular férias
def days_vacation():
    return 30 - days_monetary

def value_vacation():
    return days_vacation() * salary_day

def one_third_vacation():
    return value_vacation() / 3

def abono_value():
    return days_monetary * salary_day if abono_option == "Sim" else 0.0

def one_third_abono():
    return abono_value() / 3 if abono_option == "Sim" else 0.0

def decimo_value():
    return salary / 2 if decimo_option == "Sim" else 0.0

def calcule_inss():
    range_1 = 0
    range_2 = 0
    range_3 = 0
    if salary <= 1412:
        range_1 = salary * 0.075
        
    elif salary >= 1412.01 and salary <= 2666.68:
        range_1 = 105.90
        range_2 = (salary - 1412) * 0.09
       
    elif salary >= 2666.69 and salary <= 4000.03:
        range_1 = 105.90
        range_2 = 112.92
        range_3 = (salary - 4000.03) * 0.12
       
    elif salary >= 4000.04:
        range_1 = 105.90
        range_2 = 112.92
        range_3 = (salary - 4000.04) * 0.14
        
    total_inss = range_1 + range_2 + range_3
    return total_inss

# Função para a barra de progresso
def progress_calcule():
    progresso = st.progress(0, text="Aguarde será realizado os cálculos") 
    time.sleep(1) # Inicializa a barra de progresso
    for i in range(1, 11):
        time.sleep(0.2)  # Simula o tempo de processamento (0,2 segundos por etapa)
        progresso.progress(i * 10, text="Realizando processamento de cálculos")  # Atualiza a barra de progresso
    time.sleep(0.5)    
    st.success("Cálculos realizados com SUCESSO")

# Função imprimir recibo férias
def vacation_receipt():
    value_1 = value_vacation()
    value_2 = one_third_vacation()
    value_desconto = calcule_inss()
    value_abono = abono_value()
    value_one_third_abono = one_third_abono()
    value_decimo = decimo_value()
    total_value = value_1 + value_2 + value_abono + value_one_third_abono + value_decimo - value_desconto

    st.info(f"""| RECIBO DE FÉRIAS |
    
    | ---------------------------------------------------------------------|
    | Empresa: {company}           
    | Colaborador: {colaborater}               
    | {days_vacation()} dias de Férias                    
    | Salário R$ {salary}                   
    | Férias R$ {value_1:.2f}                    
    | 1/3 de Férias R$ {value_2:.2f}              
    | Abono Pecuniário R$ {value_abono:.2f}           
    | 1/3 Abono Pecuniário R$ {value_one_third_abono:.2f}       
    | Parcela 1 - Décimo Terceiro R$ {value_decimo:.2f} 
    | Desconto INSS - R$ {value_desconto:.2f}
    | ---------------------------------------------------------------------|
    | TOTAL | R$ {total_value:.2f}
    | ---------------------------------------------------------------------|
    """)

# Função para validar os campos
def click_calcular():
    valid = True

    if company.isdigit() or len(company) < 4:
        st.error("O nome da [EMPRESA] deve conter letras e ter mais de 4 caracteres !!!")
        valid = False
        
    if colaborater.isdigit() or len(colaborater) < 6:
        st.error("O nome do [COLABORADOR] deve conter letras e ter mais de 6 caracteres !!!")
        valid = False
        
    if salary <= 0:
        st.error("No campo salário digite apenas | NÚMEROS |")
        valid = False
    
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

# Função para abrir o sidebar com informações de ajuda
def open_help_sidebar():
    # Estilo CSS para justificar completamente o texto
    st.sidebar.markdown(
        """
        <style>
            .justified-text {
                text-align: justify;
                text-justify: inter-word;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.write("---------------------------")
    st.sidebar.warning("Como funciona o sistema?")
    st.sidebar.write("---------------------------")
    st.sidebar.markdown("""
                <div class="justified-text">
                    Sistema web de cálculo de férias,
                    onde você coloca nome da empresa,
                    nome do colaborador e o salário,
                    com os dados o sistema ja cálcula o valor
                    do dia de serviço, apresentando o valor
                    na tela para o usuário, Após preencher
                    corretamente todos os campos, você terá
                    duas opções: clicar no botão "Calcular"
                    para visualizar o cálculo em um popup no
                    próprio sistema ou selecionar "Gerar PDF"
                    para criar um documento pronto para impressão
                    e visualização.
                </div>
                """,
                unsafe_allow_html=True)

# Criação do container título e logotipo
frame_title = st.container(border=True)
with frame_title:
    col1, col2 = st.columns([1, 3]) 
    col1.image(image_path)
    col2.markdown('<div class="centered-title">| Cálculo de Férias RH |</div>', unsafe_allow_html=True)

# Criação do container empresa e colaborador
frame_company = st.container(border=True)
with frame_company:
    col1, col2 = st.columns([10, 5])
    with col1:
        st.markdown("Forneça os dados a seguir :")
    with col2:
        if st.button("Informações do Sistema   |CLIQUE AQUI|  "):
            open_help_sidebar()

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

# CSS para estilizar o botão
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #114d69; /* Cor de fundo */
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px; /* Bordas arredondadas */
    }
    .stButton>button:hover {
        background-color: #1198d6; /* Cor ao passar o mouse */
        color: white; /* Cor do texto */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Criação do container dos botões
frame_buttons = st.container(border=True)
with frame_buttons:
    col1, col2, col3 = st.columns([15, 55, 18])
    with col1:
        calculation = st.button("Calcular", key="calcular")
    with col2:
        if calculation:
            valid = click_calcular()
            if valid:
                progress_calcule()
                st.session_state.popup_open = True
    with col3:
        generator_pdf = st.button("Gerar PDF", key="gerarpdf")

    if st.session_state.popup_open:
        vacation_receipt()
        col1, col2, col3 = st.columns([20, 20, 10])
        with col2:
            st.button("Fechar Pop-up", on_click=lambda: setattr(st.session_state, "popup_open", False), key="fechar")

# Criação do container rodapé
frame_end = st.container(border=True)
with frame_end:
    st.image(image_end)
