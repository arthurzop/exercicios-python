# 11. Faça um programa que pergunte ao usuário quantos números interos deseja solicitar e exiba:
#     14.1. a quantidade de números pares e;
#     14.2. a quantidade de números impares.

# Ao término da exibição deverá ser perguntado ao usuário de deseja continuar? (S/N)
# Se 'S' (Sim) deverá ser executado o programa novamente.
# Se 'N' (Não) encerrar o programa e exibir a seguinte mensagem: 'Valew!!!'
import os
from time import sleep

while True:
    quant = int(input("quantos números interos deseja solicitar? "))

    cp = 0
    ci = 0

    for quant in range(0, quant):
        if quant % 2 == 0:
            cp += 1

        if quant % 2 == 1:
            ci += 1

    print(f"Quantidade de pares: {cp} e Quantidade de impares: {ci}")

    op = input("Deseja continuar? s/n: ").casefold()
    if op == "s":
        os.system("cls")
        sleep(.6)
        continue
    elif op == "n":
        print("valeu")
        break

