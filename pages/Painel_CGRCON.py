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
st.title('Monitoramento CGRCON: ANVISA, ANS, ANCINE, ANATEL')

aba1, aba2, aba3, aba4 = st.tabs(['ANVISA', 'ANS', 'ANCINE', 'ANATEL'])


with aba1:
    st.title('Informações sobre a ANS')
    
    url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/consultas-publicas'
    
    html =  requests.get(url)
    
    soup = BeautifulSoup(html.text, 'html.parser')
    
    # Encontre a tabela de consultas públicas em andamento
    table = soup.find('table', class_='table-bordered')
    
    # Encontre todas as linhas das consultas
    rows = table.find_all('tr')[1:]  # Ignorar a primeira linha de cabeçalho
    
    # Lista para armazenar as informações das consultas
    consultas_info = []
    
    for row in rows:
        cells = row.find_all('td')
        
        numero = cells[0].text
        descricao = cells[1].text
        periodo = cells[2].text
        link = cells[3].find('a')['href']
        
        consulta_info = {
            "Número": numero,
            "Descrição": descricao,
            "Período": periodo,
            "Link de Acesso": link
        }
        
        consultas_info.append(consulta_info)
    
    # Criar uma interface Streamlit
    st.text("Link : https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/consultas-publicas")
    
    # Iterar sobre as informações de consulta e exibi-las na interface
    for consulta in consultas_info:
        st.subheader(f'Consulta pública n°: {consulta["Número"]}')
        st.write("Descrição:", consulta["Descrição"])
        st.write("Período:", consulta["Período"])
        st.write("Link de Acesso:", consulta["Link de Acesso"])
        st.write("=" * 50)  # Para separar as informações de cada consulta

with aba2:
    st.title('Informações sobre a ANCINE')
    st.text("Link: https://www.gov.br/participamaisbrasil/consultaspublicas")
    st.text("Última consulta pública atualizada:")
    import requests
    from bs4 import BeautifulSoup
    
    # URL da página que você deseja acessar
    url = "https://www.gov.br/participamaisbrasil/agencia-nacional-do-cinema"
    
    # Faz a requisição HTTP
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Parseia o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra todos os elementos <div> com a classe "itens"
        divs = soup.find_all('div', class_='itens')
        
        # Itera sobre os elementos <div> encontrados
        for div in divs:
            # Extrai o texto da consulta pública
            texto_consulta = div.find('span', class_='textoConsulta').text.strip()
            
            # Extrai a área
            area = div.find('span', class_='areas').text.strip()
            
            # Extrai a data de início
            data_inicio = div.find('span', class_='dados-card').text.strip()
            
            # Extrai o status
            status = div.find('span', class_='status').text.strip()
            
            # Imprime as informações extraídas
            st.write("Texto da Consulta Pública:", texto_consulta)
            st.write("Área:", area)
            st.write("Data de Início:", data_inicio)
            st.write("Status:", status)
            st.write("\n")
    else:
        st.write("Erro ao acessar a página:", response.status_code)

