# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
import os
from time import sleep

while True:
    nome = input("Digite seu nome: ")
    if len(nome) <= 3:
        input("Nome Inválido, digite novamente: ")
    break

while True:
    id = int(input("Digite sua Idade: "))
    if id < 0 or id > 150:
        input("Idade Inválida, digite novamente: ")
    break

while True:
    sal = float(input("Digite seu salário: "))
    if sal < 0:
        input("Salário Inválido, digite novamente: ")
    break

while True:
    sex = input("Digite seu sexo (m ou f): ").casefold()
    if sex != "m" or sex != "f":
        input("Opção Inválida, digite novamente: ").casefold()
    break

while True:
    ec = input("Digite seu Estado Civil (s, c, v ou d): ").casefold()
    if ec != "s" or ec != "c" or ec !="v" or "d":
        input("Estado Civil Inválido, digite novamente: ").casefold()
    break

print("Validado!")
sleep(1.5)
os.system("slc")

