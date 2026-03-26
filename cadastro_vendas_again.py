import runcodes

class Produto:
    def __init__(self, cod, nome, preco, estoque):
        self.cod = int(cod)
        self.nome = nome
        self.preco = float(preco)
        self.estoque = int(estoque)

class Venda:
    def __init__(self, mes, ano, cod, quantidade, preco_unitario):
        self.mes = int(mes)
        self.ano = int(ano)
        self.cod = int(cod)
        self.quantidade = int(quantidade)
        self.preco_unitario = float(preco_unitario)
        self.valor_total = float(quantidade) * float(preco_unitario)

sistema_produtos = {}
historico_vendas = []

def adicionar_produto(cod, nome, preco, estoque):
    cod_int = int(cod)
    sistema_produtos[cod_int] = Produto(cod_int, nome, float(preco), int(estoque))

def remover_produto(cod):
    cod_int = int(cod)
    if cod_int in sistema_produtos:
        del sistema_produtos[cod_int]
    else:
        print("PRODUTO_INEXISTENTE")

def listar_produtos():
    produtos_ordenados = sorted(sistema_produtos.values(), key=lambda x: x.cod)
    for prod in produtos_ordenados:
        print(f"{prod.cod} {prod.nome} {prod.preco:.2f} {prod.estoque}")

def consultar_produto(cod):
    cod_int = int(cod)
    if cod_int in sistema_produtos:
        prod = sistema_produtos[cod_int]
        print(f"{prod.nome} {prod.preco:.2f}")
    else:
        print("PRODUTO_INEXISTENTE")

def registrar_venda(cod, quantidade, mes, ano):
    cod_int = int(cod)
    qtd_int = int(quantidade)
    mes_int = int(mes)
    ano_int = int(ano)
    
    if cod_int not in sistema_produtos:
        print("ERRO: PRODUTO_INEXISTENTE")
        return
    
    if qtd_int <= 0:
        print("ERRO: QUANTIDADE_INVALIDA")
        return
    
    produto = sistema_produtos[cod_int]
    
    if qtd_int > produto.estoque:
        print("ERRO: ESTOQUE_INSUFICIENTE")
        return
    
    produto.estoque -= qtd_int
    valor_total = qtd_int * produto.preco
    nova_venda = Venda(mes_int, ano_int, cod_int, qtd_int, produto.preco)
    historico_vendas.append(nova_venda)
    print(f"VENDA_OK {valor_total:.2f}")

def listar_vendas_produto(cod):
    cod_int = int(cod)
    encontrou = False
    for venda in historico_vendas:
        if venda.cod == cod_int:
            print(f"{venda.mes} {venda.ano} {venda.quantidade} {venda.preco_unitario:.2f} {venda.valor_total:.2f}")
            encontrou = True
    if not encontrou:
        print("SEM_VENDAS")

def listar_vendas_ano(ano):
    ano_int = int(ano)
    encontrou = False
    for venda in historico_vendas:
        if venda.ano == ano_int:
            print(f"{venda.mes} {venda.cod} {venda.quantidade} {venda.preco_unitario:.2f} {venda.valor_total:.2f}")
            encontrou = True
    if not encontrou:
        print("SEM_VENDAS")

def listar_todas_vendas():
    if not historico_vendas:
        print("SEM_VENDAS")
        return
    for venda in historico_vendas:
        print(f"{venda.mes} {venda.ano} {venda.cod} {venda.quantidade} {venda.preco_unitario:.2f} {venda.valor_total:.2f}")

