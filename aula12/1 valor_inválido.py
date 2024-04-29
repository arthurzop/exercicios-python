# 1. Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Salvar o código como: valor_invalido.py

while True:
    n = float(input("Digite uma nota: "))
    
    if n >= 0 and n <= 10:
        print("Nota Válida! \nFim do programa.")
        break
    elif n < 0 or n > 10:
        print("Valor invalido!")

