import sys

data = sys.stdin.read().strip().split()
if not data:
    exit()
n = int(data[0]); m = int(data[1])
vals = list(map(int, data[2:2 + n * m]))
mat = [vals[i * m:(i + 1) * m] for i in range(n)]

soma_total = sum(sum(row) for row in mat)
media_geral = soma_total / (n * m)
soma_linha = [sum(row) for row in mat]
soma_turno = [sum(mat[i][j] for i in range(n)) for j in range(m)]
maior_valor = max(max(row) for row in mat)
menor_valor = min(min(row) for row in mat)

print("Matriz de producao:")
print("[", end="")
for i, row in enumerate(mat):
    if i == 0:
        print("[" + " ".join(map(str, row)) + "]", end="")
    else:
        print("\n [" + " ".join(map(str, row)) + "]", end="")
print("]")
print()
print("Soma total:", soma_total)
print("Media geral: %.2f" % media_geral)
print("Soma por linha:", "[" + " ".join(map(str, soma_linha)) + "]")
print("Soma por turno:", "[" + " ".join(map(str, soma_turno)) + "]")
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)