def carregar_estoque(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        
        sistema_produtos.clear()
        numero_linha = 1
        
        for linha in linhas:
            linha = linha.strip()
            if not linha:
                numero_linha += 1
                continue
                
            partes = linha.split(',')
            if len(partes) != 4:
                print(f"Linha {numero_linha} Invalida!")
                numero_linha += 1
                continue
            
            try:
                cod = partes[0].strip()
                nome = partes[1].strip()
                preco = partes[2].strip()
                estoque = partes[3].strip()
                
                cod_int = int(cod)
                if cod_int <= 0:
                    raise ValueError
                
                preco_float = float(preco)
                estoque_int = int(estoque)
                if estoque_int < 0:
                    raise ValueError
                
                sistema_produtos[cod_int] = Produto(cod_int, nome, preco_float, estoque_int)
                
            except ValueError:
                print(f"Linha {numero_linha} Invalida!")
            
            numero_linha += 1
        
        print(f"ESTOQUE_CARREGADO {nome_arquivo}")
        
    except FileNotFoundError:
        print("ERRO: ARQUIVO_INEXISTENTE")

def salvar_estoque(nome_arquivo):
    produtos_ordenados = sorted(sistema_produtos.values(), key=lambda x: x.cod)
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for produto in produtos_ordenados:
            linha = f"{produto.cod},{produto.nome},{produto.preco:.2f},{produto.estoque}\n"
            arquivo.write(linha)
    
    runcodes.verificar_arquivo(nome_arquivo)

def carregar_vendas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
        
        historico_vendas.clear()
        numero_linha = 1
        
        for linha in linhas:
            linha = linha.strip()
            if not linha:
                numero_linha += 1
                continue
                
            partes = linha.split(',')
            if len(partes) != 6:
                print(f"Linha {numero_linha} Invalida!")
                numero_linha += 1
                continue
            
            try:
                mes = partes[0].strip()
                ano = partes[1].strip()
                cod = partes[2].strip()
                quantidade = partes[3].strip()
                preco_unitario = partes[4].strip()
                valor_total = partes[5].strip()
                
                mes_int = int(mes)
                if mes_int < 1 or mes_int > 12:
                    raise ValueError
                
                ano_int = int(ano)
                if ano_int < 1900 or ano_int > 2100:
                    raise ValueError
                
                cod_int = int(cod)
                if cod_int <= 0:
                    raise ValueError
                
                qtd_int = int(quantidade)
                if qtd_int <= 0:
                    raise ValueError
                
                preco_float = float(preco_unitario)
                total_float = float(valor_total)
                
                nova_venda = Venda(mes_int, ano_int, cod_int, qtd_int, preco_float)
                historico_vendas.append(nova_venda)
                
            except ValueError:
                print(f"Linha {numero_linha} Invalida!")
            
            numero_linha += 1
        
        print(f"HISTORICO_CARREGADO {nome_arquivo}")
        
    except FileNotFoundError:
        print("ERRO: ARQUIVO_INEXISTENTE")

def salvar_vendas(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for venda in historico_vendas:
            linha = f"{venda.mes},{venda.ano},{venda.cod},{venda.quantidade},{venda.preco_unitario:.2f},{venda.valor_total:.2f}\n"
            arquivo.write(linha)
    
    runcodes.verificar_arquivo(nome_arquivo)

def main():
    while True:
        try:
            entrada = input().strip()
            if not entrada:
                continue
                
            if entrada == "FIM":
                break
                
            partes = entrada.split()
            comando = partes[0]
            
            if comando == "ADICIONAR" and len(partes) == 5:
                adicionar_produto(partes[1], partes[2], partes[3], partes[4])
                
            elif comando == "REMOVER" and len(partes) == 2:
                remover_produto(partes[1])
                
            elif comando == "LISTAR_PRODUTOS":
                listar_produtos()
                
            elif comando == "CONSULTAR" and len(partes) == 2:
                consultar_produto(partes[1])
                
            elif comando == "VENDER" and len(partes) == 5:
                registrar_venda(partes[1], partes[2], partes[3], partes[4])
                
            elif comando == "LISTAR_POR_PRODUTO" and len(partes) == 2:
                listar_vendas_produto(partes[1])
                
            elif comando == "LISTAR_POR_ANO" and len(partes) == 2:
                listar_vendas_ano(partes[1])
                
            elif comando == "LISTAR_TODAS_VENDAS":
                listar_todas_vendas()
                
            elif comando == "CARREGAR_ESTOQUE" and len(partes) == 2:
                carregar_estoque(partes[1])
                
            elif comando == "SALVAR_ESTOQUE" and len(partes) == 2:
                salvar_estoque(partes[1])
                
            elif comando == "CARREGAR_VENDAS" and len(partes) == 2:
                carregar_vendas(partes[1])
                
            elif comando == "SALVAR_VENDAS" and len(partes) == 2:
                salvar_vendas(partes[1])
                
        except EOFError:
            break

if __name__ == "__main__":
    main()