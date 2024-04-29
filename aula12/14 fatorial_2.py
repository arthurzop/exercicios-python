# 14. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes.
import os
from time import sleep
import math

while True:
    num = int(input("Digite um número de 1 a 9: "))
    i = num
    c = 1
    if num >= 1 and num <= 9:
        fat = math.factorial(num)

        print(f"{num}! = {fat}")
        
        op = input("Deseja continuar? s/n: ").casefold()
    if op == "s":
        os.system("cls")
        sleep(.6)
        continue
    elif op == "n":
        print("fim do programa.")
        break
    else:
        print("Valor Inválido.")
        exit

    