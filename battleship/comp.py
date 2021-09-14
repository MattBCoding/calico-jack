# comp file to contain comp class
from battleship.board import Board
import random
import string


class Comp:
    '''
    AI player - controls shot selection
    setting ship locations
    difficulty algorithms
    '''

    def __init__(self, name, dimensions, difficulty):
        self.name = name
        self.dimensions = dimensions
        self.board = Board(dimensions)
        self.difficulty = difficulty
        self.ships = []
        self.previous_shots = []
        self.hit_counter = 0
        self.last_shot_hit = False
        self.target_list = []

    def generate_easy_shot(self):
        alpha = list(string.ascii_letters[:self.dimensions])
        shot = None
        x = 0
        while x < 1:
            coords = [random.choice(alpha),
                      random.randint(0, (self.dimensions - 1))]
            shot = [(ord(coords[0].upper()) - 65), int(coords[1])]
            if shot in self.previous_shots:
                continue
            else:
                self.previous_shots.append(shot)
                x += 1
        return shot

    def generate_normal_shot(self):
        if self.last_shot_hit:
            neighbours = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for x, y in neighbours:
                last = self.previous_shots[-1]
                temp = [last[0] + x, last[1] + y]
                if (temp[0] >= 0 and temp[0] < self.dimensions):
                    if (temp[1] >= 0 and temp[1] < self.dimensions):
                        if temp not in self.previous_shots:
                            self.target_list.append(temp)
            shot = self.target_list[0]
            self.previous_shots.append(shot)
            self.target_list.pop(0)
            return shot
        elif len(self.target_list) > 0:
            shot = self.target_list[0]
            self.previous_shots.append(shot)
            self.target_list.pop(0)
            return shot
        else:
            shot = self.generate_easy_shot()
            return shot

    # x is each row, x + 1 moves down one row
    # y is each column within a row, y + 1 moves right one column
    def does_ship_fit(self, length, x, y, orientation, game):
        miss_or_hit = ('\x1b[93mM\x1b[0m', '\x1b[91m#\x1b[0m')
        if orientation == 'v':
            if x + length <= self.dimensions:
                # check each tile for a miss or hit marker for length of ship
                for i in range(x, x + length):
                    if game.player.board.board[i][y] in miss_or_hit:
                        return False
                return True
            else:
                return False
        # if not 'v'ertical must be horizontal
        else:
            if y + length <= self.dimensions:
                # check each tile for a miss or hit market for length of ship
                for i in range(y, y + length):
                    if game.player.board.board[x][i] in miss_or_hit:
                        return False
                return True
            else:
                return False

    def find_rest_of_ship(self, x, y, game):
        miss_or_hit = ('\x1b[93mM\x1b[0m', '\x1b[91m#\x1b[0m')
        neighbours = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        temp = []
        for a, d in neighbours:
            if (x + a >= 0 and x + a < self.dimensions):
                if (y + d >= 0 and y + d < self.dimensions):
                    if (game.player.board.board[x + a][y + d]
                       not in miss_or_hit):
                        temp.append([x + a, y + d])
        return temp

    def generate_hard_shot(self, game):
        self.probability_list = [[0 for y in range(self.dimensions)]
                                 for x in range(self.dimensions)]
        max_value = 0
        location = [0, 0]
        miss_or_hit = ('\x1b[93mM\x1b[0m', '\x1b[91m#\x1b[0m')
        for x in range(self.dimensions):
            for y in range(self.dimensions):
                for ship in game.player.ships:
                    if ship.health > 0:
                        # check if ship fits for each tile
                        if self.does_ship_fit(ship.length, x, y, 'v', game):
                            for i in range(x, x + ship.length):
                                self.probability_list[i][y] += 1
                        # add 1 to each tile ship would take
                        # do for vertical and horizontal orientations
                        if self.does_ship_fit(ship.length, x, y, 'h', game):
                            for i in range(y, y + ship.length):
                                self.probability_list[x][i] += 1
        # check for hits - update list for surrounding tiles
        for x in range(self.dimensions):
            for y in range(self.dimensions):
                if game.player.board.board[x][y] == '\x1b[91m#\x1b[0m':
                    temp = self.find_rest_of_ship(x, y, game)
                    for x, y in temp:
                        self.probability_list[x][y] += 100
        for x in range(self.dimensions):
            for y in range(self.dimensions):
                if ((self.probability_list[x][y] > max_value)
                   and (self.probability_list[x][y] not in miss_or_hit)):
                    max_value = self.probability_list[x][y]
                    location = [x, y]
        return location

    def get_target_from_comp(self, game):
        if self.difficulty == 'e':
            shot = self.generate_easy_shot()
            game.turn_loop(self, shot)
        elif self.difficulty == 'n':
            shot = self.generate_normal_shot()
            game.turn_loop(self, shot)
        elif self.difficulty == 'h':
            shot = self.generate_hard_shot(game)
            game.turn_loop(self, shot)

    def place_ships(self, game):
        for ship in self.ships:
            self.position_ship(ship, game)

    def position_ship(self, ship, game):
        alpha = list(string.ascii_letters[:self.dimensions])
        option = ['h', 'v']
        coords = [random.choice(alpha),
                  random.randint(0, (self.dimensions - 1))]
        while True:
            if self.board.can_ship_be_placed(coords, ship) == 1:
                orientation = random.choice(option)
                self.add_ship(ship, coords, orientation, game)
                break
            elif self.board.can_ship_be_placed(coords, ship) == 2:
                orientation = 'h'
                self.add_ship(ship, coords, orientation, game)
                break
            elif self.board.can_ship_be_placed(coords, ship) == 3:
                orientation = 'v'
                self.add_ship(ship, coords, orientation, game)
                break
            elif self.board.can_ship_be_placed(coords, ship) == 4:
                orientation = 'h'
                self.add_ship(ship, coords, orientation, game)
                break
            elif self.board.can_ship_be_placed(coords, ship) == 5:
                coords = [random.choice(alpha),
                          random.randint(0, (self.dimensions - 1))]
                pass
            elif self.board.can_ship_be_placed(coords, ship) == 6:
                orientation = 'v'
                self.add_ship(ship, coords, orientation, game)
                break
            elif self.board.can_ship_be_placed(coords, ship) == 7:
                coords = [random.choice(alpha),
                          random.randint(0, (self.dimensions - 1))]
                pass
            elif self.board.can_ship_be_placed(coords, ship) == 8:
                coords = [random.choice(alpha),
                          random.randint(0, (self.dimensions - 1))]
                pass

    def add_ship(self, ship, coords, orientation, game):
        x = (ord(coords[0].upper()) - 65)
        y = int(coords[1])
        ship.set_position(x, y, orientation)
        self.board.set_ship_position(ship)
