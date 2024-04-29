# 10. Desenvolver um programa que calcule e exiba a tabuada de hum a dez de um número qualquer.
#     Exemplo:
#     ******************************
#     Informe o número da tabuada: 5
#     ******************************
#     1 x 5 = 5
#     2 x 5 = 10
#     3 x 5 = 15
#     4 x 5 = 20
#     5 x 5 = 25
#     6 x 5 = 30
#     7 x 5 = 35
#     8 x 5 = 40
#     9 x 5 = 45
#     10 x 5 = 50

# Salvar o código como: tabuada.py

 
num = int(input("Digite qual número quer a tabuada: "))

print("*****************************")
print("        TABUADA DE {}        " .format(num))
print("*****************************") 

a = 1

while a <= 10:
    print("{} x {} = {}" .format(a, num, (a * num)))
    a += 1

