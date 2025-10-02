dados_bruto = input()
dados = dados_bruto.split("-")

ID = dados[0]
id_novo = ID[3:]
id_novo = ID.lower()
nome = dados[1]
nome_novo = nome[5:]
nome_novo = nome.title()
idade = dados[2]
idade_nova = idade[6:]
idade_nova = int(idade)
cidade = dados[3]
cidade_novo = cidade[7:]
cidade_novo = cidade.upper()

print("--- Ficha Cadastral ---")
print(f"ID: {id_novo}")
print(f"Nome: {nome_novo}")
print(f"Idade: {idade_nova}")
print(f"Cidade: {cidade_novo}")