n = int(input())

vendas_por_categoria = {}

for _ in range(n):
    entrada = input().split(',')
    if len(entrada) < 2:
        continue
        
    categoria = entrada[0].strip()
    valor_str = entrada[1].strip()
    
    try:
        valor = float(valor_str)
    except:
        continue
    
    if categoria not in vendas_por_categoria:
        vendas_por_categoria[categoria] = []
    
    vendas_por_categoria[categoria].append(valor)

categorias_ordenadas = sorted(vendas_por_categoria.keys())

for categoria in categorias_ordenadas:
    vendas = vendas_por_categoria[categoria]
    total_vendas = len(vendas)
    total_valor = sum(vendas)
    media = total_valor / total_vendas if total_vendas > 0 else 0
    
    print(f"Categoria: {categoria}")
    print(f"  - Vendas: {total_vendas}")
    print(f"  - Média: R$ {media:.2f}")
    print(f"  - Total: R$ {total_valor:.2f}")