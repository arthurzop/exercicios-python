# 17. Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
# Após todos os alunos (cinco alunos) terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A

# Após concluir a primeira parte você deverá incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
import os
from time import sleep

al = 0
while al <= 5:
    c = 0
    nota = 0
    soma = 0
    while c < 5:
        al += 1
        print(f'\naluno {al}')
        n1 = input('Resposta questão 1: ').capitalize()
        if n1 == 'A':
            nota += 1
        n2 = input('Resposta questão 2: ').capitalize()
        if n2 == 'B':
            nota += 1
        n3 = input('Resposta questão 3: ').capitalize()
        if n3 == 'C':
            nota += 1
        n4 = input('Resposta questão 4: ').capitalize()
        if n4 == 'D':
            nota += 1
        n5 = input('Resposta questão 5: ').capitalize()
        if n5 == 'E':
            nota += 1
        n6 = input('Resposta questão 6: ').capitalize()
        if n6 == 'E':
            nota += 1
        n7 = input('Resposta questão 7: ').capitalize()
        if n7 == 'D':
            nota += 1
        n8 = input('Resposta questão 8: ').capitalize()
        if n8 == 'C':
            nota += 1
        n9 = input('Resposta questão 9: ').capitalize()
        if n9 == 'B':
            nota += 1
        n10 = input('Resposta questão 10: ').capitalize()
        if n10 == 'A':
            nota += 1
        c += 1
        soma += nota
        sleep(.5)
        os.system('cls')
    print(f'\n')
    
        
    
    