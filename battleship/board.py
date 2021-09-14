# board file to contain board class
class Board:
    '''
    Creates and manages the playing boards,
    methods include placing ships on the board
    along with checking ships will fit and don't
    collide with other ships during placement.
    '''

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.board = [
            ["~" for i in range(dimensions)] for i in range(dimensions)
            ]

    def turn_into_blank_board(self):
        self.board = [
            ["_" for i in range(self.dimensions)]
            for i in range(self.dimensions)
        ]

    def on_board_test(self, coords, game):
        row_test = ((ord(coords[0].upper()) - 65) < self.dimensions)
        column_test = (int(coords[1]) < self.dimensions)
        if(row_test and column_test):
            return True
        else:
            return False

    def can_ship_be_placed(self, coords, ship):
        '''
    checks if ship can be placed horizontally and/or vertically
    on the board. checks will ship fit, then checks if something
    already there.
    parameters: self is board being checked, coords is starting location
    ship is the ship being checked, gives access to length.
        '''

        # convert row coord value into int to perform checks
        row_coord_value = (ord(coords[0].upper()) - 65)
        # convert column coord value into int to perform checks
        column_coord_value = int(coords[1])
        # holding list to check space against
        clear_space_vertical = []
        clear_space_horizontal = []
        # vertical orientation from row check
        vertical_check = (self.dimensions - row_coord_value - ship.length >= 0)
        # horizontal orientation from column check
        horizontal_check = (self.dimensions
                            - column_coord_value
                            - ship.length >= 0)
        # Check board to see if locations are clear
        if horizontal_check:
            if vertical_check:
                # Ship fits both horizontally and vertically
                # horizontal clear
                i = 0
                while i < ship.length:
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_horizontal.append((row_coord_value,
                                                      column_coord_value))
                        column_coord_value += 1
                        i += 1
                    else:
                        column_coord_value += 1
                        i += 1
                # vertical clear
                j = 0
                # reset values back to original after while loop
                row_coord_value = (ord(coords[0].upper()) - 65)
                column_coord_value = int(coords[1])
                while j < ship.length:
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_vertical.append((row_coord_value,
                                                    column_coord_value))
                        row_coord_value += 1
                        j += 1
                    else:
                        row_coord_value += 1
                        j += 1

                if ship.length == len(clear_space_horizontal):
                    if ship.length == len(clear_space_vertical):
                        return 1
                    else:
                        return 2
                elif ship.length == len(clear_space_vertical):
                    return 3
                else:
                    return 8

            else:
                # Ship fits horizontally but not vertically
                i = 0
                while i < ship.length:
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_horizontal.append((row_coord_value,
                                                      column_coord_value))
                        column_coord_value += 1
                        i += 1
                    else:
                        column_coord_value += 1
                        i += 1
                if ship.length == len(clear_space_horizontal):
                    return 4
                else:
                    return 5

        else:
            if vertical_check:
                # ship fits vertically but not horizontally
                i = 0
                while i < ship.length:
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_vertical.append((row_coord_value,
                                                    column_coord_value))
                        row_coord_value += 1
                        i += 1
                    else:
                        row_coord_value += 1
                        i += 1
                if ship.length == len(clear_space_vertical):
                    return 6
                else:
                    return 7
            else:
                return 8

    def set_ship_position(self, ship):
        for tile in ship.location:
            self.board[tile[0]][tile[1]] = 'S'
