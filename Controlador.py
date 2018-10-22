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
        
        def adicionaBufferElfo(self, elfo):
            if not self.porta.locked():
                self.porta.acquire()
                if not self.anel.locked():
                    self.anel.acquire()
                    self.contadorElfo += 1
                    if self.contadorElfo == self.bufferElfo.getTamanho():
                        self.papaiNoel.acorda()
                    else:
                        self.porta.release()
                    self.anel.release()
                    self.bufferElfo.insere(elfo)
        
        def adicionaBufferRena(self, rena):
            if not self.porta.locked():
                self.porta.acquire()
                if not self.anel.locked():
                    self.anel.acquire()
                    self.contadorRena += 1
                    if self.contadorRena == self.bufferRena.getTamanho():
                        self.papaiNoel.acorda()
                    else:
                        self.porta.release()
                    self.anel.release()
                    self.bufferRena.insere(rena)
        

    def __init__(self, papaiNoel=None, listaElfo=None, listaRena=None, tamanhoGrupoElfos=None):
        if not Controlador.instancia:
            Controlador.instancia = Controlador.__Controlador(papaiNoel, listaElfo, listaRena, tamanhoGrupoElfos)
