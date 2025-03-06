import Indeces
import Objects
import Cells


class MappedGrid:
    def __init__(self, total_x, total_y):
        self.total_x = total_x
        self.total_y = total_y
        self.grid = [[Cells.Empty(x, y) for x in range(total_x)]
                     for y in range(total_y)]

        self.agent = Cells.Agent(0, 0)

    def update(self, perception):
        # actualizar neighborhood up
        up_obj = perception[Indeces.NEIGHBORHOOD_UP]
        up_dist = perception[Indeces.NEIGHBORHOOD_DIST_UP]
        up_obj_x = self.agent.x
        up_obj_y = self.agent.y - up_dist
        self.put_obj_on_grid(up_obj, up_obj_x, up_obj_y)

        # actualizar neighborhood down
        down_obj = perception[Indeces.NEIGHBORHOOD_DOWN]
        down_dist = perception[Indeces.NEIGHBORHOOD_DIST_DOWN]
        down_obj_x = self.agent.x
        down_obj_y = self.agent.y + down_dist
        self.put_obj_on_grid(down_obj, down_obj_x, down_obj_y)

        # actualizar neighborhood right
        right_obj = perception[Indeces.NEIGHBORHOOD_RIGHT]
        right_dist = perception[Indeces.NEIGHBORHOOD_DIST_RIGHT]
        right_obj_x = self.agent.x + right_dist
        right_obj_y = self.agent.y
        self.put_obj_on_grid(right_obj, right_obj_x, right_obj_y)

        # actualizar neighborhood left
        left_obj = perception[Indeces.NEIGHBORHOOD_LEFT]
        left_dist = perception[Indeces.NEIGHBORHOOD_DIST_LEFT]
        left_obj_x = self.agent.x - left_dist
        left_obj_y = self.agent.y
        self.put_obj_on_grid(left_obj, left_obj_x, left_obj_y)

        # actualizar donde esta el player
        player_x = int(perception[Indeces.PLAYER_X])
        player_y = int(perception[Indeces.PLAYER_Y])
        self.grid[player_x][player_y] = Cells.Player(player_x, player_y)

        # actualizar donde esta el command center
        center_x = int(perception[Indeces.COMMAND_CENTER_X])
        center_y = int(perception[Indeces.COMMAND_CENTER_Y])
        self.grid[center_x][center_y] = Cells.Center(center_x, center_y)

        # actualizar el agente
        # self.grid[self.agent.x][self.agent.y] = Cells.Empty(
            # self.agent.x, self.agent.y)

        agent_x = int(perception[Indeces.AGENT_X])
        agent_y = int(perception[Indeces.AGENT_Y])
        self.grid[agent_x][agent_y] = self.agent

        self.agent.x = agent_x
        self.agent.y = agent_y
        self.agent.can_fire = perception[Indeces.CAN_FIRE]
        self.agent.health = perception[Indeces.HEALTH]

    def put_obj_on_grid(self, object, x, y):
        x = int(x)
        y = int(y)
        if object == Objects.NOTHING:
            self.grid[x][y] = Cells.Empty(x, y)
        elif object == Objects.UNBREAKABLE:
            self.grid[x][y] = Cells.Steel(x, y)
        elif object == Objects.BRICK:
            self.grid[x][y] = Cells.Brick(x, y)
        elif object == Objects.COMMAND_CENTER:
            self.grid[x][y] = Cells.Center(x, y)
        elif object == Objects.PLAYER:
            self.grid[x][y] = Cells.Player(x, y)
        elif object == Objects.SHELL:
            self.grid[x][y] = Cells.Shell(x, y)
        elif object == Objects.OTHER:
            self.grid[x][y] = Cells.Other(x, y)

    def __repr__(self):
        s = ""
        s += "+" + "-"*(2*self.total_y-1) + "+\n"
        for y in range(len(self.grid)):
            s += "|"
            for x in range(len(self.grid[0])):
                s += str(self.grid[x][self.total_y - y - 1]) + " "
            s = s[:-1]
            s += "|\n"
        s += "+" + "-"*(2*self.total_y-1) + "+"
        return s
