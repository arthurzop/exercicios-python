# Crie um programa que leia um número inteiro e 
# exiba na tela seu antecessor e seu sucessor

num = int(input("Digite um número: "))
antecessor = num - 1
sucessor = num + 1
# print(antecessor, "e", sucessor)
print("Sucessor = {}, Antecessor = {}" .format(sucessor, antecessor))