valor_hamburguer = float(input())
quantidade_hamburguer = int(input())
valor_bebida = float(input())
quantidade_bebida = int(input())
valor_pago = float(input())

valor_total = (valor_hamburguer * quantidade_hamburguer) + \
    (valor_bebida * quantidade_bebida)
troco = valor_pago - valor_total
print(
    f"O preço final do pedido é R$ {valor_total:.2f}. Seu troco é R$ {troco:.2f}.")
