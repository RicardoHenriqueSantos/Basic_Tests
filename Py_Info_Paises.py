from countryinfo import CountryInfo

pais = CountryInfo(input("INSIRA O NOME DO PAÍS: "))
print()
print(f"PAÍS: {pais.name()}")
print(f"NOME NATIVO: {pais.native_name()}")
print(f"CAPITAL: {pais.capital()}")
print(f"POPULAÇÃO: {pais.population()}")
print(f"CÓDIGO DE ÁREA: {pais.calling_codes()}")
print(f"MOEDAS: {pais.currencies()}")
print(f"IDIOMA: {pais.languages()}")
print(f"REGIÃO: {pais.region()}")

