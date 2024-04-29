# 7. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

quant = int(input('digite a quantidade de temperaturas: '))
lista = []
for i in range(quant):
    temp = float(input('digite a temperatura: '))
    lista.append(temp)

print(f'menor temp: {min(lista)}°C \nmaior temperatura: {max(lista)}°C \nmedia: {sum(lista)/quant:.1f}')