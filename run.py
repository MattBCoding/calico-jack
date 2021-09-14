# import required modules here
import math
import random
import string
import time
import os
# python code goes here
'''
NOTE to self
added this line so could push the movement of assets directory
possibly move some classes to other files to make things easier to find

'''


def clear_terminal():
    """
    Clears the terminal window prior to new content.
    Original code from
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    Recommended to me by Goran Sigeskog
    https://github.com/gorsig
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class C:
    END = '\33[0m'
    RED = '\33[91m'
    YELLOW = '\33[93m'
    BGBLUE = '\33[44m'


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


class Player:
    '''
    Player object controls inputs from user
    for shots, ship placement. Stores details
    such as ships in fleet, previous hits
    links ships player and board
    '''

    def __init__(self, name, dimensions):
        self.name = name
        self.board = Board(dimensions)
        self.ships = []
        self.previous_shots = []
        self.hit_counter = 0

    def get_target_from_user(self, game):
        x = 0
        shot = None
        try:
            while x < 1:
                user_target = input('''
What are your orders? Where do you want to target?
Select the location in the format of row then column e.g. 'E4':\n''')
                if user_target == '':
                    raise TypeError
                else:
                    user_target_coords_list = list(user_target)
                # check input is correct length
                    if len(user_target_coords_list) != 2:
                        raise Exception
                    elif (not user_target_coords_list[0].isalpha()
                            or not user_target_coords_list[1].isdigit()):
                        raise Exception
                    # check target is a valid on board location
                    elif (self.board.on_board_test(user_target_coords_list,
                                                   game)) is False:
                        clear_terminal()
                        game.print_blank_and_player_boards()
                        print('''
The location entered is not on the board! Try again!
Are you trying to hit their ships or the mainland?''')
                    elif self.board.on_board_test(user_target_coords_list,
                                                  game):
                        a = (ord(user_target_coords_list[0].upper()) - 65)
                        b = int(user_target_coords_list[1])
                        shot = [a, b]
                        while True:
                            try:
                                if shot in self.previous_shots:
                                    raise Exception
                                else:
                                    self.previous_shots.append(shot)
                                    x += 1
                                    break
                            except Exception:
                                clear_terminal()
                                game.print_blank_and_player_boards()
                                print('''
You have already fired there, are you trying to waste our Cannonballs?
You better get your head in the game pirate, lets try this again!''')
                            break
        except TypeError:
            clear_terminal()
            game.print_blank_and_player_boards()
            print('''
You have to choose a target location! Waving the white flag will just
get your head to the gallows sooner. Try again, it needs to be in the format
of 'E4' letter then number, no spaces, no dashes, no second chances!\n''')
            self.get_target_from_user(game)
        except Exception:
            clear_terminal()
            game.print_blank_and_player_boards()
            print('''
We've been through this already, it needs to be in the format of 'E4'
Letter then Number, this is not a time to act the fool, try again! ''')
            self.get_target_from_user(game)
        game.turn_loop(self, shot)

    def get_position_from_user(self, player, comp, game):
        game.print_player_board()
        input('''
Now we need to position our ships ready for battle! Are ye ready?
Press 'Enter' to start!\n''')
        for ship in self.ships:
            self.position_ship(ship, game)
        print('''
THERE HERE!!! THERE HERE!!! MAN THE CANNONS!!!
Wait?? Where is everyone?? You'll have to fight them on your own while I
go and wake that drunken rabble up! Do not let Calico Jack down!\n''')
        time.sleep(3)
        game.comp_setup()

    def position_ship(self, ship, game):
        while True:
            try:
                # display message informing user on next ship to be placed
                # name and size
                user_input_coords = input(f'''
Please select the starting location for your {ship.name}, it is
{ship.length} tiles long, in the format of row then column e.g. 'E4':\n''')
                # convert input to list
                user_input_coords_list = list(user_input_coords)
                # check input is the correct length
                if len(user_input_coords_list) != 2:
                    raise Exception
                # check input is in the correct format letter then number
                elif (not user_input_coords_list[0].isalpha()
                        or not user_input_coords_list[1].isdigit()):
                    raise Exception
                # input validation of starting location for next ship
                # need to check if input is valid board coords.
                elif (self.board.on_board_test(user_input_coords_list, game)
                      ) is False:
                    clear_terminal()
                    game.print_player_board()
                    print('''
The location entered is not on the board. Try again!
Remembering the correct format e.g. E4 letter then number.''')
                elif self.board.on_board_test(user_input_coords_list, game):
                    # now need to check if ship can be placed Hor or Ver
                    if self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 1:
                        try:
                            orientation = input('''
Would you like to place this ship horizontally, left to right
or vertically, downwards from starting location?
Enter 'H' for horizontally, 'V' for vertically:\n''').lower()
                            if (orientation != 'h') and (orientation != 'v'):
                                raise Exception
                            else:
                                self.add_ship(ship, user_input_coords_list,
                                              orientation, game)
                                break
                        except Exception:
                            clear_terminal()
                            game.print_player_board()
                            print('''
It can only be 'H' for horizontally or 'V' for vertically
There are no other options, try again!''')
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 2:
                        orientation = 'h'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 3:
                        orientation = 'v'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 4:
                        orientation = 'h'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 5:
                        clear_terminal()
                        game.print_player_board()
                        print('''
Can not place ship, only option from this location is horizontal
which would hit another ship. Try a different location''')
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 6:
                        orientation = 'v'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        print('''
Ship can only be placed vertically, so we placed it.''')
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 7:
                        clear_terminal()
                        game.print_player_board()
                        print('''
Can not place ship, only option from this location is vertical
which would hit another ship. Try a different location\n''')
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 8:
                        clear_terminal()
                        game.print_player_board()
                        print('''
Can not place ship, it will not fit either horizontally or
vertically at this location. Try a different location\n''')
                else:
                    raise Exception
# display error message - repeat user input
            except Exception:
                clear_terminal()
                game.print_player_board()
                print('''
The starting location needs to be entered in the format of row then
column, e.g. 'F4' or 'A2' a letter followed by a number, no spaces, dashes,
dots or bottles of rum before after or in the middle. Try again!''')

    def add_ship(self, ship, coords, orientation, game):
        x = (ord(coords[0].upper()) - 65)
        y = int(coords[1])
        ship.set_position(x, y, orientation)
        self.board.set_ship_position(ship)
        game.print_player_board()


# create blanked out version of board to display in game
class Blank:
    '''
    class to hold a blank board to display to player
    blank board will reference comp board to determine if
    a ship has been hit. Used for targetting
    '''

    def __init__(self, dimensions, opponent):
        self.dimensions = dimensions
        self.board = Board(dimensions)
        self.reference_board = opponent.board
        self.board.turn_into_blank_board()


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


class Game:
    '''
    game instance, controls player turns
    displays information to user
    prints boards to screen
    '''

    def __init__(self, dimensions, player, comp, blank):
        self.dimensions = dimensions
        self.player = player
        self.comp = comp
        self.blank = blank
        self.scoreboard = []

# setup the winning condition
    def win_needs(self, hits):
        self.to_win = hits

# check for a win
    def check_for_win(self, whichplayer):
        if whichplayer.hit_counter == self.to_win:
            return True
        else:
            return False

# end game and declare winner
    def end_game(self, whichplayer):
        clear_terminal()
        print("\n\n\n\n\n\n\n\n")
        print(C.RED + '#' * 80 + C.END)
        print(C.RED + '#' * 80 + C.END)
        print(C.RED + '#' + ' ' * 78 + '#' + C.END)
        print(C.RED + '#' + ' ' * 78 + '#' + C.END)
        if whichplayer == self.player:
            print(C.RED + '#' + ' ' * 35 + 'You Win!' + ' ' * 35 + '#' + C.END)
        else:
            print(C.RED + '#' + ' ' * 35 + 'You Lose!' + ' ' * 34 + '#'
                  + C.END)
        print(C.RED + '#' + ' ' * 78 + '#' + C.END)
        print(C.RED + '#' + ' ' * 78 + '#' + C.END)
        print(C.RED + '#' * 80 + C.END)
        print(C.RED + '#' * 80 + C.END)
        print('\n\n\n\n')
        again = 'N'
        while again == 'N':
            try:
                again = input('''Would you like to play again me 'arty?
    (enter 'Y' to play or 'N' to quit):\n''').lower()
                if (again != 'y') and (again != 'n'):
                    raise Exception()
                elif again == "n":
                    print('''
        Goodbye''')
                    quit()
            except Exception:
                print('''
        Argh! all that for nothin... I should make ye walk the plank...
        Wait, shall we try that again?\n''')
                again = 'N'
        setup()

    def create_scoreboard(self):
        player_pinnace = 0
        player_sloop = 0
        player_schooner = 0
        player_lugger = 0
        player_brigantine = 0
        comp_pinnace = 0
        comp_sloop = 0
        comp_schooner = 0
        comp_lugger = 0
        comp_brigantine = 0
        if self.dimensions == 6:
            for ship in self.player.ships:
                if ship.name == 'Schooner':
                    if ship.health > 0:
                        player_schooner = 1
                    else:
                        player_schooner = 0
                elif ship.name == 'Lugger':
                    if ship.health > 0:
                        player_lugger = 1
                    else:
                        player_lugger = 0
                elif ship.name == 'Brigantine':
                    if ship.health > 0:
                        player_brigantine = 1
                    else:
                        player_brigantine = 0
            for ship in self.comp.ships:
                if ship.name == 'Schooner':
                    if ship.health > 0:
                        comp_schooner = 1
                    else:
                        comp_schooner = 0
                elif ship.name == 'Lugger':
                    if ship.health > 0:
                        comp_lugger = 1
                    else:
                        comp_lugger = 0
                elif ship.name == 'Brigantine':
                    if ship.health > 0:
                        comp_brigantine = 1
                    else:
                        comp_brigantine = 0

            self.scoreboard = [
                              ['   C.J', 'ACK', '   ', 'J.B', 'ARN', 'ET  '],
                              ['      ', ' SH', 'IPS', ' LE', 'FT ', '    '],
                              ['    ' + str(player_schooner) + ' ', '  S',
                               'CHO', 'ONE', 'R  ', ' ' + str(comp_schooner)
                               + '  '],
                              ['    ' + str(player_lugger) + ' ', '   ', 'LUG',
                               'GER', '   ', ' ' + str(comp_lugger) + '  '],
                              ['    ' + str(player_brigantine) + ' ', ' BR',
                               'IGA', 'NTI', 'NE ', ' ' + str(comp_brigantine)
                               + '  '],
                              ['    ' + str(player_schooner + player_lugger
                               + player_brigantine) + ' ', '   ', 'TOT', 'AL ',
                               '   ', ' ' + str(comp_schooner + comp_lugger
                                                + comp_brigantine) + '  ']
                              ]
        else:
            for ship in self.player.ships:
                if ship.name == 'Pinnace':
                    if ship.health > 0:
                        player_pinnace = 1
                    else:
                        player_pinnace = 0
                elif ship.name == 'Sloop':
                    if ship.health > 0:
                        player_sloop = 1
                    else:
                        player_sloop = 0
                elif ship.name == 'Schooner':
                    if ship.health > 0:
                        player_schooner = 1
                    else:
                        player_schooner = 0
                elif ship.name == 'Lugger':
                    if ship.health > 0:
                        player_lugger = 1
                    else:
                        player_lugger = 0
                elif ship.name == 'Brigantine':
                    if ship.health > 0:
                        player_brigantine += 1
            for ship in self.comp.ships:
                if ship.name == 'Pinnace':
                    if ship.health > 0:
                        comp_pinnace = 1
                    else:
                        comp_pinnace = 0
                elif ship.name == 'Sloop':
                    if ship.health > 0:
                        comp_sloop = 1
                    else:
                        comp_sloop = 0
                elif ship.name == 'Schooner':
                    if ship.health > 0:
                        comp_schooner = 1
                    else:
                        comp_schooner = 0
                elif ship.name == 'Lugger':
                    if ship.health > 0:
                        comp_lugger = 1
                    else:
                        comp_lugger = 0
                elif ship.name == 'Brigantine':
                    if ship.health > 0:
                        comp_brigantine += 1

            self.scoreboard = [
                              ['  C', 'AL', 'IC', 'O ', '  ', ' J', 'ON', 'AT',
                               'HA', 'N  '],
                              ['   ', 'JA', 'CK', '  ', '  ', '  ', 'BA', 'RN',
                               'ET', '   '],
                              ['   ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',
                               '  ', '   '],
                              ['   ', '  ', ' S', 'HI', 'PS', ' L', 'EF', 'T ',
                               '  ', '   '],
                              ['  ' + str(player_pinnace), '  ', '  ', 'PI',
                               'NN', 'AC', 'E ', '  ', '  ', str(comp_pinnace)
                               + '  '],
                              ['  ' + str(player_sloop), '  ', '  ', ' S',
                               'LO', 'OP', '  ', '  ', '  ', str(comp_sloop)
                               + '  '],
                              ['  ' + str(player_schooner), '  ', '  ', 'SC',
                               'HO', 'ON', 'ER', '  ', '  ', str(comp_schooner)
                               + '  '],
                              ['  ' + str(player_lugger), '  ', '  ', ' L',
                               'UG', 'GE', 'R ', '  ', '  ', str(comp_lugger)
                               + '  '],
                              ['  ' + str(player_brigantine), '  ', ' B', 'RI',
                               'GA', 'NT', 'IN', 'E ', '  ',
                               str(comp_brigantine) + '  '],
                              ['  ' + str(player_pinnace
                                          + player_sloop
                                          + player_schooner
                                          + player_lugger
                                          + player_brigantine),
                               '  ', '  ', ' T', 'OT', 'AL', '  ', '  ', '  ',
                               str(comp_pinnace
                                   + comp_sloop
                                   + comp_schooner
                                   + comp_lugger
                                   + comp_brigantine)
                               + '  ']
                              ]

# setup the comp player and starts turn loop
    def comp_setup(self):
        self.comp.place_ships(self)
        clear_terminal()
        print('This is the target selection screen, use the targeting radar \
to determine')
        print(f'where to shoot. If you miss a {C.BGBLUE + "~" + C.END} will \
appear. If you hit a {C.RED + "#" + C.END} will appear.')
        print('The enemies shots will appear on your board.')
        print(f'If they miss a {C.YELLOW + "M" + C.END} will appear a hit \
will be marked with a {C.RED + "#" + C.END}\n')
        self.print_blank_and_player_boards()
        self.player.get_target_from_user(self)

# identify if ship sunk, and return ship name
    def identify_ship(self, opponent, shot):
        for ship in opponent.ships:
            if shot in ship.location:
                ship.health -= 1
                if ship.health == 0:
                    if opponent == self.comp:
                        print(f'We sunk their {ship.name}!')
                    else:
                        print(f'They sunk our {ship.name}!')

# manage the turn of each player
# check board locations for ships
    def turn_loop(self, whichplayer, shot):
        if (whichplayer == self.player):
            if self.comp.board.board[shot[0]][shot[1]] == '~':
                self.blank.board.board[shot[0]][shot[1]]\
                    = C.BGBLUE + '~' + C.END
                clear_terminal()
                print('''
Nothing but water! What a waste of some perfectly good iron.
Your turn is over! You missed!\n''')
                time.sleep(1)
                self.comp.get_target_from_comp(self)
            else:
                self.blank.board.board[shot[0]][shot[1]]\
                    = C.RED + '#' + C.END
                clear_terminal()
                print('''
Direct Hit!!! The sound of screams and breaking wood is unmistakable!''')
                self.player.hit_counter += 1
                # check if ship sunk
                self.identify_ship(self.comp, shot)
                if self.check_for_win(whichplayer):
                    self.end_game(whichplayer)
                else:
                    time.sleep(1)
                    self.comp.get_target_from_comp(self)
        else:
            if self.player.board.board[shot[0]][shot[1]] == '~':
                self.player.board.board[shot[0]][shot[1]] = C.YELLOW + 'M'\
                    + C.END
                self.print_blank_and_player_boards()
                self.comp.last_shot_hit = False
                print('''
They missed! Nothing but water! Useless West India Co landlovers
They would miss a bottle of rum if it was in their own hands.
It's our turn again, let's do some damage argh!''')
                time.sleep(1)
                self.player.get_target_from_user(self)
            else:
                self.player.board.board[shot[0]][shot[1]] = C.RED + '#' + C.END
                self.print_blank_and_player_boards()
                self.comp.last_shot_hit = True
                print('''
Direct Hit!!! We took damage! Don't just stand their you filthy rats,
did you expect them to just send over rum and wenches for a party? It's
our turn now! Unleash Hell!''')
                self.comp.hit_counter += 1
                self.identify_ship(self.player, shot)
                time.sleep(1)
                if self.check_for_win(whichplayer):
                    self.end_game(whichplayer)
                else:
                    time.sleep(1)
                    self.player.get_target_from_user(self)

    def print_blank_and_player_boards(self):
        self.create_scoreboard()
        letter = 0
        x = ' '
        if self.dimensions == 6:
            print(x + 'TARGETING RADAR'
                  + x * 32
                  + 'YOUR BOARD'
                  + x * 5
                  + '\n')
        else:
            print(x * 5
                  + 'TARGETING RADAR'
                  + x * 40
                  + 'YOUR BOARD'
                  + x * 7
                  + '\n')
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            print(i, end=' ')
        # prints ending character for numbers area and gap to new board
        print('| ', ' '*24, end=' ')
        # prints first line of board with numbers for column reference board 2
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            print(i, end=' ')
        print('| ')

        # prints player board to screen,
        for letter in range(self.dimensions):
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.blank.board.board[letter])):
                print(self.blank.board.board[letter][column], end=' ')
        # prints ending character for numbers area and gap to new board
        # Inserts Scoreboard information in here
            print('|', end='  ')
            for column in range(len(self.scoreboard[letter])):
                print(self.scoreboard[letter][column], end='')
            # puts a capital letter in front of each row of board
            print('  ', end=' ')
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.player.board.board[letter])):
                print(self.player.board.board[letter][column], end=' ')
            print('| ')
            letter += 1

    def print_player_board(self):
        letter = 0
        # prints first line of board with numbers for column reference
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            print(i, end=' ')
        # prints ending character for numbers area and gap to new board
        print('| ')
        # prints player board to screen,
        for letter in range(self.dimensions):
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.player.board.board[letter])):
                print(self.player.board.board[letter][column], end=' ')
            print('| ')
            letter += 1


def create_player_ships(dimensions, player, comp, game):
    # pre-determined ratio so number of ships is appropriate
    number_of_ships_ratio = 0.6
    # list of possible ships in game, for large boards
    # list will loop through again
    ships = [
        ('Brigantine', 2),
        ('Lugger', 3),
        ('Schooner', 3),
        ('Sloop', 4),
        ('Pinnace', 5)
    ]
    # calculate number of ships based on board dimensions
    number_of_ships = math.floor(dimensions * number_of_ships_ratio)
    fleet = []
    x = 0
    hits = 0
    # generate list of ships for each player
    while x < number_of_ships:
        v = x % len(ships)
        fleet.append(ships[v])
        x += 1
    # reverse order of ships so players can assign them in
    # the order of largest ship first. It is needed due to
    # the list of ships being generated based on board size
    # this way small boards don't get three large ships.
    fleet = sorted(fleet, reverse=True, key=lambda x: x[1])
    # takes sum of the length of each ship to create win condition
    for ship in fleet:
        hits += ship[1]
    game.win_needs(hits)
    # creates Boat object for each ship within player objects
    for ship in fleet:
        player.ships.append(Boat(ship[0], ship[1]))
        comp.ships.append(Boat(ship[0], ship[1]))


# Function to initialise game, players and ships
def create_players(dimensions, difficulty):
    player = Player('Calico Jack', dimensions)
    comp = Comp('Jonathan Barnet', dimensions, difficulty)
    blank = Blank(dimensions, comp)
    game = Game(dimensions, player, comp, blank)
    create_player_ships(dimensions, player, comp, game)
    player.get_position_from_user(player, comp, game)


# SETUP function - establishes parameters for game
def setup():
    clear_terminal()
    print("Good on ya, argh, we'll make a pirate out of ye yet!")
# USER OPTIONS LOGIC
# Grid dimension selection 6x6 or 10x10 message
    while True:
        try:
            # user input of desired dimension for board
            dimensions = int(input('''
How brave are ye? Shall we play a full game or a little one?
Select a board size, enter '6' for a little one or '10' for normal:\n'''))
            #   validation of user input
            if (dimensions != 6) and (dimensions != 10):
                raise Exception()
            elif (dimensions == 6) or (dimensions == 10):
                break
        # display error message if input fails vaidation
        except Exception:
            clear_terminal()
            print('''
Don't be getting all artistic with the choices like some scurvy landlover.
It's either '6' or '10' that be it. Just the number! Try again!\n''')

# Difficulty options
    while True:
        try:
            if dimensions == 6:
                difficulty = input('''
A little one, suppose you want it easy as well? Select your difficulty,
enter 'E' for easy, 'N' for normal or 'H' for hard:\n''').lower()
                if ((difficulty != 'e')
                        and (difficulty != 'n')
                        and (difficulty != 'h')):
                    raise Exception()
                else:
                    break
            elif dimensions == 10:
                difficulty = input('''
Hmm a full one, ye be a brave pirate tryin to impress me? If you really
want to impress me, you should try it on hard. Select your difficulty,
enter 'E' for easy, 'N' for normal or 'H' for hard:\n''').lower()
                if ((difficulty != 'e')
                        and (difficulty != 'n')
                        and (difficulty != 'h')):
                    raise Exception()
                else:
                    break
        except Exception:
            clear_terminal()
            print('''
There ye go getting artistic, are ye a pirate or a West Indian spy?
Try again, before we make ye walk the plank, it's 'E', 'N' or 'H'
Just the letters, no dots, dashs or bottles of rum\n''')
    create_players(dimensions, difficulty)


# START function - first function - welcome through to setup()
# Game start
# Display Welcome Message
def start():

    print('''
                              @@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@
    @                      @@@@@@@@@@@@@@@@@@@@@@@@                        ,
    .@@                   @@@@*@@@@@@@@@@@@@@@@@@@@@                      @@
    *@@@                  @@/@@.     @@@/.    %@ @@                   /@@@
     @@@@(                 @/@@.    @@.@@@    @@ @                  @@@.@
       @@@@@               @@@@@@@@@ . /@@@@@@@@@               *@@@,@
         @@@@@@             %@@@@@@@&@@@@@@@ *%.              @@@@%@
            &@@@@@@.          ,@( (@@@@@@@@  @@            #@@@@,@,
             @@@@@#@@        @@           ,@(         @@&@@@@(
                   %@@@@.@@@     @@@@@@@@@@@@@/     *@@&.@@@@,
                       @@@@&,@@@&   @@@&@@@%    @@@@ @@@@&
                           @@@@@,%@@@@/   &@@@@,&@@@@#
                 @@@@@          @@@@@%.@@@@@&,%@#         %@@@@
                 @@@.@@@  ,%@@@@@& ,#*@@@@@@* (@@@@@@*  @@@%@@@
          @@@ @@(@@*@&%@@@@ &@@@@@@#        *@@@@@@@*/@@@@ @,@@ @@ @@@
         @@@@@ @@@@@@@@%@@ *                          @@@/@@@@@@@,*@@@@
        ,@@/          @@@ (#                    *% /@@          (@@#
                        @@@@@%                   @@@@@''')

    play = 'N'
    while play == 'N':
        try:
            play = input('''Would you like to play a game me 'arty?
Click inside the terminal window and then using your keyboard press 'I' for
the instructions, 'Y' to play or 'Q' to quit, followed by the enter key:\n''')
            play = play.lower()
            if (play != 'y') and (play != 'q') and (play != 'i'):
                raise Exception()
            elif play == 'q':
                print('''
    Goodbye
    To restart the game click on the 'RUN PROGRAM' button above!\n''')
                quit()
            elif play == 'i':
                clear_terminal()
                print(C.RED + 'Instructions' + C.END)
                print('''It is the night of October 31st, 1720. Anchored off
the coast of Jamaica, infamous pirate Calico Jack and his crew were
celebrating a fun day. One in which they had made another pirate ship turn and
flea and were enjoying several bottles of rum. Unbeknown to Jack and his crew
the pirate ship they had earlier scared off was working for the notorious
bounty hunter Jonathan Barnet. With Barnet now on his way to their location
Jack and his crew started to retire, falling asleep just as Barnet entered the
cove in which they were anchored. You are the one lowly deck hand tasked with
keeping watch and defending the ships in the cove, when you hear Barnet callout
"Who sails there?? Identify yourself!"
With surrender not an option, you know you must defend the ships and Jack!''')
                print(C.RED + 'Objective' + C.END)
                print("Sink all Barnet's ships before he sinks all of Jacks")
                print()
                play = 'N'
        except Exception:
            clear_terminal()
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?\n''')
            play = 'N'

    setup()


start()
