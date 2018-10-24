from Buffer import Buffer
from threading import Lock

class Controlador:
    instancia = None

    class __Controlador:
        def __init__(self, papaiNoel, listaElfo, listaRena, tamanhoGrupoElfos):
            self.listaRena = listaRena
            self.listaElfo = listaElfo
            self.papaiNoel = papaiNoel
            self.bufferElfo = Buffer(tamanhoGrupoElfos)
            self.bufferRena = Buffer(len(self.listaRena))
            self.contadorElfo = 0
            self.contadorRena = 0
            self.porta = Lock()
            self.anel = Lock()
        

        def __adicionaBufferElfo(self, elfo):
            if self.porta.acquire(False):
                if self.anel.acquire(False):
                    self.contadorElfo += 1
                    if self.contadorElfo == self.bufferElfo.getTamanho():
                        self.anel.release()
                        self.papaiNoel.acorda()
                    else:
                        self.porta.release()
                        self.anel.release()
                    self.bufferElfo.insere(elfo)
            
        
        def __adicionaBufferRena(self, rena):
            if self.anel.acquire(False):
                self.contadorRena += 1
                if self.contadorRena == self.bufferRena.getTamanho():
                    print("adicionou!")
                    self.anel.release()
                    self.papaiNoel.acorda()
                else:
                    self.anel.release()
                self.bufferRena.insere(rena)

        def __ajudaElfos(self):
            if self.anel.acquire(False):
                elfo = self.bufferElfo.remove()
                elfo.obtemAjuda()
                self.anel.release()
                self.papaiNoel.dorme()
        
        def __ajuda(self):
            if self.anel.acquire(False):
                if(self.__bufferRenasCheio()):
                    self.papaiNoel.ajudaRenas()
                    self.anel.release()
                    renas = self.bufferRena.getPilha()
                    # Amarrar as renas
                    for rena in renas:
                        if self.anel.acquire(False):
                            rena.amarraRena()
                            self.anel.release()
                    # Destribuir os brinquedos
                    if self.anel.acquire(False):
                        self.papaiNoel.distribuiBrinquedos()
                        self.anel.release()
                    # Desamarrar as renas
                    while not self.bufferRena.estaVazio():
                        rena = self.bufferRena.remove()
                        print(self.bufferRena.getTamanhoAtual())
                        self.contadorRena -= 1
                        print("Rena " + str(rena.name) + " sendo removido do buffer")
                        #Tranca o anel
                        if self.anel.acquire(False):
                            print("Rena " + str(rena.name) + " esta sendo desamarrada")
                            # Obtem a ajuda e tranca o anel novamente
                            rena.desamarraRena()
                            print("Rena " + str(rena.name) + " liberando o anel")
                            self.anel.release()
                            rena.tiraFerias()
                    # Voltar a dormir
                    self.papaiNoel.dorme()
                    for rena in self.listaRena:
                        rena.terminouFerias()
                    # for i in range(len(self.listaRena)):
                    #     print("AQY")
                        # self.listaRena[i].descansa()

                else:
                    self.papaiNoel.ajudaElfos()
                    elfo = self.bufferElfo.remove()
                    elfo.obtemAjuda()
                    self.anel.release()
                    self.papaiNoel.dorme()
                    # Enquanto tiver elfo no buffer...
                    while not self.bufferElfo.estaVazio():
                        # Pega um elfo do buffer
                        elfo = self.bufferElfo.remove()
                        print(self.bufferElfo.getTamanhoAtual())
                        self.contadorElfo -= 1
                        print("Elfo " + str(elfo.name) + " sendo removido do buffer")
                        #Tranca o anel
                        if self.anel.acquire(False):
                            print("Elfo " + str(elfo.name) + " trancando o anel")
                            # Obtem a ajuda e tranca o anel novamente
                            elfo.obtemAjuda()
                            print("Elfo " + str(elfo.name) + " liberando o anel")
                            self.anel.release()
                        if self.bufferElfo.estaVazio():
                            print("Elfo está destrancando a porta")
                            self.porta.release()

        def __bufferRenasCheio(self):
            return self.bufferRena.estaCheio()

        def __bufferElfosCheio(self):
            return self.bufferElfo.estaCheio()



    def __init__(self, papaiNoel=None, listaElfo=None, listaRena=None, tamanhoGrupoElfos=None):
        if not Controlador.instancia:
            Controlador.instancia = Controlador.__Controlador(papaiNoel, listaElfo, listaRena, tamanhoGrupoElfos)
    

    def ajuda(self):
        self.instancia.__ajuda()

    def adicionaBufferElfo(self, elfo):
        self.instancia.__adicionaBufferElfo(elfo)

    def adicionaBufferRena(self, rena):
        self.instancia.__adicionaBufferRena(rena)

    
    def ajudaRenas(self):
        return
    
    def ajudaElfos(self):
        self.instancia.__ajudaElfos()
        return
