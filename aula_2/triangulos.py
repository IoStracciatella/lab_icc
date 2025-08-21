a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0:
    print(False)
elif (a + b > c) and (a + c > b) and (b + c > a):
    print(True)
else:
    print(False)
