import Indeces
import Movements
import Objects
import Cells

TANK_SIZE = 0.24625


class MappedGrid:
    def __init__(self, total_x, total_y):
        self.total_x = total_x
        self.total_y = total_y
        self.grid = [[Cells.Empty(x, y) for y in range(total_y)]
                     for x in range(total_x)]

        self.agent = Cells.Agent(2, 26)
        self.center = None
        # self.grid[2][26] = self.agent

    def update_up(self, perception):
        up_obj = perception[Indeces.NEIGHBORHOOD_UP]
        up_dist = perception[Indeces.NEIGHBORHOOD_DIST_UP]
        up_obj_x = self.agent.x
        up_obj_y = self.agent.y + up_dist + (1 - TANK_SIZE)
        self.put_obj_on_grid(up_obj, up_obj_x, up_obj_y)

    def update_down(self, perception):
        down_obj = perception[Indeces.NEIGHBORHOOD_DOWN]
        down_dist = perception[Indeces.NEIGHBORHOOD_DIST_DOWN]
        down_obj_x = self.agent.x
        down_obj_y = self.agent.y - down_dist - (1 - TANK_SIZE)
        self.put_obj_on_grid(down_obj, down_obj_x, down_obj_y)

    def update_right(self, perception):
        right_obj = perception[Indeces.NEIGHBORHOOD_RIGHT]
        right_dist = perception[Indeces.NEIGHBORHOOD_DIST_RIGHT]
        right_obj_x = self.agent.x + right_dist + (1 - TANK_SIZE)
        right_obj_y = self.agent.y
        self.put_obj_on_grid(right_obj, right_obj_x, right_obj_y)

    def update_left(self, perception):
        left_obj = perception[Indeces.NEIGHBORHOOD_LEFT]
        left_dist = perception[Indeces.NEIGHBORHOOD_DIST_LEFT]
        left_obj_x = self.agent.x - left_dist - (1 - TANK_SIZE)
        left_obj_y = self.agent.y
        self.put_obj_on_grid(left_obj, left_obj_x, left_obj_y)

    def update(self, perception):
        # actualizar el agente
        agent_x = perception[Indeces.AGENT_X]
        agent_y = perception[Indeces.AGENT_Y]

        self.agent.x = agent_x
        self.agent.y = agent_y
        self.agent.can_fire = perception[Indeces.CAN_FIRE]
        self.agent.health = perception[Indeces.HEALTH]

        # actualizar neighborhood up
        self.update_up(perception)

        # actualizar neighborhood down
        self.update_down(perception)

        # actualizar neighborhood right
        self.update_right(perception)

        # actualizar neighborhood left
        self.update_left(perception)

        # actualizar donde esta el command center
        center_x = int(perception[Indeces.COMMAND_CENTER_X])
        center_y = int(perception[Indeces.COMMAND_CENTER_Y])
        self.center = Cells.Center(center_x, center_y)
        self.grid[center_x][center_y] = self.center

    def put_obj_on_grid(self, object, x, y):
        print("x: ", x, "y: ", y)
        x = round(x)
        y = round(y)
        if object == Objects.NOTHING:
            self.grid[x][y] = Cells.Empty(x, y)
        elif object == Objects.UNBREAKABLE:
            self.grid[x][y] = Cells.Steel(x, y)
        elif object == Objects.BRICK:
            self.grid[x][y] = Cells.Brick(x, y)
        elif object == Objects.COMMAND_CENTER:
            center = Cells.Center(x, y)
            self.center = center
            self.grid[x][y] = center

    def get_next_agent_move(self):
        self.floodfill()

        neighbors = self.neighborhood(round(self.agent.x), round(self.agent.y))
        passable_neighbors = {k: v for k, v in neighbors.items() if v.cost != -1 and isinstance(
            v, Cells.Empty) or isinstance(v, Cells.Center) or isinstance(v, Cells.Brick)}
        if not passable_neighbors:
            print("No empty neighbors :(")
            return None
        direction = min(passable_neighbors.keys(),
                        key=lambda k: passable_neighbors[k].cost)
        if passable_neighbors[direction].cost < 0:
            print("Agent is blocked :(")
            return None
        return direction

    def floodfill(self):
        # Clear cost
        for col in self.grid:
            for cell in col:
                cell.cost = -1

        # A*
        q = [(self.center.x, self.center.y)]
        while q:
            source_x, source_y = q.pop(0)
            cost = self.grid[source_x][source_y].cost + 1
            neighbors = list(self.neighborhood(source_x, source_y).values())
            neighbors.sort(key=lambda n: n.cost)
            for n in neighbors:
                # if we should not floodfill, undefined cost
                if not (isinstance(n, Cells.Empty) or isinstance(n, Cells.Brick)):
                    continue
                x, y = n.x, n.y
                # if a cost is already applied to the neighbor, skip
                if self.grid[x][y].cost != -1:
                    continue
                self.grid[x][y].cost = cost
                q.append((x, y))

    def neighborhood(self, x, y):
        n = {}

        directions = {
            Movements.MOVE_UP: (0, 1),
            Movements.MOVE_LEFT: (-1, 0),
            Movements.MOVE_RIGHT: (1, 0),
            Movements.MOVE_DOWN: (0, -1),
        }

        for key, val in directions.items():
            dx, dy = val
            if not (0 <= x + dx < self.total_x):
                continue
            if not (0 <= y + dy < self.total_y):
                continue

            n[key] = self.grid[x + dx][y + dy]

        return n

    def __repr__(self):
        s = ""
        s += "+" + "-"*(2*self.total_y-1) + "+\n"
        for y in range(self.total_y - 1, -1, -1):
            s += "|"
            for x in range(len(self.grid[0])):
                s += str(self.grid[x][y]) + " "
            s = s[:-1]
            s += "|\n"
        s += "+" + "-"*(2*self.total_y-1) + "+"
        return s
