# 13. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. 
#     Deverão ser aceitos somente valores entre -100 (menor valor) e 100 (maior valor).

# list = []
# try:
#     while True:
#         list.append(int(input("Digite um número ou se quiser sair, digite uma letra: ")))
# except:
#     print (f"O menor valor é: {min(list)}  \nO maior valor é: {max(list)} \nA soma dos valores é: {sum(list)}")

n = int(input("Digite a quantidade de numeros: "))

maior = 0
menor = 0
soma = 0

c = 0
while c < n:
    num = int(input("Digite um número "))
    
    if num < -100 or num > 100: 
        print("Numero inválido")
        break

    if c == 0:
        maior = num
        menor = num
        
    if num > maior:
        maior = num

    if num < menor:
        menor = num

    soma = soma + num

    c += 1

print(f"maior: {maior} \nmenor: {menor} \nsoma: {soma}")