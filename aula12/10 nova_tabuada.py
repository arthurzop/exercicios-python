# 10. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
# Ao término da exibição deverá ser perguntado ao usuário de deseja continuar? (s/n)
# Se a resposta for 's' (sim) deverá ser executado o gerador novamente.
# Se a resposta for 'n' (não) encerrar o programa e exibir a seguinte mensagem: 'Até a próxima!!!'
# A saída deve ser conforme o exemplo abaixo:

# Tabuada do número:  5

# 5 X 1 = 5
# 5 X 2 = 10
# ...
# ...
# ...
# 5 X 10 = 50

# Deseja continuar? (s/n) n
# Até a próxima!!!

import os
from time import sleep

while True:
    num = int(input("Digite qual número quer a tabuada: "))

    print("*****************************")
    print("        TABUADA DE {}        " .format(num))
    print("*****************************") 

    a = 1

    while a <= 10:
        print("{} x {} = {}" .format(a, num, (a * num)))
        a += 1

    op = input("Deseja continuar? (s ou n): ").casefold()

    if op == "s":
        os.system("cls")
        sleep(.6)
        continue
    elif op == "n":
        print("Até a Próxima!")
        break
