cont = 1
soma = 0
c1 = 0
c2 = 0
maior = 0
menor = 0
while cont <= 5:
    num = int(input('digite um numero: '))
    if cont == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        maior = num

    if num % 2 == 0:
        c1 += 1

    else:
        c2 += 1

    soma += num
    cont += 1

print(f'maior: {maior} \nmenor: {menor} \nsoma: {soma} \nmédia: {(soma/cont):.2f} \npares: {c1} \nimpares: {c2}')