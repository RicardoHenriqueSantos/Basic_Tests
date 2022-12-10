from num2words import num2words

num = int(input("Insira um número: "))

num_en = num2words(num, lang='en')
num_pt = num2words(num, lang='pt-br')
num_en_ord = num2words(num, lang='en', to='ordinal')
num_pt_ord = num2words(num, lang='pt-br', to='ordinal')

print(f"Em Inglês: {num_en}")
print(f"Em inglês [Ordinal]: {num_en_ord}")
print(f"Em Português: {num_pt}")
print(f"Em Português [Ordinal]: {num_pt_ord}")
