numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = 'Vegano' if input() is "s" else "Nao-vegano"
    print(f"Pedido {i}: {prato} ({ehVegano}) - {calorias} calorias")
