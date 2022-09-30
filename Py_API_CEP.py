import requests

user = input("Insira o cep: ")

cep = requests.get(f"https://cep.awesomeapi.com.br/json/{user}")
cep = cep.json()

print(f"{cep['address_type']} {cep['address_name']} - {cep['district']}")
print(f"{cep['city']} - {cep['state']}")
