# 5. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 	À vista (em espécie) 	10
# 2	Cartão de débito	5
# 3	Cartão de crédito	3
# 4	PIX			7.5

# Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
# Ao fim, o programa deve informar o valor final a ser pago.
# Salvar o código como: black_friday.py

total = float(input("Digite o total da compra: "))
print("Condição de desconto")
print("1 - À vista \n2 - Cartão de debito \n3 - Cartão de Crédito \n4 - pix")
op = int(input("Selecione uma opção: "))

if op == 1:
    des = (10 * total) / 100
    valor = total - des
    print("Selecionado: À vista \nValor com desconto: R${:.2f}" .format(valor))

elif op == 2:
    des = (5 * total) / 100
    valor = total - des
    print("Selecionado: Cartão de Débito \nValor com desconto: R${:.2f}" .format(valor))

elif op == 3:
    des = (3 * total) / 100
    valor = total - des
    print("Selecionado: Cartão de Crédito \nValor com desconto: R${:.2f}" .format(valor))

elif op == 4:
    des = (7.5 * total) / 100
    valor = total - des
    print("Selecionado: pix \nValor com desconto: R${:.2f}" .format(valor))

else:
    print("Opção Inválida")
    exit

