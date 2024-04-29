lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = []

for indice in range(len(lista1)):
    lista3.append(lista1[indice] + lista2[indice])

print(f'lista3 = {lista3}')