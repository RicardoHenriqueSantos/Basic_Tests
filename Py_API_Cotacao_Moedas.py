import requests

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = cotacao.json()

print(f" Dólar R$ {cotacao['USDBRL']['bid']}")
print(f" Euro R$ {cotacao['EURBRL']['bid']}")
print(f" Bitcoin R$ {cotacao['BTCBRL']['bid']}")
