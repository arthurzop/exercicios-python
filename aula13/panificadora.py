# 5. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# Preço do pão: R$ 0.50

# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.50
# 2 - R$ 1.00
# 3 - R$ 1.50
# 4 - R$ 2.00
# ...

# 50 - R$ 25.00


print('Panificadora Pão de Ontem \nTabela de Preços')
c = 0
n = 0
while n < 50:
    c += 0.50
    n += 1
    print(f'{n} - {c:.2f}')