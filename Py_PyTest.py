# pip install pytest

# TESTE PARA ANALISAR SE UM NÚMERO É ÍMPAR OU NÃO
def impar(num):
    if num % 2 == 0:
        return False
    else:
        return True

# REALIZAREMOS O TESTE
def test():
    assert impar(1) == True
    assert impar(2) == False
    assert impar(3) == True
    assert impar(4) == False
    assert impar(5) == True