# 7. Desenvolva um programa que exiba na tela um menu de opções:

#    1 - Opção 1
#    2 - Opção 2
#    3 - Opção 3
#    4 - Sair
#    Digite uma opção: 
# Se o usuário digitar 1, exibir na tela: 'Você selecionou a opção 1'
# Se o usuário digitar 2, exibir na tela: 'Você selecionou a opção 2'
# Se o usuário digitar 3, exibir na tela: 'Você selecionou a opção 3'
# Se o usuário digitar 4, exibir na tela: 'Você selecionou sair'
# Se o usuário digitar uma opção diferente das apresentadas no menu, exibir 'Opção inválida!!!'
# Exibir no final do processamento 'Fim do programa!'

print("Digite um número para selecionar a opção:\n 1 - Opção 1\n 2 - Opção 2\n 3 - Opção 3\n 4 - Sair")
op = int(input("Digite a Opção: "))

if op == 1:
    print("Você selecionou a opção 1.")

elif op == 2:
    print("Você selecionou a opção 2.")

elif op == 3:
    print("Você selecionou a opção 3.")

elif op == 4:
    print("Você selecionou Sair.")

else:
    print("Opção Inválida!!!")

print("Fim do Programa!")