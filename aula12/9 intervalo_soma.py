#9. Altere o programa anterior para mostrar no final a soma dos números.

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

a1 = a
b1 = b
soma = 0
while a <= b:
    print(a)
    a += 1
    soma += a
    
while b <= a:
    print(b)
    b += 1
    soma += b

print(f"\nA soma é: {soma}")


