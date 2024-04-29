#Crie um programa que leia um número e mostre na tela seu dobro, triplo e raiz quadrada.

import math
num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

print("O dobro é = {}\no triplo é = {}\na raiz quadrada é = {}" .format(dobro, triplo, raiz))

#print("O dobro é = {}, o triplo é = {} e a raiz quadrada é = {}" .format(num * 2, num * 3, num ** .5))