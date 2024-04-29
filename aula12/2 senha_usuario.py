# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem:
#     'Senha e Usuário iguais'
# e voltando a pedir as informações.

while True:
    u = input("Digite o usuario: ")
    s = input("Digite a senha: ")
    
    if u == s:
        print("Senha e Usuario iguais")
    elif u != s:
        break