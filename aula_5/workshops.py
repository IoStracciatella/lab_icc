N = int(input().strip())
inscricoes = {}

for i in range(N):
    entrada = input().strip()
    nome, workshop = entrada.split(",")
    if workshop not in inscricoes:
        inscricoes[workshop] = set()
    inscricoes[workshop].add(nome)
    i+=1
consulta = input().strip()
if consulta in inscricoes:
    print(len(inscricoes[consulta]))
else:
    print(0)
