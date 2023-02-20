import os     # IMPORTA BIBLIOTECA QUE INTEGRA OS RECURSOS E PROGRAMAS DO SO
import time   # IMPORTA BIBLIOTECA QUE INTEGRA FUNÇÕES RELACIONADAS À TEMPO

# ABRE O ARQUIVO SELECIONADO
with open("Py_Hosts.txt") as file:
    dump = file.read()                  # A VARIÁVEL RECEBE AS INFORMAÇÕES DO ARQUIVO
    dump = dump.splitlines()            # AS INFORMAÇÕES AGORA SÃO SEPARADAS LINHA POR LINHA

    # UM LOOP PARA PERCORRER E IMPRIMIR TODAS AS INFORMAÇÕES DA VARIÁVEL
    for ip in dump:
        print("-" * 60)                 # FORMATAÇÃO SIMPLES
        print("VERIFICANDO...")         # FORMATAÇÃO SIMPLES
        os.system(f"ping -n 4 {ip}")    # EXECUTANDO UM COMANDO DA BIBLIOTECA OS | PING -N <NÚMERO DE PACOTES> <IP>
        time.sleep(2)                   # HÁ UM TEMPO DE ESPERA DE 2 SEGUNDOS