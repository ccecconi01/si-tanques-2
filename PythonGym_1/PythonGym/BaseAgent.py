import random
import time

# Indices de perception
NEIGHBORHOOD_UP = 0
NEIGHBORHOOD_DOWN = 1
NEIGHBORHOOD_RIGHT = 2
NEIGHBORHOOD_LEFT = 3
NEIGHBORHOOD_DIST_UP = 4
NEIGHBORHOOD_DIST_DOWN = 5
NEIGHBORHOOD_DIST_RIGHT = 6
NEIGHBORHOOD_DIST_LEFT = 7
PLAYER_X = 8
PLAYER_Y = 9
COMMAND_CENTER_X = 10
COMMAND_CENTER_Y = 11
AGENT_X = 12
AGENT_Y = 13
CAN_FIRE = 14
HEALTH = 15

# Objetos detectados
NOTHING = 0
UNBREAKABLE = 1
BRICK = 2
COMMAND_CENTER = 3
PLAYER = 4
SHELL = 5
OTHER = 6

# Movimientos
NOTHING = 0
MOVE_UP = 1
MOVE_DOWN = 2
MOVE_RIGHT = 3
MOVE_LEFT = 4

class BaseAgent:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    #Devuelve el nombre del agente
    def Name(self):
        return self.name
    #Devuelve el id del agente
    def Id(self):
        return self.id
    #Metodo que se llama al iniciar el agente. No devuelve nada y sirve para contruir el agente
    def Start(self):
        print("Inicio del agente ")

    #Metodo que se llama en cada actualización del agente, y se proporciona le vector de percepciones
    #Devuelve la acción u el disparo si o no
    def Update(self, perception):
        print("Toma de decisiones del agente")
        print(perception)
        action = random.randint(0,4)
        return action, True
    
    #Metodo que se llama al finalizar el agente, se pasa el estado de terminacion
    def End(self, win):
        print("Agente finalizado")
        print("Victoria ",win)