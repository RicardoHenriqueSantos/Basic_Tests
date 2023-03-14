import webbrowser       # BIBLIOTECA DE INTERFACE DE ALTO NÍVEL PARA PERMITIR A EXIBIÇÃO DE DOCUMENTOS WEB AOS USUÁRIOS
from tkinter import *   # BIBLIOTECA DE INTERFACE PADRÃO DO PYTHON PARA O KIT DE FERRAMENTAS GRÁFICAS TK

# REPRESENTAÇÃO DA TELA
root = Tk( )
# DEFINIÇÃO DO TÍTULO
root.title("Open Browser")
# TAMANHO DA TELA
root.geometry("260x80")

# FUNÇÃO PARA ABRIR BROWSER
def google():
    webbrowser.open("www.google.com")

# DEFINE O BOTÃO, FUNÇÃO E POSIÇÃO
Button(root, text="Abrir Google", command=google).pack(pady=20)

# EXECUTA A INTERFACE
root.mainloop()