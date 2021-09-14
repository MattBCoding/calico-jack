# boat file to contain boat class
class Boat:
    '''
    Constructor for Boat objects holds details
    such as name, location, health, orientation
    '''
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.x = None
        self.y = None
        self.orientation = None
        self.health = length
        self.location = []

    def set_position(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
        width = 1
        height = 1
        if self.orientation == 'h':
            width = self.length
        else:
            height = self.length

        for r in range(width):
            for u in range(height):
                self.location.append([self.x + u, self.y + r])
