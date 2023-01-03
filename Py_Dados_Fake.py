from faker import Faker

fake = Faker()

nome = fake.name()
primeiro_nome = fake.first_name_male()
usuario = fake.user_name()
senha = fake.password()

print(f"Nome: {nome}")
print(f"Primeiro Nome: {primeiro_nome}")
print(f"Usuário: {usuario}")
print(f"Senha: {senha}")
