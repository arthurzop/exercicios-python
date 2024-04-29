# 18. Faça um programa que calcule o mostre a média aritmética de N notas. Deverá ser limitado de 1 a 6 notas.
while True:
    quant = int(input("quantas notas deseja calcular? (de 2 a 6): "))
    if quant >= 2 and quant <= 6:
        c = 0
        nota = 0
        soma = 0
        while c < quant:
            nota = float(input("nota: "))
            if nota >= 0 and nota <= 10:
                c += 1
                soma += nota 
            else:
                print("Invalido.")
            
        print("A media é: {:.2f}" .format(soma/quant))
        break
    else:
        print("Quantidade inválida.")

    