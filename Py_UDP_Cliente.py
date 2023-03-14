import  socket

# CRIANDO O OBJETO DE CONEXÃO
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# MENSAGEM DE ÊXITO NA CRIAÇÃO
print("CLIENTE SOCKET CRIADO COM SUCESSO!")

# VARIÁVEIS PARA ENVIAR DADOS
host = "localhost"
porta = 5433
mensagem = "HAIL SERVER!"

try:
    # EMPACTOCA A MENSAGEM ENVIADA
    s.sendto(mensagem.encode(), (host, 5432))

    # RECEBE DO SERVIDOR UMA RESPOSTA
    dados, servidor = s.recvfrom(4096)
    # DESEMPACOTA OS DADOS
    dados = dados.decode()
    print(f"CLIENTE: {dados}")

finally:
    print("CLIENTE: FECHANDO A CONEXÃO")
    # FECHA A CONEXÃO PARA QUE NÃO FIQUE EM LOOP
    s.close()