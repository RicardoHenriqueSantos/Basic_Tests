import  socket # IMPORTA A BIBLIOTECA PARA RELACIONAMENTO DA PLACA DE REDE COM O SISTEMA OPERACIONAL

# CRIANDO O OBJETO DE CONEXÃO
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# MENSAGEM DE ÊXITO NA CRIAÇÃO
print("SOCKET CRIADO COM SUCESSO!")

# VARIÁVEIS PARA ARMAZENAR OS DADOS DA CONEXÃO
host = "localhost"
porta = 5432

# REALIZA A CONEXÃO COM AS INFORMAÇÕES INFORMADAS
s.bind((host, porta))

mensagem = "\nSERVIDOR: HAIL CLIENTE!"

# SE BIND RETORNAR VERDADEIRO
while 1:
    dados, endereco = s.recvfrom(4096)
    if dados:
        print("SERVIDOR ENVIANDO MENSAGEM...")
        s.sendto(dados + (mensagem.encode()), endereco)