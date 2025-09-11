n = int(input())
matriz = []
for _ in range(n*n):
    matriz.append(int(input()))
lista = []
while True:
    x = int(input())
    if x == -1:
        break
    lista.append(x)
res = []
for v in lista:
    res.append(matriz.count(v))
print(*res)
