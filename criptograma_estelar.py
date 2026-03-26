n = int(input())
mapa = {}
for _ in range(n):
    data = input().split()
    if len(data) < 2:
        continue
    simbolo = data[0]
    letra = data[1]
    mapa[simbolo] = letra

L = int(input())
mensagem_cripto = []
for _ in range(L):
    mensagem_cripto.append(input())

mensagem_decifrada = []
traduzidos = 0
simbolos_unicos = set()

for linha in mensagem_cripto:
    nova_linha = ""
    for char in linha:
        if char in mapa:
            nova_linha += mapa[char]
            traduzidos += 1
            if char != ' ':
                simbolos_unicos.add(char)
        else:
            nova_linha += char
            if char != ' ':
                simbolos_unicos.add(char)
    mensagem_decifrada.append(nova_linha)

freq = {}
for linha in mensagem_decifrada:
    for char in linha:
        if char.isalpha():
            char_lower = char.lower()
            freq[char_lower] = freq.get(char_lower, 0) + 1

print("Mensagem Decifrada:")
for linha in mensagem_decifrada:
    print(linha)

print("\nEstatísticas:")
print(f"Caracteres traduzidos: {traduzidos}")
print(f"Símbolos únicos na mensagem original: {len(simbolos_unicos)}")
print("\nFrequência de Letras (a-z):")
for letra in sorted(freq.keys()):
    if 'a' <= letra <= 'z':
        print(f"- {letra}: {freq[letra]}")