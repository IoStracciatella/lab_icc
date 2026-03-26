senha = input().strip()

erros = []

if len(senha) < 6 or len(senha) > 20:
    erros.append("tamanho invalido")

tem_minuscula = False
for char in senha:
    if char.islower():
        tem_minuscula = True
        break
if not tem_minuscula:
    erros.append("sem minuscula")

tem_maiuscula = False
for char in senha:
    if char.isupper():
        tem_maiuscula = True
        break
if not tem_maiuscula:
    erros.append("sem maiuscula")

tem_numero = False
for char in senha:
    if char.isdigit():
        tem_numero = True
        break
if not tem_numero:
    erros.append("sem digito")

caracter_invalido = False
for char in senha:
    if ord(char) < 32 or ord(char) > 126:
        caracter_invalido = True
        break
if caracter_invalido:
    erros.append("caracteres invalidos")

repetido = False
for i in range(len(senha)-2):
    if senha[i] == senha[i+1] == senha[i+2]:
        repetido = True
        break
if repetido:
    erros.append("3 caracteres repetidos")

def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

data_valida = False
for i in range(len(senha)-5):
    pedaco = senha[i:i+6]
    if pedaco.isdigit():
        dia = int(pedaco[:2])
        mes = int(pedaco[2:4])
        ano = int(pedaco[4:6])
        if 0 <= ano <= 25:
            ano_completo = 2000 + ano
            if mes == 2:
                if ano_bissexto(ano_completo):
                    if 1 <= dia <= 29:
                        data_valida = True
                else:
                    if 1 <= dia <= 28:
                        data_valida = True
            elif mes in [1,3,5,7,8,10,12]:
                if 1 <= dia <= 31:
                    data_valida = True
            elif mes in [4,6,9,11]:
                if 1 <= dia <= 30:
                    data_valida = True
            else:
                if 1 <= mes <= 12 and 1 <= dia <= 31:
                    pass

for i in range(len(senha)-7):
    pedaco = senha[i:i+8]
    if pedaco.isdigit():
        dia = int(pedaco[:2])
        mes = int(pedaco[2:4])
        ano = int(pedaco[4:8])
        if 1900 <= ano <= 2025:
            if mes == 2:
                if ano_bissexto(ano):
                    if 1 <= dia <= 29:
                        data_valida = True
                else:
                    if 1 <= dia <= 28:
                        data_valida = True
            elif mes in [1,3,5,7,8,10,12]:
                if 1 <= dia <= 31:
                    data_valida = True
            elif mes in [4,6,9,11]:
                if 1 <= dia <= 30:
                    data_valida = True
            else:
                if 1 <= mes <= 12 and 1 <= dia <= 31:
                    pass

if data_valida:
    erros.append("data valida")

if len(erros) == 0:
    print("senha forte")
else:
    for erro in erros:
        print("senha fraca:", erro)