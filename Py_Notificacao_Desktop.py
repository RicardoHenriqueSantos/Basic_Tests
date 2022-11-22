from win10toast import ToastNotifier
import time

# INICIALIZAÇÃO
toaster = ToastNotifier()

# REALIZAREMOS UMA CONTAGEM E QUANDO FOR ENCERRADA RECEBERÁ UMA NOTIFICAÇÃO
cont = 0
for cont in range(cont, 11):
    print(cont)
    time.sleep(1)

# PARÂMETROS
toaster.show_toast(
    "Notificação",
    "Processo encerrado",
    threaded=True,
    icon_path=None,
    duration=3  # SEGUNDOS
)
