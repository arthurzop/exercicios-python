# 4. Suponha que o professor Atila possua dois logins na rede do SENAI-SP. 
# Construa um programa que valide o acesso do professor à rede. 
# Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”.
# Caso contrário, “Usuário e senha não conferem”.
# Dados dos dois logins:
# login 1			login 2
# usuário: atila		usuário: olivi
# senha: 12345		senha: 54321
# Salvar o código como: dois_logins.py

l = input("Login: ")
s = input("Senha: ")

usuario1 = "atila"
senha1 = "12345"

usuario2 = "olivi"
senha2 = "54321"

if l == usuario1:
    if s == senha1:
        print("Bem-vindo!")
    else:
        print("Senha Inválida!")

elif l == usuario2:
    if s == senha2:
        print("Bem-Vindo!")
    else:
        print("Senha Inválida!")

else:
    print("Login ou Senha invalidos!")