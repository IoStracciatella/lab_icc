# Função para adicionar alunos e notas
def adicionar_aluno(lista_nomes, lista_notas):
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break
        nota = float(input(f"Digite a nota de {nome}: "))
        lista_nomes.append(nome)
        lista_notas.append(nota)

# Função para calcular estatísticas
def calcular_estatisticas(notas):
    media = sum(notas) / len(notas) if notas else 0
    maior = max(notas) if notas else None
    menor = min(notas) if notas else None
    return media, maior, menor

# Função para exibir resultados
def exibir_resultados(nomes, notas):
    media, maior, menor = calcular_estatisticas(notas)
    aprovados = [nomes[i] for i in range(len(notas)) if notas[i] >= 6]

    print("\n--- Resultados ---")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print("Aprovados:", ", ".join(aprovados) if aprovados else "Nenhum aluno aprovado")

# Programa principal
nomes = []
notas = []

adicionar_aluno(nomes, notas)
exibir_resultados(nomes, notas)
