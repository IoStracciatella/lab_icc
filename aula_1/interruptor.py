IA = int(input())
IB = int(input())
FA = int(input())
FB = int(input())

if FA == IA and FB == IB:
    print(0)
elif FA != IA and FB == IB:
    print(1)
elif FA == IA and FB != IB:
    print(2)
elif FA != IA and FB != IB:
    print(1) 

#if IA == 0 and IB == 0:
#    print("1")
#elif IA == 1 and IB == 0:
#    print("2")
#elif IA == 0 and IB == 1:
#    print("1")
#else:
#    print("0")