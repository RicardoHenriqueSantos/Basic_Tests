import socket   # RELACIONAMENTO DA PLACA DE REDE COM O SISTEMA OPERACIONAL
import sys      # FORNECE ALGUMAS VARIÁVEIS E ALGUMAS FUNÇÕES EM CONJUNTO COM O PYTHON

# FUNÇÃO PARA TESTAR UMA CONEXÃO TCP
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("A CONEXÃO FALHOU!")
        print(f"ERRO: {error}")
        sys.exit()

    print("SOCKET CRIADO COM SUCESSO")

    HostAlvo = input("INSIRA O HOST OU IP A SER CONECTADO: ")
    PortaAlvo = input("INSIRA A PORTA A SER CONECTADA: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"CLIENTE TCP CONECTADO COM SUCESSO NOS HOST {HostAlvo} E PORTA {PortaAlvo}!")
        s.shutdown(2)
    except socket.error as error:
        print("A CONEXÃO FALHOU!")
        print(f"ERRO: {error}")
        sys.exit()

# SE O NOME DA FUNÇÃO FOR MAIN, CHAME MAIN
if __name__ == "__main__":
    main()

