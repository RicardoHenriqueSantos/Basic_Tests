# IMPORTANDO PANDAS
import pandas as pd

# ABRIR ARQUIVO EXCEL
df = pd.read_excel("EXCEL.xlsx", engine="openpyxl")

# SABER QUAIS ABAS EXISTEM NO ARQUIVO
arquivo_excel = pd.ExcelFile("EXCEL.xlsx")
print(arquivo_excel.sheet_names)

# CASO QUEIRA ESCOLHER UMA ABA DIFERENTE
'''df = pd.read_excel("EXCEL.xlsx", engine="openpyxl", sheet_name="Aba 2")'''

# UTILIZANDO O PARSE
aba1 = arquivo_excel.parse("Vendas")
aba2 = arquivo_excel.parse("Aba 2")

# VISUALIZANDO A ABA SELECIONADA
print(aba2.head())
