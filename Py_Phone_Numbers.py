import phonenumbers
from phonenumbers import geocoder, carrier

cod = "+" + input("INSIRA O CÓDIGO DO PAÍS: ")
ddd = input("INSIRA O DDD: ")
numero = input("INSIRA O NÚMERO DO TELEFONE: ")
numero_cel = cod + ddd + numero

numero_cel = phonenumbers.parse(numero_cel)
operadora = carrier.name_for_number(numero_cel, "pt-br")
regiao = geocoder.description_for_number(numero_cel, "pt-br")

print(f"\nOPERADORA: {operadora.upper()}")
print(f"REGIÃO: {regiao.upper()}")