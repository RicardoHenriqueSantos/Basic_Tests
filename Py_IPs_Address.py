import ipaddress # A BIBLIOTECA FORNECE RECURSOS PARA REALIZAR CÁLCULOS COM O IP

ip = "192.168.0.100"
endereco = ipaddress.ip_address(ip)
print(endereco)
