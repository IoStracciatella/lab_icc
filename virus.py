trecho = input().strip().upper()
virus = input().strip().upper()

tipo = ""
if 'U' in virus:
    tipo = "RNA"
else:
    tipo = "DNA"

contagem = 0
i = 0
while i <= len(virus) - len(trecho):
    if virus[i:i+len(trecho)] == trecho:
        contagem += 1
        i += len(trecho)
    else:
        i += 1

resistencia = ""
if contagem == 0:
    resistencia = "Nao resistente"
elif contagem == 1:
    resistencia = "Resistente"
elif contagem == 2:
    resistencia = "Muito resistente"
else:
    resistencia = "Super resistente"

print("INFORMACOES DO VIRUS")
print(f"Tipo: {tipo}")
print(f"Resistencia: {resistencia}")
print(f"Numero de ocorrencias: {contagem}")