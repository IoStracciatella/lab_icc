import numpy as np

c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))

M = np.array([c1, c2, c3]).T

print('--- Matriz de C para B ---')
print(M)

det = np.linalg.det(M)
if abs(det) < 1e-9:
    print('A base C nao e valida')
else:
    inv = np.linalg.inv(M)
    inv = np.round(inv, 5)
    print()
    print('--- Matriz de B para C ---')
    print(inv)
