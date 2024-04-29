import random
c = 0
lista = []
while c <= 500:
    lista.append(random.randrange(1, 5000))
    c += 1
lista.sort()
print(lista)
    
