from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# BAIXE O ARQUIVO PRODUTOS.xlsx COMO SUA BASE DE DADOS

navegador = webdriver.Chrome()

# PASSO 1 - PEGAR A COTACAO DOLAR

navegador.get("https://www.google.com.br")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys("Cotação dólar")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys(Keys.ENTER)
dolar = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')\
    .get_attribute('data-value')
print(dolar)

# PASSO 2 - PEGAR A COTACAO EURO
navegador.get("https://www.google.com.br")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys("Cotação euro")
navegador.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")\
    .send_keys(Keys.ENTER)
euro = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')\
    .get_attribute('data-value')
print(euro)

# PASSO 3 - PEGAR A COTACAO OURO
navegador.get("https://www.melhorcambio.com/ouro-hoje")
ouro = navegador.find_element("xpath", '//*[@id="comercial"]')\
    .get_attribute("value")
ouro = ouro.replace(',', '.')
print(ouro)

navegador.quit()

# PASSO 4 - ATUALIZAR A BASE DE DADOS

tabela = pd.read_excel(r"")
print(tabela.head())

# PASSO 5 - RECALCULAR OS PRECOS

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(ouro)
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

print(tabela.head())

# PASSO 6 - EXPORTAR A BASE DE DADOS
tabela.to_excel("Produtos Update.xlsx", index=False)
