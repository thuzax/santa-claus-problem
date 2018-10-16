import threading
import time


class PapaiNoel (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.dormindo = False


    def run(self):
        print ("Starting " + self.name)
        print ("Exiting " + self.name)

