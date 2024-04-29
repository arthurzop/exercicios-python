quant = int(input("quantidade: "))
c = 0
soma = 0
while c < quant:
    soma += int(input("idade: "))
    c += 1

print(f"media: {soma/quant}")

