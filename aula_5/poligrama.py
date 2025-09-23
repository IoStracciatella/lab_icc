def main():
    import sys

    N = int(sys.stdin.readline().strip())
    P = sys.stdin.readline().strip()

    if len(P) != N:
        print('*')
        return

    divisores = []
    for i in range(1, N):
        if N % i == 0:
            divisores.append(i)

    divisores.sort(reverse=True)

    def sao_anagramas(a, b):
        return sorted(a) == sorted(b)

    raiz_encontrada = None
    for k in divisores:
        num_blocos = N // k
        bloco_ref = P[0:k]
        todos_anagramas = True
        for i in range(num_blocos):
            bloco_atual = P[i*k:(i+1)*k]
            if not sao_anagramas(bloco_ref, bloco_atual):
                todos_anagramas = False
                break
        
        if todos_anagramas:
            raiz_encontrada = bloco_ref

    if raiz_encontrada:
        print(raiz_encontrada)
    else:
        print('*')

if __name__ == "__main__":
    main()