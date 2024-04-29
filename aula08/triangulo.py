# 6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Digite o tamanho do 1° lado: "))
lado2 = float(input("Digite o tamanho do 2° lado: "))
lado3 = float(input("Digite o tamanho do 3° lado: "))

tr1 = lado1 + lado2 
tr2 = lado2 + lado3
tr3 = lado1 + lado3

if tr1 < tr2 and tr1 < tr3 and tr2 < tr3:
    print("Não forma um triangulo")

elif lado1 == lado2 == lado3:
    print("Triangulo equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Traingulo isósceles")

else:
    print("Triangulo Escaleno")