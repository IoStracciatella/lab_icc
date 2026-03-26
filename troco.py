compra = float(input())
pago = float(input())

troco = pago - compra

cedulas_moedas = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
nomes = ["200.00", "100.00", "50.00", "20.00", "10.00", "5.00", "2.00", "1.00", "0.50", "0.25", "0.10", "0.05", "0.01"]

troco_centavos = round(troco * 100)

resultado = []

for i in range(len(cedulas_moedas)):
    valor = cedulas_moedas[i]
    quantidade = troco_centavos // valor
    if quantidade > 0:
        resultado.append(f"{quantidade} x R$ {nomes[i]}")
        troco_centavos -= quantidade * valor

for linha in resultado:
    print(linha)