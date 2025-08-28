n = int(input())
a = n

while n > 1:
    a = a * (n - 1)
    n -= 1
print(a)