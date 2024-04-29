# 4. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
# que são Tensão, Resistência e Corrente. Sabe-se que:
# U = R * I, 
# onde, 
# U é a Tensão      (em V), 
# R é a Resistência (em Ώ) e,
# I é a Corrente    (em A).

# Você foi contratado(a) pela empresa para atender a essa solicitação.
# Construa um programa que apresente o seguinte menu:

# ******************************
# CÁLCULO DE GRANDEZAS ELÉTRICAS
# ******************************
# 1. Tensão (em Volt)
# 2. Resistência (em Ohm)
# 3. Corrente (em Ampére)
# 4. Sair do programa
# ******************************
# Qual grandeza deseja calcular?

# Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo.

# Quando o eletricista escolher:
# 1. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente.
#    Utilizar a fórmula: U = R * I

# 2. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente.
#    Utilizar a fórmula: R = U / I

# 3. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência.
#    Utilizar a fórmula: I = U / R

# Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
# Obs.: Qualquer opção diferente das apresentadas no menu (1 a 4) deverão ser informadas ao usuário como 'Opção inválida!'
# Salvar o código como: grandezas.py

print("*****************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("*****************************") 
print("1. Tensão (Em volts) \n2. Resistencia (em Ohm) \n3. Corrente (Em Ampére) \n4. Sair do programa")
print("*****************************")
op = int(input("Qual Grandeza deseja calcular? (De 1 a 4): "))

if op == 1:
    r = float(input("Digite o valor da Resistencia: "))
    i = float(input("Digite o valor da Corrente: "))
    u = r * i
    print("A tensão é: {}" .format(u))

elif op == 2:
    u = float(input("Digite o valor da Tensão: "))
    i = float(input("Digite o valor da Resistencia: "))
    r = u / i
    print("A resistencia é: {}" .format(r))

elif op == 3:
    r = float(input("Digite o valor da resistencia: "))
    u = float(input("Digite o valor da Tensão: "))
    i = u / r
    print("A Corrente é: {}" .format(i))

elif op == 4:
    print("Saindo do programa.")
    exit

else:
    print("Opção Inválida!")