import threading
import time

from PapaiNoel import PapaiNoel
from Elfo import Elfo
from Rena import Rena
from Controlador import Controlador

QUANTIDADE_ELFOS = 10
QUANTIDADE_RENAS = 9
TAMANHO_GRUPO_ELFOS = 3

def main():
    idThread = 0
    papaiNoel = PapaiNoel(idThread, "Papai Noel")

    listaElfo = []
    for j in range(0, QUANTIDADE_ELFOS):
        elfo = Elfo(idThread, "Elfo" + str(j))
        listaElfo.append(elfo)
        idThread += 1

    listaRena = []
    for j in range(0, QUANTIDADE_RENAS):
        elfo = Rena(idThread, "Rena" + str(j))
        idThread += 1
        listaRena.append(elfo)

    controlador = Controlador(papaiNoel, listaElfo, listaRena, TAMANHO_GRUPO_ELFOS)
    controlador.start()

main()