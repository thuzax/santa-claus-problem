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
        print(c1.instancia)
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
    
    def acorda(self):
        self.dormindo = False
    
    def dormindo(self):
        self.dormindo = True


