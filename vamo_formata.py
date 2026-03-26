s = input()
partes = s.split('-')
dados = {}
for p in partes:
    if ':' not in p:
        continue
    chave, valor = p.split(':', 1)
    dados[chave.strip().upper()] = valor.strip()
id_formatado = dados["ID"].lower()
nome_formatado = dados["NOME"].title()
idade_formatada = int(dados["IDADE"])
cidade_formatada = dados["CIDADE"].upper()
print("--- Ficha Cadastral ---")
print(f"ID: {id_formatado}")
print(f"Nome: {nome_formatado}")
print(f"Idade: {idade_formatada}")
print(f"Cidade: {cidade_formatada}")
