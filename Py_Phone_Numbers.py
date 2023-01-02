import phonenumbers
from phonenumbers import geocoder, carrier

cod = "+" + input("Insira o código do país: ")
ddd = input("Insira o DDD: ")
numero = input("Insira o número do telefone: ")
numero_cel = cod + ddd + numero

numero_cel = phonenumbers.parse(numero_cel)
operadora = carrier.name_for_number(numero_cel, "pt-br")
regiao = geocoder.description_for_number(numero_cel, "pt-br")

print()
print(f"Operadora: {operadora}")
print(f"Região: {regiao}")