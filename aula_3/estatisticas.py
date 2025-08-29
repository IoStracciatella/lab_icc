import random
import math

def formatar_inteiro(valor):
    """Formata o número para remover .0 se for inteiro (apenas para min, max, Q1, Q3, IQR)"""
    if valor == int(valor):
        return str(int(valor))
    else:
        return f"{valor:.6f}".rstrip('0').rstrip('.')

def formatar_mediana(valor):
    """Formata a mediana para sempre mostrar .0 quando for inteira"""
    if valor == int(valor):
        return f"{valor:.1f}"
    else:
        return f"{valor:.6f}".rstrip('0').rstrip('.')

def formatar_geral(valor):
    """Formata o número normalmente com 6 casas decimais (para as outras estatísticas)"""
    return f"{valor:.6f}".rstrip('0').rstrip('.')

def main():
    random.seed(int(input().strip()))
    n = int(input().strip())
    dist = input().strip()
    params = input().split()
    
    samples = []
    if dist == "uniforme":
        a, b = map(float, params)
        samples = [random.uniform(a, b) for _ in range(n)]
    elif dist == "binomial":
        n_binom, p = map(float, params)
        samples = [random.binomialvariate(n_binom, p) for _ in range(n)]
    elif dist == "beta":
        alpha, beta = map(float, params)
        samples = [random.betavariate(alpha, beta) for _ in range(n)]
    elif dist == "exponencial":
        lambd = float(params[0])
        samples = [random.expovariate(lambd) for _ in range(n)]
    elif dist == "gamma":
        alpha, beta = map(float, params)
        samples = [random.gammavariate(alpha, beta) for _ in range(n)]
    elif dist == "gauss":
        mu, sigma = map(float, params)
        samples = [random.gauss(mu, sigma) for _ in range(n)]
    elif dist == "lognormal":
        mu, sigma = map(float, params)
        samples = [random.lognormvariate(mu, sigma) for _ in range(n)]
    elif dist == "pareto":
        alpha = float(params[0])
        samples = [random.paretovariate(alpha) for _ in range(n)]
    elif dist == "weibull":
        alpha, beta = map(float, params)
        samples = [random.weibullvariate(alpha, beta) for _ in range(n)]
    
    sorted_samples = sorted(samples)
    mean = sum(samples) / n
    
    if n % 2 == 1:
        median = sorted_samples[n//2]
    else:
        median = (sorted_samples[n//2 - 1] + sorted_samples[n//2]) / 2
    
    min_val = min(samples)
    max_val = max(samples)
    
    Q1 = sorted_samples[n//4]
    Q3 = sorted_samples[3*n//4]
    IQR = Q3 - Q1
    
    variance = sum((x - mean) ** 2 for x in samples) / n
    std_dev = math.sqrt(variance)
    
    if mean != 0:
        coeff_var = std_dev / mean
    else:
        coeff_var = 0
    
    mad = sum(abs(x - mean) for x in samples) / n
    
    if std_dev != 0:
        skewness = sum((x - mean) ** 3 for x in samples) / n / (std_dev ** 3)
    else:
        skewness = 0
        
    if std_dev != 0:
        kurtosis = sum((x - mean) ** 4 for x in samples) / n / (std_dev ** 4)
    else:
        kurtosis = 0
    
    # Formatação específica para cada tipo de estatística
    print(f"Média: {formatar_geral(mean)}")
    print(f"Mediana: {formatar_mediana(median)}")  # Formatação especial para mediana
    print(f"Mínimo: {formatar_inteiro(min_val)}")
    print(f"Máximo: {formatar_inteiro(max_val)}")
    print(f"Q1: {formatar_inteiro(Q1)}")
    print(f"Q3: {formatar_inteiro(Q3)}")
    print(f"Amplitude interquartil: {formatar_inteiro(IQR)}")
    print(f"Variância: {formatar_geral(variance)}")
    print(f"Desvio padrão: {formatar_geral(std_dev)}")
    print(f"Coeficiente de variação: {formatar_geral(coeff_var)}")
    print(f"Desvio absoluto médio: {formatar_geral(mad)}")
    print(f"Coeficiente de assimetria: {formatar_geral(skewness)}")
    print(f"Coeficiente de curtose: {formatar_geral(kurtosis)}")

if __name__ == "__main__":
    main()