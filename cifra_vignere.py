operacao = input().strip()
mensagem = input().strip()
chave = input().strip()

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tamanho_alfabeto = len(alfabeto)

resultado = []
indice_chave = 0

for char in mensagem:
    if char in alfabeto:
        pos_char = alfabeto.index(char)
        
        letra_chave = chave[indice_chave % len(chave)]
        pos_chave = alfabeto.index(letra_chave)
        
        if operacao == 'codificar':
            nova_pos = (pos_char + pos_chave) % tamanho_alfabeto
        else:
            nova_pos = (pos_char - pos_chave) % tamanho_alfabeto
            
        resultado.append(alfabeto[nova_pos])
        indice_chave += 1
    else:
        resultado.append(char)

print(''.join(resultado))