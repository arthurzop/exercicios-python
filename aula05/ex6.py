# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input("Valor em metros: "))
print("O valor em centímetros é = {:.2f}cm \nO valor em milímetros é = {:.2f}mm" .format(metro * 100, metro * 1000))
