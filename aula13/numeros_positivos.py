# 16. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
while True:

    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    
    while True:
        num = int(input('digite um numero: '))
        if num >= 0 and num <= 25:
            c1 += 1
            continue
        elif num >= 26 and num <= 50:
            c2 += 1
            continue
        elif num >= 51 and num <= 75:
            c3 += 1
            continue
        elif num >= 76 and num <= 100:
            c4 += 1
        
        if num < 0:
            break
    break

print(f'tem {c1} no intervalo: [00-25] \ntem {c2} no intervalo: [26-50] \ntem {c3} no intervalo: [51-75] \ntem {c4} no intervalo: [76-100]')
    


    