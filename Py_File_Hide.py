import ctypes

# DEFINIR ATRIBUTO DO ARQUIVO - HEXADECIMAL
atributo_ocultar = 0x02

# DLL QUE PERMITE O AQUIVO SER MANIPULADO - IRÁ RETORNAR TRUE OU FALSE
retorno = ctypes.windll.kernel32.SetFileAttributesW("file_hide_test.txt", atributo_ocultar)

# VERIFICAR SE O ARQUIVO FOI OCULTADO
if retorno:
    print("ARQUIVO OCULTADO!")
else:
    print("O ARQUIVO NÃO FOI OCULTADO!")