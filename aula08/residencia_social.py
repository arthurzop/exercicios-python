# 1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 7,59
# Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
# Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
# Se o consumo for acima dos 50m3, então R$ 7,31 por m3
# residencia_social.py

consumo = float(input("Digite a quantidade de Litros gastos (L\m³): "))

if consumo <= 10:
    print("O valor a ser pago é R$ 7,59")

elif consumo <= 20:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 1.31))

elif consumo <= 30:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 4.64))

elif consumo <= 50:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 6.62))

else:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 7.31))