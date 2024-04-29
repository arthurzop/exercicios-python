# 8. Faça um programa que receba dois números inteiros, gere e exiba os números que estão no intervalo compreendido por eles.
#     Exemplo:
#     num1 = int(input('Digite o número 1: '))  #foi digitado 1
#     num2 = int(input('Digite o número 2: '))  #foi digitado 10
#     Portanto o intervalo compreendido é: 1 a 10.
#     1
#     2
#     3
#     4
#     5
#     6
#     7
#     8
#     9
#     10

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

while a <= b:
    print(a)
    a += 1

while b <= a:
    print(b)
    b += 1