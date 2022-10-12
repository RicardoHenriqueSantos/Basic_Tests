import pyautogui
import pyperclip
import time
import pandas as pd

# SALVE O ARQUIVO "RELATÓRIO VENDAS DEZ" COMO BASE DE DADOS NO DRIVE DE SUA ESCOLHA

# PASSO 1 - ENTRAR NO SISTEMA

# UM DELAY PARA QUE TODAS AS AÇÕES SEJAM EXECUTADAS
pyautogui.PAUSE = 1

# PROCESSO PARA ABRIR O NAVEGADOR
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# O PYPERCLIP É MAIS RECOMENDÁVEL POIS COPIA O LINK COM CARACTERES ESPECIAIS
time.sleep(1)
pyperclip.copy("")

# COLA O LINK ACIMA E EXECUTA COM ENTER
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press("enter")

# UMA PAUSA PARA TODAS AS TAREFAS SEREM EXECUTADAS E CONTINUAR O PROCESSO
time.sleep(6)

# PASSO 2 - NAVEGAR E ENCONTRAR BASE DE DADOS
pyautogui.click(x=390, y=306, clicks=2)  # SELECIONA A PASTA
time.sleep(1)
pyautogui.click(x=390, y=306)  # SELECIONA O ARQUIVO
time.sleep(1)
pyautogui.click(x=1159, y=195)  # SELECIONA A TAREFA
time.sleep(1)

# PASSO 3 - DOWNLOAD BASE DE DADOS

pyautogui.click(x=1025, y=561)  # SOLICITA O DOWNLOAD
time.sleep(7)

# PASSO 4 - CALCULAR OS INDICADORES
tabela = pd.read_excel(r"")
print(tabela.head())

quantidade = tabela['Quantidade'].sum()  # QUANTIDADE DE PRODUTOS VENDIDOS
faturamento = tabela['Valor Final'].sum()  # SOMA DO VALOR FINAL
print(quantidade)
print(faturamento)

# PASSO 5 - ENTRAR NO EMAIL
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(7)

# PASSO 6 - ENVIAR O RELATÓRIO
pyautogui.click(x=76, y=200)  # CLICAR EM ESCREVER NO GMAIL

pyautogui.write("")  # COLAR O EMAIL DO DESTINATÁRIO
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(1)

pyperclip.copy("Relatório de Vendas")  # INSERE O ASSUNTO
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(1)

texto = f"""
Olá Sr. Ricardo!

A quantidade de itens vendidos foi de {quantidade:,}.
O faturamento foi de R$ {faturamento:,.2f}.

Abraços 
Clark Joseph Kent
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

pyautogui.click(x=836, y=636)
time.sleep(4)
pyautogui.click(x=322, y=615)
