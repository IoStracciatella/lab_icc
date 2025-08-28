n = int(input())
contador = 0

a1 = 0
a2 = 1
a3 = 0

print(0)
while contador < n - 1:
    a3 = a1 + a2

    print(a3)
    contador+=1 
    a2 = a1
    a1 = a3