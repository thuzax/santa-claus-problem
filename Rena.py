import threading
import time
from Controlador import Controlador


class Rena(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.estaDeFerias = False

    def run(self):
        print ("Starting " + self.name)
        controlador = Controlador()
        while True:
            if not self.estaDeFerias:
                controlador.adicionaBufferRena(self)
                time.sleep(2)
        print ("Exiting " + self.name)
    
    def amarraRena(self):
        print("Amarrando a rena " + str(self.name))
        time.sleep(0.1)
    
    def desamarraRena(self):
        print("Desamarando a rena " + str(self.name))
        time.sleep(0.1)
    
    def tiraFerias(self):
        print("A rena " + str(self.name) + " está tirando férias")
        self.estaDeFerias = True
    
    def terminouFerias(self):
        print("A rena " + str(self.name) + " acabou suas férias")
        self.estaDeFerias = False


    def descansa(self):
        time.sleep(1)
