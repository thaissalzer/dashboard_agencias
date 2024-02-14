import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
from selenium import webdriver
import difflib
import os
from selenium.webdriver.chrome.options import Options



st.set_page_config(layout = 'wide')
#inserindo o titulo
st.title('Monitoramento CGTS: ANAC, ANA, ANTAQ e ANTT')

aba1, aba2 = st.tabs(['ANAC', 'ANA'])

with aba1:
    st.title('Informações sobre a ANAC')


with aba2:
    
    # Configurar o caminho para o Chrome WebDriver usando a biblioteca os
    chrome_driver_path = os.path.join(os.getcwd(), 'chromedriver')
    
    with st.sidebar:
        st.title('Informações sobre a ANA')
        st.text("Link: https://participacao-social.ana.gov.br/")
    
    # Configurar as opções do Chrome
    options = Options()
    
    # Desativar a exibição da interface do navegador
    options.headless = True
    
    # Criar uma instância do driver do Selenium
    driver = webdriver.Chrome(options=options)
    
    # URL da página que você deseja consultar
    url = "https://participacao-social.ana.gov.br/"
    
    # Acessar a página usando o driver do Selenium
    driver.get(url)
    
    # Aguardar algum tempo para a página carregar completamente (ajuste conforme necessário)
    driver.implicitly_wait(10)
    
    # Obter o código HTML da página carregada pelo Selenium
    html = driver.page_source
    
    # Parsear o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Encontrar a tabela com o id "tableContent"
    table = soup.find('table', id='tableContent')
    
    # Inicializar listas vazias para armazenar os dados
    numeros = []
    meios_de_participacao = []
    objetos = []
    periodos_de_contribuicao = []
    
    # Encontrar todas as linhas da tabela
    rows = table.find_all('tr')
    
    # Iterar sobre as linhas da tabela, excluindo o cabeçalho
    for row in rows[1:]:
        # Encontrar as células da linha (colunas)
        cells = row.find_all('td')
    
        # Extrair as informações de cada célula
        numero = cells[0].text.strip()
        meio_de_participacao = cells[1].text.strip()
        objeto = cells[2].text.strip()
        periodo_de_contribuicao = cells[3].text.strip()
    
        # Adicionar os dados às listas
        numeros.append(numero)
        meios_de_participacao.append(meio_de_participacao)
        objetos.append(objeto)
        periodos_de_contribuicao.append(periodo_de_contribuicao)
    
    # Fechar o driver do Selenium quando terminar
    driver.quit()
    
    # Criar um DataFrame com os dados
    data = {
        "Número": numeros,
        "Meio de Participação": meios_de_participacao,
        "Objeto": objetos,
        "Período de Contribuição": periodos_de_contribuicao
    }
    
    df_ana = pd.DataFrame(data)
    
    # Exibir o DataFrame
    st.dataframe(df_ana)
