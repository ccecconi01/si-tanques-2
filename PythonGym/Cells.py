
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = -1


class Empty(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "."


class Steel(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "#"


class Brick(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "@"


class Center(Cell):
    def __init__(self, x, y, health=1):
        super().__init__(x, y)
        self.cost = 0

    def __repr__(self):
        return "C"


class Player(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "P"


class Shell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "#"


class Other(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return "#"


class Agent(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.can_fire = True
        self.health = 10

    def __repr__(self):
        return "A"
