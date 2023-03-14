import requests                 # FAZ REQUISIÇÕES HTTP
from bs4 import BeautifulSoup   # REALIZA TRABALHOS COM HTML E XML
import operator                 # IMPLEMENTA OPERADORES
from collections import Counter # MANIPULAR LISTAS, TUPLAS E DICIONÁRIOS

# A FUNÇÃO DEFINE E INICIA TODO WEB CRAWLER
def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")

    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

# FUNÇÃO PARA REMOVER TODOS OS ITENS INDESEJADOS
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$^&*()_-+={[}]|\;:"<>?/.,'

        for i in range(8, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


# FUNÇÃO PARA CRIAR E CONTAR CADA PALAVRA
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)

if __name__ == "__main__":
    start("https://portaldobitcoin.uol.com.br/cotacao-bitcoin/")