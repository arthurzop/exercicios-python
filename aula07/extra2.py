#desenvolver um programa que leia um ano no formato xxxx e exiba se o mesmo é bissexto ou não 

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print("{} foi Bissexto" .format(ano))
else:
    print("{} não foi Bissexto" .format(ano))