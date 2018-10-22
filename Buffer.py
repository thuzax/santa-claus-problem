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


    def remove(self):
        if(self.estaVazio()):
            return None
        return self.pilha.pop()