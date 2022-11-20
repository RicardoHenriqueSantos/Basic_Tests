# IMPORTANDO PANDAS
import pandas as pd

# ABRIR ARQUIVO CSV
df = pd.read_csv("CSV.csv", encoding="ANSI", sep=";")

# UTILIZA A LINHA SELECIONADA COMO CABEÇALHO
'''df = pd.read_csv("Pandas Ler CSV.csv", encoding="ANSI", sep=";", header=0)'''

# SELECIONA AS COLUNAS A SEREM VISUALIZADAS
'''df = pd.read_csv("Pandas Ler CSV.csv", encoding="ANSI", sep=";", usecols=['Dia', 'Faturamento'])'''

# SELECIONA A QUANTIDADE DE LINHAS A SERER VISUALIZADAS
'''df = pd.read_csv("Pandas Ler CSV.csv", encoding="ANSI", sep=";", usecols=['Dia', 'Faturamento'], nrows=200)'''

# EXIBIR DADOS DO ARQUIVO
print(df.head())

# EXIBIR FORMATO DO AQUIVO [LINHAS, COLUNAS]
print(df.shape)
