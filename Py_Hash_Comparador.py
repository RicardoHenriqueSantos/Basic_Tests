import hashlib   # IMPORTANDO A BIBLIOTECA PARA IMPLEMENTAR UMA INTERFACE COMUM PARA MUITOS ALGORITMOS DE HASH

# CRIANDO VARIÁVEIS PARA UTILIZAÇÃO DOS ARQUIVOS CRIADOS
arquivo1 = "teste_hash_comparador.txt"
arquivo2 = "teste_hash_comparador_2.txt"

# AS HASHES SÃO CRIADAS
hash1 = hashlib.new("ripemd160")
hash1.update(open(arquivo1, "rb").read())
hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

# COMPARANDO AS HASHS
if hash1.digest() != hash2.digest():
    # DIGEST RESUME OS DADOS PASSADOS PELO UPDATE
    # HEXDIGEST RESUME OS DADOS PARA HEXIDECIMAL
    print(f"O ARQUIVO: {arquivo1} É DIFERENTE DO ARQUIVO: {arquivo2}")
    print(f"HASH ARQUIVO 1: {hash1.hexdigest()}")
    print(f"HASH ARQUIVO 2: {hash2.hexdigest()}")
else:
    print(f"O ARQUIVO: {arquivo1} É IGUAL O ARQUIVO: {arquivo2}")
    print(f"HASH ARQUIVO 1: {hash1.hexdigest()}")
    print(f"HASH ARQUIVO 2: {hash2.hexdigest()}")