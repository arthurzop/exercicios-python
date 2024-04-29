# 3. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quant = int(input('digite a quantidade de cds: '))
c = 0
valor = 0
while c < quant:
    valor += float(input('digite o valor do cd: '))
    c += 1

print(f'valor total gasto: {valor} \nmedia do valor gasto: {valor/quant:.2f}')
    