# 12. Desenvolva um programa para escrever a contagem regressiva do lançamento de um foguete. 
# O programa deve imprimir 10, 9, 8, …, 1, 0 e 'Ignição!' na tela.
# Salvar o código como: lancamento.py

a = 10

while a > -1:
    print("{}..." .format(a))
    a = a - 1

print("Ignição!")