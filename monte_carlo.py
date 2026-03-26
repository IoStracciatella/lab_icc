import random
import matplotlib.pyplot as plt

def gerar_pontos(n):
    pontos = []
    random.seed(42)
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        pontos.append((x, y))
    return pontos

def dentro_do_circulo(ponto):
    x, y = ponto
    return x*x + y*y <= 1

def estimar_pi(pontos):
    dentro = 0
    for ponto in pontos:
        if dentro_do_circulo(ponto):
            dentro += 1
    return 4 * dentro / len(pontos)

def plotar_pontos(pontos):
    x_dentro = []
    y_dentro = []
    x_fora = []
    y_fora = []
    
    for ponto in pontos:
        x, y = ponto
        if dentro_do_circulo(ponto):
            x_dentro.append(x)
            y_dentro.append(y)
        else:
            x_fora.append(x)
            y_fora.append(y)
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x_dentro, y_dentro, color='blue', s=1, label='Dentro')
    plt.scatter(x_fora, y_fora, color='red', s=1, label='Fora')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Estimação de π usando Monte Carlo')
    plt.legend()
    plt.axis('equal')
    plt.show()

def main():
    ni = int(input())
    pontos = gerar_pontos(ni)
    pi_estimado = estimar_pi(pontos)
    
    print(f"Numero de pontos: {ni}")
    print(f"Valor estimado de pi: {pi_estimado:.6f}")
    
    plotar_pontos(pontos)

if __name__ == "__main__":
    main()