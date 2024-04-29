# 11 - Desenvolva um programa que recebe o salário de um funcionário e determine o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 1000,00 (incluindo)     : aumento de 20%
#   salários até R$ 1.700,00                : aumento de 15%
#   salários até R$ 2.300,00                : aumento de 10%
#   salários acima de R$ 2.300,00 em diante : aumento de 5%

# Após o processamento exibir na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

salario = float(input("Digite seu salário: "))

if salario < 1000.00:
    perc = 20
    valor = (20 * salario / 100)
    novo = salario + valor 

elif salario < 1700.00:
    perc = 15
    valor = (15 * salario / 100)
    novo = salario + valor 

elif salario < 2300.00:
    perc = 10
    valor = (10 * salario / 100)
    novo = salario + valor 

else:
    perc = 5
    valor = (5 * salario / 100)
    novo = salario + valor 

print("O salário original: {} \nPercentual de Aumento: {} \nValor do Aumento: {} \nNovo salário: {}" .format(salario, perc, valor, novo))
