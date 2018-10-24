import threading
import time

from Controlador import Controlador


class PapaiNoel (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.dormindo = True

    def run(self):
        controlador = Controlador()
        while True:
            if(not self.dormindo):
                controlador.ajuda()
            
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
    
    def acorda(self):
        self.dormindo = False
    
    def dorme(self):
        self.dormindo = True

    def ajudaRenas(self):
        print("Ajudando as renas")
        time.sleep(1)
    
    def ajudaElfos(self):
        print("Ajudando os elfos")
        time.sleep(1)

    def estaAcordado(self):
        return (not self.dormindo)
    
    def distribuiBrinquedos(self):
        print("O papai noel está distribuindo brinquedos...")
        time.sleep(3)