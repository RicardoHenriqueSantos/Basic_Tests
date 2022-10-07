# IMPORTANDO PANDAS E SQLALCHEMY
import pandas as pd
from sqlalchemy import create_engine

# CRIANDO UMA URL PARA CONEXÃO COM BANCO DE DADOS
engine = create_engine('<>://<>:<>@<>/<>')
cnx = engine.connect()

# REALIZAÇÃO DA PESQUISA DOS DADOS
query = "SELECT * FROM venda"
dados = pd.read_sql_query(query, cnx)

# SELECIONANDO DADOS DA PESQUISA
print(dados[['ven_data', 'ven_total']].head())

# ADICIONANDO UMA NOVA COLUNA
# OBS: A JUNÇÃO SÓ FUNCIONA COM STRINGS ENTÃO É NECESSÁRIO TRANSFORMAR EM STRING
dados['cod_funcionario_produto'] = dados['ven_cod_fun'].apply(str) + " - " + dados['ven_cod_produto'].apply(str)
print(dados.head())
