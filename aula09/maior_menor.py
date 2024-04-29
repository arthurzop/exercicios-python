# 2. Desenvolva um programa que leia três números e que imprima:
#    2.1. o maior,
#    2.2. o menor,
#    2.3. a soma,
#    2.4. a média.
# Exemplo:
# num1 = 5	num2 = 3	num3 = 10
# **********
# maior = 10
# menor = 3
# soma = 18
# media = 6
# Salvar o código como: maior_menor.py

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

soma = a + b + c
media = (a + b + c) / 4

if a > b and b > c:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(a, c, soma, media))

elif b > a and a > c:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(b, c, soma, media))

elif c > a and c > b:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(c, b, soma, media))

elif c > a and b > a:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(c, a, soma, media))

elif a > b and c > b:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(a, b, soma, media))

elif b > a and c > a:
    print("Maior: {} \nMenor: {} \nSoma: {} \nMédia: {}" .format(b, a, soma, media))

