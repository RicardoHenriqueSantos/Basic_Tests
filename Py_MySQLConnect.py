import mysql.connector

cnx = mysql.connector.connect(
            host='',
            database='',
            user='',
            password='')

if cnx.is_connected():
    info = cnx.get_server_info()
    print(f"Conectado ao servidor MySQL versão {info}")

cnx.commit()
cnx.close()
