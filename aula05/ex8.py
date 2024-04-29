# Crie um programa que leia/solicite para o usuário inserir, separadamente, o nome de uma rua, bairro, cidade e o número da casa. No final, o programa deve mostrar o endereço completo em apenas um print.

rua = input("Digite o nome da rua: ")
num = input("Digite o número da casa: ")
bairro = input("Digite o bairro: ")
cidade = input("Digite a cidade: ")


print("Rua {}\nCasa n°{}, {}\n{}" .format(rua, num, bairro, cidade))