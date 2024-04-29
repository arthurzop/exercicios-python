# 2. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quant = int(input('digite a quantidade de turmas: '))
c = 0
a = 0
soma = 0
while c < quant:
    alunos = int(input('digite a quantidade de alunos na turma: '))
    if alunos > 0 and alunos <= 40:
        a += 1
        soma += alunos

    else:
        print('valor inválido.')
    c += 1

print(f'média: {soma/quant:.2f}')
