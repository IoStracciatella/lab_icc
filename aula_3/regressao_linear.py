def main():
    try:
        n = int(input().strip())
    except:
        return
    
    pontos = []
    for i in range(n):
        try:
            x = float(input().strip())
            y = float(input().strip())
            pontos.append((x, y))
        except:
            continue
    
    if len(pontos) == 0:
        return
    
    n_valido = len(pontos)
    soma_x = sum(x for x, y in pontos)
    soma_y = sum(y for x, y in pontos)
    media_x = soma_x / n_valido
    media_y = soma_y / n_valido
    
    numerador = 0
    denominador = 0
    for x, y in pontos:
        numerador += (x - media_x) * (y - media_y)
        denominador += (x - media_x) ** 2
    
    if denominador == 0:
        a = 0
    else:
        a = numerador / denominador
    
    b = media_y - a * media_x
    
    print(f"{a:.2f}")
    print(f"{b:.2f}")

if __name__ == "__main__":
    main()