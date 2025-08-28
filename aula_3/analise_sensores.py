def main():
    dados_validos = []
    
    while True:
        entrada = input().strip()
        if not entrada:
            continue
        try:
            numero = float(entrada)
        except ValueError:
            continue
            
        if numero == -1.0:
            break
            
        if numero < 0.0 or numero > 14.0:
            continue
            
        dados_validos.append(numero)
        
    if not dados_validos:
        print("Nenhum dado valido foi coletado.")
    else:
        n = len(dados_validos)
        maximo = max(dados_validos)
        minimo = min(dados_validos)
        media = sum(dados_validos) / n
        
        # Formata a média com 1 casa decimal sempre
        media_formatada = f"{media:.1f}"
        
        print(f"Numero de coletas validas: {n}")
        print(f"pH maximo: {maximo:.1f}")
        print(f"pH minimo: {minimo:.1f}")
        print(f"pH medio: {media_formatada}")

if __name__ == "__main__":
    main()
