import json

stopwords = [
    "o", "a", "os", "as", "em", "uma", "uns", "umas",
    "ele", "ela", "elee", "elas", "meu", "minha", "teu", "tua", "seu", "sua",
    "de", "de", "da", "dos", "das", "em", "no", "na", "nos", "nas", "por", "para", "com", "sem", "sobre",
    "c", "ou", "mas", "porque", "que", "como", "quando", "se"
]

def filtrar_stopwords(texto):
    palavras = texto.split()
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stopwords]
    return ' '.join(palavras_filtradas)

def filtrar_dados(dados):
    dados_filtrados = {"positivo": [], "negativo": []}
    for categoria in dados:
        for frase in dados[categoria]:
            frase_filtrada = filtrar_stopwords(frase)
            dados_filtrados[categoria].append(frase_filtrada)
    return dados_filtrados

class ClassificadorNaiveBayes:
    def __init__(self):
        self.vocabulario = set()
        self.contagem_palavras = {"positivo": {}, "negativo": {}}
        self.contagem_documentos = {"positivo": 0, "negativo": 0}
        self.total_documentos = 0
        
    def train(self, frases, classe):
        for frase in frases:
            self.contagem_documentos[classe] += 1
            self.total_documentos += 1
            
            palavras = frase.split()
            for palavra in palavras:
                self.vocabulario.add(palavra)
                if palavra not in self.contagem_palavras[classe]:
                    self.contagem_palavras[classe][palavra] = 0
                self.contagem_palavras[classe][palavra] += 1
    
    def classify(self, frase):
        palavras = frase.split()
        
        prob_positivo = self.contagem_documentos["positivo"] / self.total_documentos
        prob_negativo = self.contagem_documentos["negativo"] / self.total_documentos
        
        for palavra in palavras:
            if palavra in self.vocabulario:
                contagem_pos = self.contagem_palavras["positivo"].get(palavra, 0) + 1
                contagem_neg = self.contagem_palavras["negativo"].get(palavra, 0) + 1
                
                total_pos = sum(self.contagem_palavras["positivo"].values()) + len(self.vocabulario)
                total_neg = sum(self.contagem_palavras["negativo"].values()) + len(self.vocabulario)
                
                prob_positivo *= contagem_pos / total_pos
                prob_negativo *= contagem_neg / total_neg
        
        return "positivo" if prob_positivo > prob_negativo else "negativo"

def main():
    json_input = input()
    dados = json.loads(json_input)
    
    frase_classificar = input()
    
    dados_filtrados = filtrar_dados(dados)
    
    classificador = ClassificadorNaiveBayes()
    
    classificador.train(dados_filtrados["positivo"], "positivo")
    classificador.train(dados_filtrados["negativo"], "negativo")
    
    frase_filtrada = filtrar_stopwords(frase_classificar)
    resultado = classificador.classify(frase_filtrada)
    
    print(f"classificacao: {resultado}")

if __name__ == "__main__":
    main()