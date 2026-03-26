n = int(input())
produtos = {}

for _ in range(n):
    nome = input().strip()
    preco = float(input())
    produtos[nome] = preco

consulta = input().strip()

print("Lista de compras:")
for produto, preco in produtos.items():
    print(f"- {produto}: R$ {preco:.2f}")

total = sum(produtos.values())
media = total / len(produtos)
mais_caro = max(produtos, key=produtos.get)
mais_barato = min(produtos, key=produtos.get)

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Media de precos: R$ {media:.2f}")
print(f"Mais caro: {mais_caro} (R$ {produtos[mais_caro]:.2f})")
print(f"Mais barato: {mais_barato} (R$ {produtos[mais_barato]:.2f})")

if consulta in produtos:
    print(f"\nProduto encontrado: {consulta} custa R$ {produtos[consulta]:.2f}")
else:
    print(f"\nProduto não encontrado: {consulta}")