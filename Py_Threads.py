# CRIAREMOS UMA FUNÇÃO PARA O ESTUDO DE MULTI PROCESSOS COM O EXEMPLO DE UMA CORRIDA DE CARROS
import time
from threading import Thread # IMPORTA A BIBLIOTECA PARA QUE OS PROCESSOS OCORRAM SIMULTANEAMENTE
def carro (velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f"\nPILOTO: {piloto} | KM: {trajeto}")


thread_carro1 = Thread(target=carro, args=[1, "Michael S."])
thread_carro2 = Thread(target=carro, args=[2, "Ayrton S."])

thread_carro1.start()
thread_carro2.start()