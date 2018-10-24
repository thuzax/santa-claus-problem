class Buffer:

    def __init__(self, tamanho):
        self.tamanhoMax = tamanho
        self.pilha = []
    
    def estaVazio(self):
        return len(self.pilha) == 0
    
    def estaCheio(self):
        return self.tamanhoMax == len(self.pilha)

    def getTamanho(self):
        return self.tamanhoMax

    def insere(self, objeto):
        if(self.estaCheio()):
            return
        self.pilha.append(objeto)

    def getPilha(self):
        return self.pilha

    def remove(self):
        if(self.estaVazio()):
            return None
        print("removeu!")
        pop = self.pilha.pop()
        return pop
    
    def getTamanhoAtual(self):
        return len(self.pilha)