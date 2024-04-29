my_list = [1, 2, 3, 4, 5]
contador_par, contador_impar = 0, 0

for elemento in my_list:
    if elemento % 2 == 0:
        contador_par += 1
    else:
        contador_impar +=1

print(f'A lista tem {contador_par}   elementos pares')
print(f'A lista tem {contador_impar} elementos impares')