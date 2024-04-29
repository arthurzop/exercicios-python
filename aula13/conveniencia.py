# 6. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas ACME

# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 1.00

# Total    : R$ 9.00
# Dinheiro : R$ 20.00
# Troco    : R$ 11.00

import os
from time import sleep

c = 0
n = 0
total = 0
print('Digite o valor do produto abaixo: \nPara informar o fim da compra digite 0 \n')
while True:
    
    valor = float(input('Valor: '))
    n += 1
    total += valor
    if valor != 0:
        print(f'Produto {n}: R${valor:.2f}\n')

    if valor == 0:
        print(f'Total: R${total:.2f}')
        dinheiro = float(input('Qual o valor em dinheiro fornecido? '))
        troco = dinheiro - total
        print(f'\nTotal: R${total:.2f} \nDinheiro: R${dinheiro:.2f} \nTroco: R${troco:.2f}')
        sleep(5.5)
        os.system('cls')
        continue
    

