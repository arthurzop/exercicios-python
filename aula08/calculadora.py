# 8. Desenvolva um calculadora que receba dois números e efetue uma das seguintes operações aritméticas:

#    1 - Adição
#    2 - Subtração
#    3 - Multiplicação
#    4 - Divisão
#    5 - Potência
#    6 - Raiz quadrada
#    7 - Número par
#    8 - Número ímpar
import math
num1 = float(input("Digite um número: "))

print("Digite um número para selecionar a operação aritimética:\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação \n 4 - Divisão\n 5 - Potencia\n 6 - Raiz Quadrada\n 7 - Se é número par\n 8 - Se é número ímpar.")

op = int(input("Digite a Opção: "))


if op == 1:
    num2 = float(input("Digite um segundo número: "))
    print("A soma é: {}" .format(num1 + num2))

elif op == 2:
    num2 = float(input("Digite um segundo número: "))
    print("A diferença é {}" .format(num1 - num2))

elif op == 3:
    num2 = float(input("Digite um segundo número: "))
    print("O Produto é: {}" .format(num1 * num2))
    
elif op == 4:
    num2 = float(input("Digite um segundo número: "))
    print("O Quociente é: {}" .format(num1 / num2))

elif op == 5:
    num2 = float(input("Digite um segundo número: "))
    print("O resultado da potenciação é {}" .format(math.pow(num1, num2)))

elif op == 6:
    print("A raiz quadrada é: {}" .format(math.sqrt(num1)))

elif op == 7 and 8:
    sqrt = num1 % 2
    if sqrt == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

else:
    print("Opção Inválida!")
    exit

