import json

def main():
    data = json.loads(input())
    
    produto = data["produto"]
    categoria = data["categoria"]
    reviews = data["reviews"]
    
    palavras_peso = {}
    
    for review in reviews:
        comentario = review["comentario"].lower()
        estrelas = review["estrelas"]
        
        for char in "!?,.;:":
            comentario = comentario.replace(char, '')
        
        palavras = comentario.split()
        
        for palavra in palavras:
            if palavra not in palavras_peso:
                palavras_peso[palavra] = 0
            
            if estrelas >= 4:
                palavras_peso[palavra] += 1
            elif estrelas <= 2:
                palavras_peso[palavra] -= 1
    
    comentario_teste = input().lower()
    
    for char in "!?,.;:":
        comentario_teste = comentario_teste.replace(char, '')
    
    palavras_teste = comentario_teste.split()
    
    soma_peso = 0
    for palavra in palavras_teste:
        if palavra in palavras_peso:
            soma_peso += palavras_peso[palavra]
    
    if soma_peso > 0:
        classificacao = "Bom"
    elif soma_peso < 0:
        classificacao = "Ruim"
    else:
        classificacao = "Neutro"
    
    print(f"Nome: {produto} Categoria: {categoria} Comentario: {classificacao}")

if __name__ == "__main__":
    main()