from bs4 import BeautifulSoup # IMPORTA A BIBLIOTECA DE EXTRAÇÃO DE DADOS DE ARQUIVOS HTML E XML
import requests               # IMPORTA A BIBLIOTECA QUE PERMITE QUE VOCÊ ENVIE SOLICITAÇÕES HTTP EM PYTHON

# INFORMA O SITE NO QUAL SERÃO ADQUIRIDAS AS INFORMAÇÕES | CONTENT SERVE PARA PEGAR TODO O CONTEÚDO
site = requests.get("https://www.climatempo.com.br/").content

# O OBJETO BAIXA O HTML DO SITE
soup = BeautifulSoup(site, "html.parser")

# PRETTIFY TRANSFORMA O HTML EM STRING
print(soup.prettify())

