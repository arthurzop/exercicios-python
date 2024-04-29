# 3. Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,45 para viagens mais longas.
# Salvar o código como: viagens.py

dis = float(input("Digite a distancia que pretende percorrer (km): "))

if dis <= 200:
    valor = dis * 0.50
    print("A passagem ficou R${:.2f}" .format(valor))

else:
    valor = dis * 0.45
    print("A passagem ficou R${:.2f}" .format(valor))