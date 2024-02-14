import shutil
import os
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import difflib



st.set_page_config(layout = 'wide')
#inserindo o titulo
st.title('Monitoramento CGTS: ANAC, ANA, ANTAQ e ANTT')

aba1, aba2, aba3, aba4 = st.tabs(['ANAC', 'ANA', 'ANTAQ', 'ANTT'])

with aba1:
    st.title('Informações sobre a ANAC')

    url = "https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/consultas-publicas/consultas-publicas-em-andamento/consulta-publica"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontra todos os elementos <p> com a classe 'callout'
    consultas = soup.find_all('p', class_='callout')
    
    # Listas para armazenar os dados das consultas públicas
    consulta_numero_list = []
    texto_associado_list = []
    periodo_list = []
    
    # Itera sobre todos os elementos <p> com classe 'callout'
    for consulta in consultas:
        consulta_numero = consulta.find('strong').text
        
        # Encontrar o próximo elemento <p> com a classe especificada
        elemento_encontrado = consulta.find_next('p', class_='Texto_Justificado_Recuo_Primeira_Linha_Esp_Simples')
        
        # Verificar se o elemento foi encontrado
        if elemento_encontrado:
            texto_associado = elemento_encontrado.text
        else:
            texto_associado = "Nenhum texto encontrado"
        
        periodo = "Não especificado"
    
        # Encontre o próximo elemento que contenha "Período:" na sequência
        for sibling in consulta.find_next_siblings():
            if "Período:" in sibling.text:
                periodo = sibling.find('strong').text
                break
    
        consulta_numero_list.append(consulta_numero)
        texto_associado_list.append(texto_associado)
        periodo_list.append(periodo)    
    
    # Crie um DataFrame a partir das listas
    data = {'Consulta Pública': consulta_numero_list, 'Texto Associado': texto_associado_list, 'Período': periodo_list}
    df = pd.DataFrame(data)
    
    # Defina a largura máxima da coluna "Texto Associado"
    pd.set_option('display.max_colwidth', 1000)  # Defina o valor que você preferir
    st.text("Consultas e Audiências Públicas")
    st.text("Link: https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/consultas-publicas/consultas-publicas-em-andamento/consulta-publica")
    st.dataframe(df)

    st.text("Consultas Setoriais")
    st.text("Link:https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/consultas-setoriais/consultas-em-andamento")
    url = "https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/consultas-setoriais/consultas-em-andamento"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontra todos os elementos <strong> com o texto 'Consulta Setorial'
    consulta_numeros = soup.find_all('strong', string=lambda t: t and t.startswith('Consulta Setorial'))
    
    # Listas para armazenar os dados das consultas setoriais
    consulta_numero_list = []
    texto_associado_list = []
    periodo_list = []
    aviso_links_list = []
    minuta_links_list = []
    justificativa_links_list = []
    formulario_links_list = []
    
    # Itera sobre os elementos <strong> encontrados
    for consulta_numero in consulta_numeros:
        consulta_numero_text = consulta_numero.text
        texto_associado = consulta_numero.find_next('p', class_='textojustificadorecuoprimeiralinhaespsimples').text
        periodo_element = consulta_numero.find_next('strong', string=lambda t: t and t.startswith('Período:'))
        periodo = periodo_element.text if periodo_element else "Não especificado"
    
        consulta_numero_list.append(consulta_numero_text)
        texto_associado_list.append(texto_associado)
        periodo_list.append(periodo)
    
        # Links relacionados
        links = consulta_numero.find_next('ul', type='disc').find_all('a')
        aviso_link = next((link['href'] for link in links if 'Aviso' in link.text), None)
        minuta_link = next((link['href'] for link in links if 'Minuta de IS' in link.text), None)
        justificativa_link = next((link['href'] for link in links if 'Justificativa' in link.text), None)
        formulario_link = next((link['href'] for link in links if 'Formulário' in link.text), None)
    
        aviso_links_list.append(aviso_link)
        minuta_links_list.append(minuta_link)
        justificativa_links_list.append(justificativa_link)
        formulario_links_list.append(formulario_link)
    
    # Crie um DataFrame a partir das listas
    data = {
        'Consulta Setorial': consulta_numero_list,
        'Texto Associado': texto_associado_list,
        'Período': periodo_list,
        'Link Aviso': aviso_links_list,
        'Link Minuta': minuta_links_list,
        'Link Justificativa': justificativa_links_list,
        'Link Formulário': formulario_links_list
    }
    df_setorial = pd.DataFrame(data)
    
    # Imprima o DataFrame
    st.dataframe(df_setorial)

    st.text("Tomada de Subsidios")
    st.text("Link:https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/tomada-de-subsidios")
    # URL da página que você deseja consultar
    url = "https://www.gov.br/anac/pt-br/acesso-a-informacao/participacao-social/tomada-de-subsidios"
    
    # Fazer uma solicitação GET para a página
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
    
        # Encontre a tag <a> com a classe 'internal-link'
        a_tag = soup.find('a', class_='internal-link')
    
        if a_tag:
            # Extrai o texto e o link
            texto = a_tag.text
            link = a_tag['href']
    
            # Crie um DataFrame com os dados
            data = {'Texto': [texto], 'Link': [link]}
            df_tomada = pd.DataFrame(data)
    
            # Exibe o DataFrame
            print(df)
    
        else:
            print("Tag <a> não encontrada na página.")
    
    else:
        print("Não foi possível acessar a página. Código de status:", response.status_code)
    st.dataframe(df_tomada)

def get_logpath():
    return os.path.join(os.getcwd(), 'selenium.log')
    
def get_chromedriver_path():
    return shutil.which('chromedriver')

def get_webdriver_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    return options


def get_webdriver_service():
    service = Service(
        executable_path=get_chromedriver_path(),
        log_output=get_logpath()
    )
    return service
    
with aba2:
    st.title('Informações sobre a ANA')
    st.text("Link: https://participacao-social.ana.gov.br/")

with aba3:
    st.title('Informações sobre a ANTAQ')
    st.text("Link: https://www.gov.br/antaq/pt-br/acesso-a-informacao/participacao-social/audiencias-e-consultas-publicas/proximas-audiencias-publicas-1")


with aba4:
    st.title('Informações sobre a ANTT')
    st.text("Link: https://participantt.antt.gov.br/Site/AudienciaPublica/ConsultarAvisoAudienciaPublica.aspx")
    url = 'https://participantt.antt.gov.br/Site/AudienciaPublica/ConsultarAvisoAudienciaPublica.aspx'

    # Fazer uma solicitação GET para a página
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Encontre todas as tags <tr> dentro do <table>
        tr_tags = soup.find_all('table', {'id': 'Corpo_gvAudiencias'})[0].find_all('tr')
    
        data = []
    
        for tr in tr_tags[1:]:  # Comece a partir do segundo <tr> para ignorar o cabeçalho da tabela
            td_tags = tr.find_all('td')
    
            tipo_evento = td_tags[0].find('span').text.strip()
            numero_audiencia = td_tags[1].find('a').text.strip()
            descricao = td_tags[2].find('span').text.strip()
            situacao = td_tags[3].text.strip()
            periodo_validade = td_tags[4].text.strip()
    
            data.append([tipo_evento, numero_audiencia, descricao, situacao, periodo_validade])
    
        # Crie um DataFrame com os dados
        df_ANTT = pd.DataFrame(data, columns=["Tipo de Evento", "Número da Audiência", "Descrição", "Situação", "Período de Validade"])
    
    st.dataframe(df_ANTT)
