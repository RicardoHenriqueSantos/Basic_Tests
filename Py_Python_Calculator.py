# CALCULADORA EM PYTHON
print("*************** PYCALC ***************")
print("")


# FUNÇÕES DAS OPERAÇÕES MATEMÁTICAS
def soma(num1, num2):
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
    return resultado


def subtracao(num1, num2):
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
    return resultado


def multiplicacao(num1, num2):
    resultado = num1 * num2
    print(f"{num1} X {num2} = {resultado}")
    return resultado


def divisao(num1, num2):
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
    return resultado


# ATRIBUIÇÃO DA VARIÁVEL DE ESCOLHA DO USUÁRIO
escolha = 0

# LOOP PARA REALIZAÇÃO DE OPERAÇÃO DE ACORDO COM O USUÁRIO
while escolha != 5:

    # MENU DE OPÇÕES
    print("----- OPERAÇÕES ----- ")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - SAIR")

    # ESCOLHA DO USUÁRIO
    escolha = int(input("INSIRA A OPERAÇÃO QUE DESEJA REALIZAR: "))
    print("")

    # CONDICIONAIS PARA OPERAÇÃO ESCOLHIDA PELO USUÁRIO
    if escolha == 1:
        n1 = int(input("INSIRA O 1° NÚMERO: "))
        n2 = int(input("INSIRA O 2° SEGUNDO NÚMERO: "))
        soma(n1, n2)

    elif escolha == 2:
        n1 = int(input("INSIRA O 1° NÚMERO: "))
        n2 = int(input("INSIRA O 2° SEGUNDO NÚMERO: "))
        subtracao(n1, n2)

    elif escolha == 3:
        n1 = int(input("INSIRA O 1° NÚMERO: "))
        n2 = int(input("INSIRA O 2° SEGUNDO NÚMERO: "))
        multiplicacao(n1, n2)

    elif escolha == 4:
        n1 = int(input("INSIRA O 1° NÚMERO: "))
        n2 = int(input("INSIRA O 2° SEGUNDO NÚMERO: "))
        divisao(n1, n2)

    # CONDICIONAL PARA QUE NÃO APAREÇA A MENSAGEM QUANDO SAIR DO SISTEMA
    elif escolha != 5:
        print("OPÇÃO INVÁLIDA!")
