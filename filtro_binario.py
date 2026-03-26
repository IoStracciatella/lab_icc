numero_decimal = int(input())
n = int(input())
operacoes = []
for _ in range(n):
    operacoes.append(input().strip())

binario = bin(numero_decimal)[2:]

for op in operacoes:
    if op == 'INVERSO':
        novo = ''
        for bit in binario:
            if bit == '0':
                novo += '1'
            else:
                novo += '0'
        binario = novo
    elif op == 'DUPLICAR':
        binario = binario + binario
    elif op == 'DESLOCAR_ESQ':
        if len(binario) > 0:
            binario = binario[1:] + binario[0]
    elif op == 'DESLOCAR_DIR':
        if len(binario) > 0:
            binario = binario[-1] + binario[:-1]
    elif op == 'ESPELHAR':
        binario = binario[::-1]
    elif op == 'MAIORIA':
        uns = binario.count('1')
        zeros = binario.count('0')
        if uns > zeros:
            binario = '1' * len(binario)
        elif zeros > uns:
            binario = '0' * len(binario)

resultado_decimal = int(binario, 2)
print(resultado_decimal)