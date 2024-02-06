import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
from selenium import webdriver
import difflib
from selenium.webdriver.common.by import By
import time

st.set_page_config(layout = 'wide')
#inserindo o titulo
st.title('Outros monitoramentos: ANEEL, ANP, ANM')

aba1, aba2, aba3 = st.tabs(['ANEEL', 'ANP', 'ANM'])

with aba1:
    st.title('Informações sobre a ANEEL')
    
    st.text("Link: https://antigo.aneel.gov.br/web/guest/consultas-publicas")
    
    # Título da página do Streamlit
    st.title('Consulta Pública ANEEL')
        
    # Inicialize o navegador
    driver = webdriver.Chrome()  # Você precisa do ChromeDriver instalado
    url = 'https://antigo.aneel.gov.br/web/guest/consultas-publicas'
    driver.get(url)
    
    # Aguarde até que o conteúdo seja totalmente carregado (você pode ajustar o tempo de espera conforme necessário)
    import time
    time.sleep(5)  # Aguarda 5 segundos, você pode ajustar esse valor
    
    # Obtenha o conteúdo da página após o carregamento completo
    page_source = driver.page_source
    
    # Feche o navegador
    driver.quit()
    
    # Analise o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Encontre as informações de cada consulta pública (você pode ajustar os seletores conforme necessário)
    consultas_publicas = soup.find_all('td', class_='table-cell only')
    
    # Itere pelas consultas públicas e extraia as informações desejadas
    for consulta in consultas_publicas:
        # Título da consulta
        titulo_element = consulta.find('h5', class_='titulo-audiencia')
        if titulo_element:
            titulo = titulo_element.text.strip()
        else:
            titulo = "Título não encontrado"
        
        # Descrição da consulta
        descricao_element = consulta.find('div', class_='row-fluid texto')
        if descricao_element:
            descricao = descricao_element.text.strip()
        else:
            descricao = "Descrição não encontrada"
        
        # Link da consulta
        link_element = consulta.find('a', href=True)
        if link_element:
            link = link_element['href']
        else:
            link = "Link não encontrado"
        
        # Imprime as informações
        st.write(f"Título: {titulo}")
        st.write(f"Descrição: {descricao}")
        st.write(f"Link: {link}")
        st.write("="*30)

    st.title('Tomada de Subsídios ANEEL')    
    # Inicialize o navegador
    driver = webdriver.Chrome()  # Você precisa do ChromeDriver instalado
    url = 'https://antigo.aneel.gov.br/web/guest/tomadas-de-subsidios'
    driver.get(url)
    
    # Aguarde até que o conteúdo seja totalmente carregado (você pode ajustar o tempo de espera conforme necessário)
    import time
    time.sleep(5)  # Aguarda 5 segundos, você pode ajustar esse valor
    
    # Obtenha o conteúdo da página após o carregamento completo
    page_source = driver.page_source
    
    # Feche o navegador
    driver.quit()
    
    # Analise o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Encontre as informações de cada consulta pública (você pode ajustar os seletores conforme necessário)
    consultas_publicas = soup.find_all('td', class_='table-cell only')
    
    # Itere pelas consultas públicas e extraia as informações desejadas
    for consulta in consultas_publicas:
        # Título da consulta
        titulo_element = consulta.find('h5', class_='titulo-audiencia')
        if titulo_element:
            titulo = titulo_element.text.strip()
        else:
            titulo = "Título não encontrado"
        
        # Descrição da consulta
        descricao_element = consulta.find('div', class_='row-fluid texto')
        if descricao_element:
            descricao = descricao_element.text.strip()
        else:
            descricao = "Descrição não encontrada"
        
        # Link da consulta
        link_element = consulta.find('a', href=True)
        if link_element:
            link = link_element['href']
        else:
            link = "Link não encontrado"
        
        # Imprime as informações
        st.write(f"Título: {titulo}")
        st.write(f"Descrição: {descricao}")
        st.write(f"Link: {link}")
        st.write("="*30)

    st.title('Audiência Pública ANEEL')    

    driver = webdriver.Chrome()  # Você precisa do ChromeDriver instalado
    url = 'https://antigo.aneel.gov.br/web/guest/audiencias-publicas'
    driver.get(url)
    
    # Aguarde até que o conteúdo seja totalmente carregado (você pode ajustar o tempo de espera conforme necessário)
    import time
    time.sleep(5)  # Aguarda 5 segundos, você pode ajustar esse valor
    
    # Obtenha o conteúdo da página após o carregamento completo
    page_source = driver.page_source
    
    # Feche o navegador
    driver.quit()
    
    # Analise o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Encontre as informações de cada consulta pública (você pode ajustar os seletores conforme necessário)
    consultas_publicas = soup.find_all('td', class_='table-cell only')
    
    # Itere pelas consultas públicas e extraia as informações desejadas
    for consulta in consultas_publicas:
        # Título da consulta
        titulo_element = consulta.find('h5', class_='titulo-audiencia')
        if titulo_element:
            titulo = titulo_element.text.strip()
        else:
            titulo = "Título não encontrado"
        
        # Descrição da consulta
        descricao_element = consulta.find('div', class_='row-fluid texto')
        if descricao_element:
            descricao = descricao_element.text.strip()
        else:
            descricao = "Descrição não encontrada"
        
        # Link da consulta
        link_element = consulta.find('a', href=True)
        if link_element:
            link = link_element['href']
        else:
            link = "Link não encontrado"
        
        # Imprime as informações
        st.write(f"Título: {titulo}")
        st.write(f"Descrição: {descricao}")
        st.write(f"Link: {link}")
        st.write("="*30)

with aba2:
    st.title('Informações sobre a ANP')
    
    st.text("Link: https://www.gov.br/anp/pt-br/assuntos/consultas-e-audiencias-publicas")
    # Configurar o driver do Chrome (ou outro navegador de sua escolha)
    driver = webdriver.Chrome()
    
    # URL da página
    url = 'https://www.gov.br/anp/pt-br/assuntos/consultas-e-audiencias-publicas/consulta-audiencia-publica'
    
    # Abrir a página usando o Selenium
    driver.get(url)
    
    # Aguardar até que as informações sejam carregadas (aqui, esperamos 10 segundos, mas você pode ajustar conforme necessário)
    time.sleep(10)
    
    # Obter o HTML da página após o carregamento dinâmico
    page_source = driver.page_source
    
    # Analisar o HTML da página usando BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Encontrar todas as divs com a classe "tab-content active"
    consultas = soup.find_all('div', class_='tab-content active')
    
    # Loop através das consultas e imprima as informações formatadas
    for consulta in consultas:
        # Extrair o título da consulta
        titulo = consulta.text
    strings = titulo.strip().split("\n")
    
    # Crie um loop para formatar e imprimir as informações
    for s in strings:
        info = s.split("\n")
        title = info[0]
        details = "\n".join(info[1:])
        
        st.write(f"- {title}")
        st.write("=" * 40)  # Linha de separação entre as entradas
    
    driver.quit()


with aba3:
    st.title('Informações sobre a ANM')
    
    st.text("Link: https://www.gov.br/anm/pt-br/acesso-a-informacao/participacao-social")
    