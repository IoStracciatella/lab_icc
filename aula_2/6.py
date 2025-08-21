contador_lancamentos = 0
contador_seis = 0

while contador_seis < 3:
    numero = int(input())
    
    # Validação do número
    if numero < 1 or numero > 6:
        print("Numero invalido! Digite um numero entre 1 e 6.")
        continue  # não conta como lançamento válido
    
    # Contabiliza lançamento válido
    contador_lancamentos += 1
    
    # Verifica se foi um 6
    if numero == 6:
        contador_seis += 1
    else:
        contador_seis = 0  # reset se não for 6

print(f"Voce conseguiu 3 seis consecutivos em {contador_lancamentos} lancamentos!")
