import random

from pprint import pprint

import Indeces
import Objects
import Movements
# from MappedGrid import MappedGrid


class BaseAgent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.can_fire = True
        # self.mapped_grid = MappedGrid(28, 28)

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
        self.print_perception(perception)
        self.can_fire = perception[Indeces.CAN_FIRE]

        # actualizar mapped_grid con la informacion nueva
        # self.mapped_grid.update(perception)
        # print(self.mapped_grid)

        print("Toma de decisiones del agente")
        action, fire = self.decide_action(perception)
        return action, fire

    def decide_action(self, perception):
        neighborhood = [Indeces.NEIGHBORHOOD_UP, Indeces.NEIGHBORHOOD_DOWN,
                        Indeces.NEIGHBORHOOD_RIGHT, Indeces.NEIGHBORHOOD_LEFT]

        should_shoot = [Objects.COMMAND_CENTER, Objects.BRICK, Objects.SHELL]

        move_action = {
            Indeces.NEIGHBORHOOD_UP: Movements.MOVE_UP,
            Indeces.NEIGHBORHOOD_DOWN: Movements.MOVE_DOWN,
            Indeces.NEIGHBORHOOD_LEFT: Movements.MOVE_LEFT,
            Indeces.NEIGHBORHOOD_RIGHT: Movements.MOVE_RIGHT,
        }

        # Atirar jugador, bala, cc o ladrillos en su direcion si podemos
        for neighbor in neighborhood:
            if self.can_fire and perception[neighbor] in should_shoot:
                return move_action[neighbor], True

        # Coger x,y de cc y agente
        cc_x = perception[Indeces.COMMAND_CENTER_X]
        cc_y = perception[Indeces.COMMAND_CENTER_Y]
        agent_x = perception[Indeces.AGENT_X]
        agent_y = perception[Indeces.AGENT_Y]

        # Mover hacia cc
        if cc_x > agent_x:
            return Movements.MOVE_RIGHT, False
        if cc_x < agent_x:
            return Movements.MOVE_LEFT, False
        if cc_y > agent_y:
            return Movements.MOVE_UP, False
        if cc_y < agent_y:
            return Movements.MOVE_DOWN, False
        return Movements.NOTHING, False

    def print_perception(self, perception):
        labels = ["NEIGHBORHOOD_UP",
                  "NEIGHBORHOOD_DOWN",
                  "NEIGHBORHOOD_RIGHT",
                  "NEIGHBORHOOD_LEFT",
                  "NEIGHBORHOOD_DIST_UP",
                  "NEIGHBORHOOD_DIST_DOWN",
                  "NEIGHBORHOOD_DIST_RIGHT",
                  "NEIGHBORHOOD_DIST_LEFT",
                  "PLAYER_X",
                  "PLAYER_Y",
                  "COMMAND_CENTER_X",
                  "COMMAND_CENTER_Y",
                  "AGENT_X",
                  "AGENT_Y",
                  "CAN_FIRE",
                  "HEALTH",]

        pprint(list(zip(labels, perception)))
    # Metodo que se llama al finalizar el agente, se pasa el estado de terminacion

    def End(self, win):
        print("Agente finalizado")
        print("Victoria ", win)
