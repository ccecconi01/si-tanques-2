import random
import time

from MappedGrid import MappedGrid


class BaseAgent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mapped_grid = MappedGrid(26, 26)

    # Devuelve el nombre del agente
    def Name(self):
        return self.name
    # Devuelve el id del agente

    def Id(self):
        return self.id
    # Metodo que se llama al iniciar el agente. No devuelve nada y sirve para contruir el agente

    def Start(self):
        print("Inicio del agente ")

    # Metodo que se llama en cada actualización del agente, y se proporciona le vector de percepciones
    # Devuelve la acción u el disparo si o no
    def Update(self, perception):

        # actualizar mapped_grid con la informacion nueva
        self.mapped_grid.update(perception)
        print(self.mapped_grid)

        print("Toma de decisiones del agente")
        print(perception)
        action = random.randint(0, 4)
        return action, False

    # Metodo que se llama al finalizar el agente, se pasa el estado de terminacion
    def End(self, win):
        print("Agente finalizado")
        print("Victoria ", win)
