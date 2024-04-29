# Crie um programa que leia/solicite para o usuário inserir quatro notas, realize a média e mostre na tela o resultado.

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

print("A média das notas é: {:.1f} " .format((n1+n2+n3+n4)/4))
