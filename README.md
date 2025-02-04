# Cálculo de Férias RH
Projeto desenvolvido com Streamlit para calcular as férias de colaboradores, gerando um recibo detalhado e oferecendo a opção de download em PDF.

## Funcionalidades
- Cálculo Automático: Com base no salário do colaborador, o sistema calcula o valor das férias, o abono pecuniário, o adiantamento de décimo terceiro e os descontos do INSS.
- Geração de PDF: Crie um recibo de férias personalizado e faça o download em formato PDF.
- Interface Intuitiva: Inserção fácil de dados da empresa, do colaborador e de outras informações financeiras, com um layout amigável.
- Ajuda Integrada: Informações úteis sobre como utilizar o sistema, disponíveis na barra lateral.

## Tecnologias Utilizadas
* Python
* Streamlit: Framework utilizado para criar a interface web.
* FPDF: Biblioteca para a geração de PDFs.
* Locale: Para formatação de datas e valores conforme o padrão brasileiro.
* Datetime: Manipulação de datas.
* I/O e Time: Para controle de tempo e buffers de dados.

### Como Executar
Pré-requisitos: Certifique-se de ter Python instalado (versão 3.7 ou superior) e as bibliotecas necessárias.
Instalação das Dependências:
-> pip install streamlit fpdf

### Executar o Projeto:
-> streamlit run nome_do_arquivo.py
Estrutura do Sistema

Entrada de Dados: Informações da empresa, do colaborador, salário e opções de abono e décimo terceiro.
Cálculos Realizados:
Dias e valor das férias
Um terço adicional das férias
Abono pecuniário e seu terço
Desconto do INSS
Adiantamento do décimo terceiro
Barra de Progresso: Simula o processamento dos cálculos.
Exibição do Recibo: Um recibo detalhado é gerado e exibido na tela.
Geração de PDF: Com todos os valores calculados e formatados.

### Como Utilizar
Preencha as informações no formulário da interface.
Clique em "Calcular" para visualizar o recibo na tela.
Se desejar, clique em "Gerar PDF" para criar o recibo e baixá-lo.
A barra lateral contém explicações sobre o funcionamento do sistema.

### Contribuição
Fork o projeto.
Crie uma nova branch (git checkout -b feature/nome-da-feature).
Commit suas mudanças (git commit -m 'Adicionar nova feature').
Envie para a branch principal (git push origin feature/nome-da-feature).
Abra um Pull Request.