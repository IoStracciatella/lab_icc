n1 = int(input())
n2 = int(input())
simbolo = input()
resultado = 0

if simbolo == "+":
    resultado = n1 + n2
    print(int(resultado))
elif simbolo == "-":
    resultado = n1 - n2
    print(int(resultado))
elif simbolo == "*":
    resultado = n1 * n2
    print(int(resultado))
elif simbolo == "/":
    if n2 != 0: 
        resultado = n1/n2
        print(f"{resultado:.2f}")
    else:
        print("Erro: divisao por zero")
else:
    print("Erro: operacao invalida")