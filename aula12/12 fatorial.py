# 12. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Limitar o cálculo para valores de 1 até 9.
# Exemplos: 
#       6! = 6x5x4x3x2x1 = 720
#       5! = 5x4x3x2x1   = 120
#       4! = 4x3x2x1     = 24

import math
num = int(input("Digite um número de 1 a 9: "))
i = num
c = 1
if num >= 1 and num <= 9:
    txt = num
    while i > 1:
        i -= 1
        txt = str(txt) + "x" + str(i)  
    fat = math.factorial(num)

    print(f"{num}! = {txt} = {fat}")

else:
    print("Valor Inválido.")
    exit

    