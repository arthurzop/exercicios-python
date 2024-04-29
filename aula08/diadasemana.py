# 4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'

num = int(input("Digite um número de 1 a 7: "))

if num == 1:
    print("Domingo")

elif num == 2:
    print("Segunda")

elif num == 3:
    print("Terça")

elif num == 4:
    print("Quarta")

elif num == 5:
    print("Quinta")

elif num == 6:
    print("Sexta")

elif num == 7:
    print("Sábado")

else:
    print("Opção Inválida!")
