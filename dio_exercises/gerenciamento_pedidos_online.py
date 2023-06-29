
n = int(input())

total = 0

for i in range(1, n + 1):
    pedido = input().split(" ")
    nome = pedido[0]
    valor = float(pedido[1])
    total += valor


desconto = int(input().replace("%", ""))
valor_total = total - (total * (desconto / 100))
print(f"Valor total: {valor_total:.2f}")
