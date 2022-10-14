
salario = float(input("Insira o seu salário: "))

# SE PAGAR
se_pagar = (salario * 5) / 100
print(f"01 - SE PAGAR: R$ {se_pagar:.2f}")

# DOAR
doar = (salario * 10) / 100
print(f"02 - DOAR: R$ {doar:.2f}")

# PAGAR AS CONTAS
pagar_contas = (salario * 60) / 100
print(f"03 - PAGAR CONTAS: R$ {pagar_contas:.2f}")

# INVESTIR
investir = (salario * 10) / 100
print(f"04 - INVESTIR: R$ {investir:.2f}")

# POUPAR PARA SONHOS
poupar = (salario * 10) / 100
print(f"05 - POUPAR: R$ {poupar:.2f}")

# RASGAR
rasgar = (salario * 5) / 100
print(f"06 - RASGAR: R$ {rasgar:.2f}")

print("")

contas = float(input("INSIRA O VALOR DAS SUAS CONTAS: "))

print("")

if contas < pagar_contas:
    porcentagem = (contas / pagar_contas) * 100
    print(f"SUAS DÍVIDAS EQUIVALEM A {porcentagem:.1f}% DO SEU SALÁRIO")
else:
    porcentagem = ((contas - pagar_contas) / pagar_contas) * 100
    print(f"SUAS DÍVIDAS ULTRAPASSAM {porcentagem:.1f}% DO SEU SALÁRIO")
