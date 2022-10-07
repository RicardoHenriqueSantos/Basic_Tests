# IMPORTANDO O CONECTOR DO MYSQL
import mysql.connector

# ADICIONANDO OS PARÂMETROS
cnx = mysql.connector.connect(
            host='',
            database='',
            user='',
            password='')

# VERIFICANDO A CONEXÃO
if cnx.is_connected():
    info = cnx.get_server_info()
    print(f"Conectado ao servidor MySQL versão {info}")

cnx.commit()
cnx.close()
