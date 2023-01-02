from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

# COMANDOS INICIAIS
root = tk.Tk()
root.withdraw()


# FUNÇÃO PARA RECEBER OS PARÂMETROS
def informacoes(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result


# INSERINDO A URL
link_video = informacoes("Video Link", "INSIRA A URL: ")
yt = YouTube(link_video)

# INFORMAÇÕES SOBRE O VÍDEO
print(f"CANAL: {yt.author}")
print(f"TÍTULO DO VÍDEO: {yt.title}")
print(f"VIEWS: {yt.views}")

# DEFININDO A RESOLUÇÃO
vd = yt.streams.get_highest_resolution()

# INFORMANDO O CAMINHO ONDE SER SALVO O ARQUIVO
caminho = r"C:\Users\KAL-EL\Videos"
vd.download(caminho)

# MENSAGEM DE CONCLUSÃO DO PROCESSO E ONDE ESTÁ SALVO O VÍDEO
messagebox.showinfo("Mensagem", f"CONCLUÍDO! SALVO EM {caminho}")