with aba3:
    st.title('Informações sobre a ANATEL')
    
    st.text("Link: https://apps.anatel.gov.br/ParticipaAnatel/Home.aspx")
    
    st.title("Consultas públicas: ")
    import requests # para fazer requisições ao site 
    from bs4 import BeautifulSoup
    # definindo a página que queremos extrair informações
    url = 'https://apps.anatel.gov.br/ParticipaAnatel/Home.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontra todos os elementos div com a classe 'ListRecordsItem'
    items = soup.find_all('div', class_='ListRecordsItem')
    
    # Itera sobre todos os itens encontrados
    for item in items:
        # Encontre o elemento com a classe "text-primary font-semi-bold"
        titulo_element = item.find('span', class_='text-primary font-semi-bold')
        
        # Encontre todos os elementos com a classe "text-neutral-7"
        elementos_descricao = item.find_all('span', class_='text-neutral-7')
        
        # Encontre o link dentro do item
        link_element = item.find('a')
        
        # Verifique se o título, pelo menos um elemento de descrição e o link foram encontrados
        if titulo_element and elementos_descricao and link_element:
            # Extraia o texto do título
            titulo_text = titulo_element.text
            
            # Inicialize uma lista para armazenar os textos das descrições
            descricao_texts = []
            
            # Itera sobre os elementos de descrição encontrados e extrai seus textos
            for descricao_element in elementos_descricao:
                descricao_texts.append(descricao_element.text)
            
            # Extraia o URL do link
            link_href = link_element.get('href')
            
            # Imprima o título, os textos das descrições e o URL do link
            st.text( titulo_text)
            st.text("Descrições:")
            for descricao_text in descricao_texts:
                st.text(descricao_text)
            
            st.text(" ")  # Adicione uma linha em branco para separar os resultados
    
    st.title("Tomada de Subsídios")
    
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup
    import time
    
    # Inicialize o driver do Selenium
    driver = webdriver.Chrome()
    
    # Abra a página
    driver.get("https://apps.anatel.gov.br/ParticipaAnatel/Home.aspx")
    
    # Clique no botão (substitua o seletor CSS correto do botão)
    botao = driver.find_element(By.CSS_SELECTOR, '#wt32_OutSystemsUIWeb_wt21_block_wtContent_wtMainContent_wt11_OutSystemsUIWeb_wt43_block_wtColumn2_wt42')
    botao.click()
    
    # Aguarde um tempo para que o conteúdo seja carregado (ajuste conforme necessário)
    time.sleep(5)
    
    # Obtenha o HTML da página atualizada
    pagina_atualizada = driver.page_source
    
    # Use o BeautifulSoup para analisar a página atualizada
    soup = BeautifulSoup(pagina_atualizada, 'html.parser')
    
    # Encontra todos os elementos div com a classe 'ListRecordsItem'
    items = soup.find_all('div', class_='ListRecordsItem')
    
    # Itera sobre todos os itens encontrados
    for item in items:
        # Encontre o elemento com a classe "text-primary font-semi-bold"
        titulo_element = item.find('span', class_='text-primary font-semi-bold')
        
        # Encontre todos os elementos com a classe "text-neutral-7"
        elementos_descricao = item.find_all('span', class_='text-neutral-7')
        
        # Verifique se o título e pelo menos um elemento de descrição foram encontrados
        if titulo_element and elementos_descricao:
            # Extraia o texto do título
            titulo_text = titulo_element.text
            
            # Inicialize uma lista para armazenar os textos das descrições
            descricao_texts = []
            
            # Itera sobre os elementos de descrição encontrados e extrai seus textos
            for descricao_element in elementos_descricao:
                descricao_texts.append(descricao_element.text)
            
            # Imprima o título, os textos das descrições e o URL do link
            st.text( titulo_text)
            st.text("Descrições:")
            for descricao_text in descricao_texts:
                st.text(descricao_text)
            
            st.text(" ")  # Adicione uma linha em branco para separar os resultados
    
    
    # Feche o driver do Selenium
    driver.quit()

with aba4:
    st.title('Informações sobre a ANVISA')
    st.text("Link: https://antigo.anvisa.gov.br/consultas-publicas#/")
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    
    # Crie uma instância do driver do Selenium (certifique-se de ter o WebDriver apropriado instalado)
    driver = webdriver.Chrome()
    
    # Acesse a URL
    url = 'https://antigo.anvisa.gov.br/consultas-publicas#/'
    driver.get(url)
    
    # Espere o carregamento dos elementos (ajuste o tempo conforme necessário)
    wait = WebDriverWait(driver, 10)
    elementos_li = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.ng-scope')))
    
    # Crie listas para as colunas
    cp_list = []
    status_list = []
    assunto_list = []
    
    # Itere sobre os elementos <li> encontrados
    for li in elementos_li:
        try:
            # Encontre o elemento <a> dentro de cada <li> com a classe "ng-binding"
            elemento_a = li.find_element(By.CSS_SELECTOR, 'a.ng-binding')
    
            # Encontre o elemento que contém o status (por exemplo, "Aberto")
            elemento_status = li.find_element(By.CSS_SELECTOR, 'p.ng-binding')
    
            # Encontre o elemento que contém o assunto resumido
            elemento_assunto = elemento_status.find_element(By.XPATH, './following-sibling::p')
    
            # Acesse os textos dos elementos
            texto_a = elemento_a.text.strip()
            texto_status = elemento_status.text.strip()
            texto_assunto = elemento_assunto.text.strip()
    
            # Adicione os valores às listas
            cp_list.append(texto_a)
            status_list.append(texto_status)
            assunto_list.append(texto_assunto)
    
    
    
        except NoSuchElementException:
            pass
    
    # Crie o DataFrame
    df1 = pd.DataFrame({
        'CP:': cp_list,
        'Status:': status_list,
        'Assunto resumido:': assunto_list
    })
    
    # Encerre o driver do Chrome
    driver.quit()
    
    # Imprima o DataFrame
    st.dataframe(df1)
    


