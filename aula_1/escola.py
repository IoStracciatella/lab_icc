E = int(input()) * 2
A = int(input()) * 3
C = int(input()) * 5
T = (E + A + C)

if T >= 200:
    print("O")
elif 150 <= T <= 200:
    print("S")
elif 100 <= T <= 150:
    print("B")
else:
    print("N")