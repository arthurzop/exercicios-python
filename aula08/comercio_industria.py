# 3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3
# comercio_industria.py

consumo = float(input("Digite a quantidade de Litros gastos (L\m³): "))

if consumo <= 10:
    print("O valor a ser pago é R$44,95")

elif consumo <= 20:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 8.75))

elif consumo <= 50:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 16.76))

else:
    print("o valor a ser pago é: R${:.2f}" .format(consumo * 17.46))