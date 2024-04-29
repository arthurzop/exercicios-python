# 8. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#    Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro 
#    Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 

# O programa deverá ler o número de litros vendidos, o tipo de combustível codificado da seguinte forma: 
#    A - Álcool, 
#    G - Gasolina, 
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,95 o preço do litro do álcool é R$ 2,89.
# Salvar o código como: desc_combustiveis.py

tipo = input("Tipo de combustível vendido (Álcool ou Gasolina): ")
litro = float(input("Quantidade de litros vendidos: "))

a = "alcool"
g = "gasolina"

if tipo == a:
    if litro <= 20:
        valor = litro * 2.89
        des = (3 * valor) / 100
        total = valor - des
        print("O valor com desconto é: R${:.2f}" .format(total))
    elif litro > 20:
        valor = litro * 2.89
        des = (5 * valor) / 100
        total = valor - des
        print("O valor com desconto é: R${:.2f}" .format(total))

elif tipo == g:
    if litro <= 20:
        valor = litro * 4.95
        des = (4 * valor) / 100
        total = valor - des
        print("O valor com desconto é: R${:.2f}" .format(total))
    elif litro > 20:
        valor = litro * 4.95
        des = (6 * valor) / 100
        total = valor - des
        print("O valor com desconto é: R${:.2f}" .format(total))



    
        

