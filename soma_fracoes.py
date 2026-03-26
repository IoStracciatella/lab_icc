A = int(input())
B = int(input())
C = int(input())
D = int(input())

den = B*D
num = B*C + A*D

divisores = [2, 3, 4, 5, 6, 7, 8, 9]
aux = 2

for i in divisores:
    while num % i == 0 and den % i == 0:
        num = num / i
        den = den / i

print(int(num), int(den))