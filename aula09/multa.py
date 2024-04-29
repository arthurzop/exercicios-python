# 1. Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00
# Salvar o código como: multa.py

vel = int(input("Digite a velocidade do carro (km/h): "))

if vel > 80:
    multa = (vel - 80) * 50.00
    print("O valor da multa é R${}" .format(multa))

elif vel <= 80:
    print("Você não foi multado.")


