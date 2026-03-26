def converter_para_decimal(numero, base):
    return int(numero, base)

def converter_decimal_para_base(numero, base):
    if base == 10:
        return str(numero)
    elif base == 2:
        return bin(numero)[2:]
    elif base == 8:
        return oct(numero)[2:]
    elif base == 16:
        return hex(numero)[2:].upper()

entrada1 = input().split()
entrada2 = input().split()
operacao = input().strip()
base_saida = int(input())

num1_str = entrada1[0]
base1 = int(entrada1[1])
num2_str = entrada2[0]
base2 = int(entrada2[1])

num1_decimal = converter_para_decimal(num1_str, base1)
num2_decimal = converter_para_decimal(num2_str, base2)

if operacao == 'SOMA':
    resultado = num1_decimal + num2_decimal
elif operacao == 'SUB':
    resultado = num1_decimal - num2_decimal
elif operacao == 'MUL':
    resultado = num1_decimal * num2_decimal
elif operacao == 'DIV':
    resultado = num1_decimal // num2_decimal

resultado_final = converter_decimal_para_base(resultado, base_saida)
print(resultado_final)