import wikipedia
from googletrans import Translator

sumario_en = wikipedia.summary(input("INSIRA O QUE DESEJA PESQUISAR: "))

traducao = Translator()

sumario_pt = traducao.translate(sumario_en, dest='pt')

print(sumario_pt.text)
