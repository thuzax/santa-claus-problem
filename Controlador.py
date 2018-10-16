from Buffer import Buffer

class Controlador:

    def __init__(self, papaiNoel, listaElfo, listaRena, tamanhoGrupoElfos):
        self.listaRena = listaRena
        self.listaElfo = listaElfo
        self.papaiNoel = papaiNoel
        self.bufferElfo = Buffer(tamanhoGrupoElfos)
        self.bufferRena = Buffer(len(self.listaRena))

    def start(self):
        self.papaiNoel.start()

        for elfo in self.listaElfo:
            elfo.start()

        for rena in self.listaRena:
            rena.start()

    