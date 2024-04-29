# 8. Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num=int(input("Digite um numero: "))

for a in range(2, num + 1):
    if num % a==0:
        print("Não é primo")
        break
else:
    print("É primo")