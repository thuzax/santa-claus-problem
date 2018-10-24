from Controlador import Controlador
import threading
import time
import random

class Elfo(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        # time.sleep(random.random()/10)
        print ("Starting " + self.name)
        controlador = Controlador()
        while True:
            controlador.adicionaBufferElfo(self)
            time.sleep(2)
        print ("Exiting " + self.name)

    def obtemAjuda(self):
        # print("Elfo " + str(self.threadID) + " obtendo ajuda")
        time.sleep(0.8)