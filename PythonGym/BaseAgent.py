import random
import time

from pprint import pprint

import Indeces
import Movements
import Objects
from MappedGrid import MappedGrid


class BaseAgent:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mapped_grid = MappedGrid(28, 28)
        self.old_movement = None
        self.old_agent_position = (None, None)

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

        # actualizar current agent position
        current_agent_position = (
            perception[Indeces.AGENT_X], perception[Indeces.AGENT_Y])

        # actualizar el modelo con la informacion nueva
        self.mapped_grid.update(perception)
        print(self.mapped_grid)

        neighborhood_move = {
            Indeces.NEIGHBORHOOD_UP: Movements.MOVE_UP,
            Indeces.NEIGHBORHOOD_DOWN: Movements.MOVE_DOWN,
            Indeces.NEIGHBORHOOD_LEFT: Movements.MOVE_LEFT,
            Indeces.NEIGHBORHOOD_RIGHT: Movements.MOVE_RIGHT,
        }

        should_shoot = [Objects.PLAYER, Objects.COMMAND_CENTER, Objects.SHELL, Objects.OTHER]

        # Atirar centro de comando, bala o jugador en su direcion si lo vemos
        for neighbor, movement in neighborhood_move.items():
            if perception[Indeces.CAN_FIRE] and perception[neighbor] in should_shoot:
                self.old_movement = movement
                self.old_agent_position = current_agent_position
                return movement, True

        # Toma decicion para acercarse al centro de comando via floodfill
        floodfill_movement = self.mapped_grid.get_next_agent_move()

        # Si quedamos atrapados o floodfill no devuleva movement, movimiento aleatorio
        same_movement = self.old_movement == floodfill_movement
        same_x_position = self.old_agent_position[0] == current_agent_position[0]
        same_y_position = self.old_agent_position[1] == current_agent_position[1]
        same_position = same_x_position and same_y_position
        if (same_movement and same_position) or floodfill_movement == None:
            random_movement = random.choice(list(neighborhood_move.values()))
            self.old_movement = random_movement
            self.old_agent_position = current_agent_position
            return random_movement, True

        # devolver el movement de floodfill
        self.old_movement = floodfill_movement
        self.old_agent_position = current_agent_position
        return floodfill_movement, True

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

        for label, val in zip(labels, perception):
            print(label, val)

    # Metodo que se llama al finalizar el agente, se pasa el estado de terminacion
    def End(self, win):
        print("Agente finalizado")
        print("Victoria ", win)
