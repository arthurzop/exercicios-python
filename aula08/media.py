# 12. Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"

n1 = float(input("Digite a nota do primeiro bimestre: "))
n2 = float(input("Digite a nota do segundo bimestre: "))
n3 = float(input("Digite a nota do terceiro bimestre: "))
n4 = float(input("Digite a nota do quarto bimestre: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 9.0 and media <= 10.0:
    conceito = "A"

elif media >= 7.5 and media <= 8.9:
    conceito = "B"

elif media >= 6.0 and media <= 7.4:
    conceito = "C"

elif media >= 4.0 and media <= 5.9:
    conceito = "D"

else:
    conceito = "E"

if conceito == "A" and "B" and "C":
    ap = "Aprovado"

elif conceito == "D" and "E":
    ap = "Reprovado"

print("Notas: {}, {}, {}, {} \nMédia final: {} \nConceito: {} \n{} " .format(n1, n2, n3, n4, media, conceito, ap))
