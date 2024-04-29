# 5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: imc = peso / altura * altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 16:
    print("Magreza Grave")

elif imc < 17:
    print("Magreza Moderada")

elif imc < 18.5:
    print("Magreza Leve")

elif imc < 25:
    print("Saudável")

elif imc < 30:
    print("Sobrepeso")

elif imc < 35:
    print("Obesidade Grau I")

elif imc < 40:
    print("Obesidade Grau II (Severa)")

else:
    print("Obesidade grau III (Mórbida)")