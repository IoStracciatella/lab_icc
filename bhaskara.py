import math as mt

a = float(input())
b = float(input())
c = float(input())

delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b + mt.sqrt(delta))/2*a
    x2 = (-b - mt.sqrt(delta))/2*a
    print(x1, x2)
elif delta == 0:
    x1 = -b/2*a
    print(x1)
else:
    print("Nao existem raizes reais")
