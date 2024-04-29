# 10 - Desenvolva um programa que pergunte em que turno você estuda. 
# Peça para digitar: M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Obs.: Somente letras maiúsculas para M, V ou N.
print("Qual turno você estuda? \nM - Manhã \nT - Tarde \nN - Noite")
turno = input("Digite a opção: ").upper()

if turno == "M":
    print("Bom dia!")

elif turno == "T":
    print("Boa tarde!")

elif turno == "N":
    print("Boa noite!")

else:
    print("Valor Inválido!")