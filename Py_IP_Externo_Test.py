import json                         # BIBLIOTECA QUE FORNECE OPERAÇÃO DE CODIFICAÇÃO E DECODIFICAÇÃO JSON
from urllib.request  import urlopen # FUNÇÕES E CLASSES QUE AJUDAM A ABRIR URLs

# URL DO SITE DAS INFORMAÇÕES
url = "http://ipinfo.io/json"

# ABRE A URL E ENVIA A REQUISIÇÃO À RESPOSTA
resposta = urlopen(url)

# CARREGA OS DADOS DA RESPOSTA
dados = json.load(resposta)

# IMPRIMINDO OS DADOS
print(f"IP: {dados['ip']}")
print(f"PAÍS: {dados['country']}")
print(f"ESTADO: {dados['region']}")
print(f"CIDADE: {dados['city']}")
print(f"ZONA: {dados['timezone']}")