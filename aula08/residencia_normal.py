# Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3
# residencia_normal.py

consumo = float(input("Digite a quantidade de Litros gastos (L\m³): "))

if consumo <= 10:
    print("O valor a ser pago é R$22,30")

elif consumo <= 20:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 3.50))

elif consumo <= 50:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 8.75))

else:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 9.64))
