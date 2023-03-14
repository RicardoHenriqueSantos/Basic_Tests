import itertools

string = input("INSIRA A STRING A SER PERMUTADA: ")
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print("".join(i))
