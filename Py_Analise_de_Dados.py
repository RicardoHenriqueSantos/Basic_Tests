import pandas as pd
import plotly.express as px

# BAIXE O ARQUIVO TELECOM_USERS.csv COMO SUA BASE DE DADOS

# PASSO 1 - IMPORTAR BASE DE DADOS
tabela = pd.read_csv(r"",
                     encoding="UTF-8", sep=",")

# PASSO 2 - VISUALIZAR A BASE DE DADOS
tabela = tabela.drop("Unnamed: 0", axis=1)

# PASSO 3 - TRATAMENTO DOS DADOS
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info)

# PASSO 4 - ANÁLISE INICIAL DOS DADOS
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# PASSO 5 - DESCOBRIR OS MOTIVOS DOS CANCELAMENTOS

for coluna in tabela.columns:
    # CRIAÇÃO DO GRÁFICO
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # EXIBIÇÃO DO GRÁFICO
    grafico.show()

# CONCLUSÃO
'''
 - Clientes mais recentes tendem a cancelar mais que os antigos.
    - A primeira impressão do cliente pode estar ruim.
    - O início do serviço pode estar confuso.
    - Realizar uma promoção.
    - Promoções e incentivos nos primeiros meses.
 - A forma de pagamento com "Boleto Eletrônico" gera muito mais cancelamento.
    - Oferecer desconto em outras formas de pagamento.
 - O tipo de contrato mensal possui mais chances de cancelamento.
    - Oferecer um plano anual.
 - Quanto mais serviços os clientes possuem é menor a chance de cancelamento.
    - Oferecer novos recursos com um preço bem em conta.
 - Clientes com um número maior de pessoas é menor a chance de cancelamento.
    - Oferecer mais linhas gratuitas ou com um preço em conta.
'''