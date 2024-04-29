# Crie um programa que leia algo e informe:
#  3.1. O tipo primitivo dessa informação;
#  3.2. Só tem espaços em branco;
#  3.3. É do tipo numérico;
#  3.4. É do tipo string;
#  3.5. Está em letras maiúculas;
#  3.5. Está em letras minúculas;
#  3.6. Está captalizada.

algo = input("Digite algo: ") #sem conversão = string

print(type(algo))

print("Só tem espaços", algo.isspace())
print("É do tipo numérico?", algo.isnumeric())
print("É String?", algo.isalpha())
print("Está em letras maiúsculas?", algo.isupper())
print("Está em letras minúsculas?", algo.islower())
print("Está Captalizada?", algo.istitle())
