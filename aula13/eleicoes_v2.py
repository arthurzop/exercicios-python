# 1. Numa eleição existem três candidatos (candA, candB e candC). Faça um programa que:
#    _peça o número total de eleitores;
#    _peça para cada eleitor votar.
# Ao final mostrar o número de votos de cada candidato.
# Salvar o código como: eleicoes_v2.py

import os
quant = int(input("Quantidade de eleitores que votarão: "))
c1 = 0
c2 = 0 
c3 = 0
e = 0
while e < quant:
    voto = input("Digite para votar: \nCandidato A - a \nCandidato B - b \nCandidato C - c \nVoto: ").casefold()
    
    if voto == "a":
        c1 += 1
    elif voto == "b":
        c2 += 1
    elif voto == "c":
        c3 += 1
    else:
        print("inválido")
    
    e += 1
    os.system("cls")

print(f"=== Resultados: === \nVotos no candidato A: {c1} \nVotos no candidato B: {c2} \nVotos no candidato C: {c3}")