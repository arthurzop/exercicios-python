# 6. Desenvolva um programa que receba uma string e exiba a mesma na tela. Se o valor digitado for em branco exibir 'Dado inválido'
# Salvar o código como: validar_str.py

string = input("Digite a string: ")

if string.isspace():
    print("Dado Inválido!")

else:
    print(string)