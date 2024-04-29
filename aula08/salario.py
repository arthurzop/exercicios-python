# Desenvolva um programa que leia o valor (R$) de um salário qualquer e calcule e exiba o desconto com IRRF e INSS;

salario = float(input("Digite seu salário: "))

if salario <= 1903.98:
    sIR = salario

elif salario == 1903.99 or salario <= 2826.65:
    sIR = (7.5 * salario / 100)
    
elif salario == 2826.66 or salario <= 3751.05:
    sIR = (15 * salario / 100)

elif salario == 3751.06 or salario <= 4664.68:
    sIR = (22.5 * salario / 100)

else: 
    sIR = (27.5 * salario / 100)

if salario <= 1302.00:
    inss = (7.5 * salario / 100)

elif salario == 1302.02 or salario <= 2571.29:
    inss = (9 * salario / 100)

elif salario == 2571.30 or salario <= 3856.94:
    inss = (12 * salario / 100)
else:
    inss = (14 * salario / 100)

sf = salario - inss - sIR

print("Salario bruto: {} \nDesconto Imposto de renda: {} \nDesconto INSS: {} \nSalario descontado: {}" .format(salario, sIR, inss, sf))