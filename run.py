# import required modules here
import math
import random
import string
import time
import sys
# python code goes here
'''
NOTE to self
BUG in targetting on user input when they enter nothing
need to reorganise starting menu to include instructions
need to add backstory
need to adjust formatting for deployed terminal emulator
use color class to add colours to strings and boards
need to add scoreboard
could add leaderboard and link in a google sheet for highscores
possibly move some classes to other files to make things easier to find
'''


def loading():
    print("Loading...")
    print(u"\u001b[1m\u001b[31m")
    print('\n\n\n')
    sys.stdout.write(u"\u001b[3A")
    for i in range(0, 100):
        time.sleep(0.01)
        width = int((i + 1) / 4)
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" + bar)
        sys.stdout.flush()
    sys.stdout.write(u"\u001b[" + "A")
    print
    print(u"\u001b[0m")


class C:
    END = '\33[0m'
    BLACK = '\33[30m'
    RED = '\33[91m'
    GREEN = '\33[92m'
    YELLOW = '\33[93m'
    BLUE = '\33[94m'
    BGBLACK = '\33[40m'
    BGRED = '\33[41m'
    BGGREEN = '\33[42m'
    BGYELLOW = '\33[43m'
    BGBLUE = '\33[44m'
    BGVIOLET = '\33[45m'
    BGWHITE = '\33[47m'


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

    def on_board_test(self, coords):
        row_test = ((ord(coords[0].upper()) - 65) < self.dimensions)
        column_test = (int(coords[1]) < self.dimensions)
        if(row_test and column_test):
            print('coords on board')
            return True
        else:
            print('''
    The location entered is not on the board! The format is row then column,
    e.g. 'A2' or 'C5'. Try Again!''')
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
        print(vertical_check)
        # horizontal orientation from column check
        horizontal_check = (self.dimensions
                            - column_coord_value
                            - ship.length >= 0)
        print(horizontal_check)
        if horizontal_check:
            if vertical_check:
                # Ship fits both horizontally and vertically
                # check board to see if locations are clear
                # both vertically and horizontally
                # horizontal
                i = 0
                while i < ship.length:
                    print(i)
                    if self.board[row_coord_value][column_coord_value] == '~':
                        print("if")
                        clear_space_horizontal.append((row_coord_value,
                                                      column_coord_value))
                        column_coord_value += 1
                        i += 1
                    else:
                        print("else")
                        column_coord_value += 1
                        i += 1
                # vertical
                j = 0
                # reset values back to original after while loop
                row_coord_value = (ord(coords[0].upper()) - 65)
                column_coord_value = int(coords[1])
                while j < ship.length:
                    print("starting second while loop")
                    if self.board[row_coord_value][column_coord_value] == '~':
                        print("v if")
                        clear_space_vertical.append((row_coord_value,
                                                    column_coord_value))
                        row_coord_value += 1
                        j += 1
                    else:
                        print("v else")
                        row_coord_value += 1
                        j += 1

                if ship.length == len(clear_space_horizontal):
                    if ship.length == len(clear_space_vertical):
                        print(len(clear_space_horizontal))
                        print("^^^ length of clear space horizontal")
                        print(len(clear_space_vertical))
                        print("^^^ length of clear space vertical")
                        print("scenario 1")
                        return 1
                    else:
                        print("scenario 2")
                        return 2
                elif ship.length == len(clear_space_vertical):
                    print(len(clear_space_vertical))
                    print("^^^ length of clear space vertical")
                    print("scenario 3")
                    return 3
                else:
                    return 8

            else:
                # Ship fits horizontally but not vertically
                # check board to see if locations are clear (only contain ~)
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
                    print(len(clear_space_horizontal))
                    print("^^^ length of clear space horizontal")
                    print("scenario 4")
                    return 4
                else:
                    print(len(clear_space_horizontal))
                    print("^^^ length of clear space horizontal")
                    print("scenario 5")
                    return 5

        else:
            if vertical_check:
                # ship fits vertically but not horizontally
                # check board to see if locations are clear (only contain ~)
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
                    print(len(clear_space_vertical))
                    print("^^^ length of clear space vertical")
                    print("scenario 6")
                    return 6
                else:
                    print(len(clear_space_vertical))
                    print("^^^ length of clear space vertical")
                    print("scenario 7")
                    return 7
            else:
                print("scenario 8")
                return 8

    def set_ship_position(self, ship):
        for tile in ship.location:
            self.board[tile[0]][tile[1]] = 'S'
            print(self.board)


# create grid and store player ship locations
# add ships to board

# validation of ship location - does ship overlap any other ships?
# display error message informing user
#       - repeat user input to select alternative location
# ship location ok
# store ship location to ship, and to board


# HIT LOGIC LOOP
#   Record hit to board and ship record
#   Did hit sink a ship?
#   if yes, display ship that sunk message
#   are there any other ships remaining?
#   if no, player wins game - game over
#   if yes, display refreshed board and restart targetting loop
#       - user gets another go.

# MISS LOGIC
#   Record miss to board and shot record
#   display updated board
#   start other player turn

class Boat:
    '''
    Constructor for Boat objects
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
        print("from Boat set_position")
        print(self.location)


class Player:
    '''
    Player object
    '''

    def __init__(self, name, dimensions):
        self.name = name
        self.board = Board(dimensions)
        self.ships = []
        self.previous_shots = []
        self.hit_counter = 0

    def get_target_from_user(self, game):
        # BUG if user presses enter instead of inputting a coord
        # system generates a TypeError: 'NoneType' object is not
        # subscriptable. inserted a if statement to check for this
        # which successfully generates the message, however as its
        # out of a while loop, it no longer repeats the input
        # need to fix
        x = 0
        shot = None
        try:
            while x < 1:
                user_target = input('''
What are your orders? Where do you want to target?
Select the location in the format of row then column e.g. 'E4':\n''')
                if user_target is None:
                    raise TypeError
                # THIS NEEDS REFACTORING IS DUPLICATED CODE
                # DUPLICATED IN SHIP PLACEMENT AS WELL
                # MOVE INTO OWN FUNCTION
                # convert to a list
                else:
                    user_target_coords_list = list(user_target)
                # check input is correct length
                    if len(user_target_coords_list) != 2:
                        raise Exception
                    elif (not user_target_coords_list[0].isalpha()
                            or not user_target_coords_list[1].isdigit()):
                        raise Exception
                    # check target is a valid on board location
                    elif self.board.on_board_test(user_target_coords_list):
                        a = (ord(user_target_coords_list[0].upper()) - 65)
                        b = int(user_target_coords_list[1])
                        shot = [a, b]
                        while True:
                            try:
                                if shot in self.previous_shots:
                                    print(self.previous_shots)
                                    raise Exception
                                else:
                                    self.previous_shots.append(shot)
                                    print(self.previous_shots)
                                    x += 1
                                    break
                            except Exception:
                                game.print_blank_and_player_boards()
                                print('''
You have already fired there, are you trying to waste our Cannonballs?
You better get your head in the game pirate, lets try this again!''')
                            break
        except TypeError:
            print('''
You have to choose a target location! Waving the white flag will just
get your head to the gallows sooner. Try again, it needs to be in the format
of 'E4' letter then number, no spaces, no dashes, no second chances!\n''')
        except Exception:
            print('''
We've been through this already, it needs to be in the format of 'E4'
Letter then Number, this is not a time to act the fool, try again! ''')
        game.turn_loop(self, shot)

    def get_position_from_user(self, player, comp, game):
        game.print_boards()  # remove this for finished game
        # game.print_player_board() switch to this line for finished game
        input('''
    Now we need to position our ships ready for battle! Are ye ready?
    Press 'Enter' to start!\n''')
        for ship in self.ships:
            self.position_ship(ship, game)
        print('''
    THERE HERE!!! THERE HERE!!! MAN THE CANNONS!!!
    Wait?? Where is everyone?? You'll have to fight them on your own while I
    go and wake that drunken rabble up! Do not let Calico Jack down!\n''')
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
                # user input of starting location for next ship
                # check input is the correct length
                if len(user_input_coords_list) != 2:
                    raise Exception
                # check input is in the correct format letter then number
                elif (not user_input_coords_list[0].isalpha()
                        or not user_input_coords_list[1].isdigit()):
                    raise Exception
                # input validation of starting location for next ship
                # need to check if input is valid board coords.
                elif self.board.on_board_test(user_input_coords_list):
                    # now need to check if ship can be placed Hor or Ver
                    # at location specified by user.
                    # check for space enough and clear
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
                            print('''
    It can only be 'H' for horizontally or 'V' for vertically
    There are no other options, try again!''')
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 2:
                        print("Can only be H, V hits another ship")
                        orientation = 'h'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 3:
                        print("Can only be V, H hits another ship")
                        orientation = 'v'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 4:
                        # scenario 4 = ship can only be placed horizontally
                        # being used as a test case to assign ship to board
                        orientation = 'h'
                        self.add_ship(ship, user_input_coords_list,
                                      orientation, game)
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 5:
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
                        print('''
    Can not place ship, only option from this location is vertical
    which would hit another ship. Try a different location\n''')
                        game.print_boards()
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 8:
                        print('''
    Can not place ship, it will not fit either horizontally or
    vertically at this location. Try a different location\n''')
                else:
                    raise Exception
# display error message - repeat user input
            except Exception:
                print('''
    The starting location needs to be entered in the format of row then
    column, e.g. 'F4' or 'A2' a letter followed by a number,
    no spaces, dashes, dots or bottles of rum before after or in the
    middle. Try again!\n''')

    def add_ship(self, ship, coords, orientation, game):
        x = (ord(coords[0].upper()) - 65)
        y = int(coords[1])
        ship.set_position(x, y, orientation)
        print("ship position just set")
        print(ship.x, ship.y, ship.orientation)
        self.board.set_ship_position(ship)
        print("ship added to board ok")
        game.print_boards()
        print(self.board)  # so I can check the object against original value


# GAME SETUP LOGIC
# validation of ship location - does ship fit starting in that location in
#       either horizontal or vertical orientation?
# if fails location validation - display error message to user informing them
#       why and repeat user input
# display message asking user if ship horizontal or vertical
# user choice h = horizontal v = vertical
# user input for ship orientation
# input validation for ship orientation
# display error message if wrong type of input inserted by user
#       - repeat user input
# validation of ship location - does ship fit in selected location
# display error message if ship does not fit, informing user why
#       - repeat user input
# validation of ship location - does ship overlap any other ships?
# display error message informing user
#       - repeat user input to select alternative location
# ship location ok
# store ship location to ship, and to board
# check to see if more ships still to be placed
# if needed repeat earlier steps for other ships

# display message to user about selecting firing location
#   display message to user to select which column
#   user input of column - should be integer
#   user input validation
#       - column selection
#       - will come in as string
#       - convert to int
#   if value fails validation display error message and have user repeat input
#   display message to user to select row
#   user input of row - should be string - letter
#   user input validation
#       - row selection
#       - will come in as string
#       - convert to lowercase using .lower()
#   if value fails validation
#       - display error message and have user repeat input
#   validated target location check - has target been selected before?
#   if target previously been entered
#       - display error message to user and restart targetting process
#   check target location for enemy ship
#   hit or miss?

# create blanked out version of board to display in game
class Blank:
    '''
    class to hold a blank board to display to player
    blank board will reference comp board to determine if
    a ship has been hit.
    '''

    def __init__(self, dimensions, comp):
        self.dimensions = dimensions
        self.board = Board(dimensions)
        self.reference_board = comp.board
        self.board.turn_into_blank_board()


class Comp:
    '''
    AI player - will need shot selection
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
                print("comp shot")
                print(shot)
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
            print(self.target_list)
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

    def get_target_from_comp(self, game):
        if self.difficulty == 'e':
            shot = self.generate_easy_shot()
            game.turn_loop(self, shot)
        elif self.difficulty == 'n':
            shot = self.generate_normal_shot()
            game.turn_loop(self, shot)

    # def generate_target_locations(self, last_hit):

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
        # copied from player class
        x = (ord(coords[0].upper()) - 65)
        y = int(coords[1])
        ship.set_position(x, y, orientation)
        print("ship position just set")
        print(ship.x, ship.y, ship.orientation)
        self.board.set_ship_position(ship)
        print("ship added to board ok")
        game.print_boards()
        print(self.board)  # so I can check the object against original value


# AI SELECT LOCATIONS FOR SHIPS LOGIC

# AI SHOT LOGIC
#   AI selects firing location
#       - easy mode fully random selection
#       - normal mode AI will pick neighbouring tiles on hit
#       - hard mode AI uses algorithm to select targets
#   check location not previously selected
#   check if location a hit or miss
#   if hit - run hit logic loop
#   if miss - run miss logic loop


class Game:
    '''
    game object
    '''

    def __init__(self, dimensions, player, comp, blank):
        self.dimensions = dimensions
        self.player = player
        self.comp = comp
        self.blank = blank

# setup the winning condition
    def win_needs(self, hits):
        self.to_win = hits
        print("from the win_needs method")
        print(self.to_win)

# check for a win
    def check_for_win(self, whichplayer):
        if whichplayer.hit_counter == self.to_win:
            return True
        else:
            return False

# end game and declare winner
    def end_game(self, whichplayer):
        spacer = int((72 - len(whichplayer.name))/2)
        name = whichplayer.name
        print("\n\n\n\n\n\n\n\n")
        print(C.RED + '#' * 74 + C.END)
        print(C.RED + '#' * 74 + C.END)
        print(C.RED + '#' + ' ' * 72 + '#' + C.END)
        print(C.RED + '#' + ' ' * 72 + '#' + C.END)
        if whichplayer == self.player:
            print(C.RED + '#' + ' ' * 32 + 'You Win!' + ' ' * 32 + '#' + C.END)
        else:
            print(C.RED + '#' + ' ' * 32 + 'You Lose!' + ' ' * 31 + '#'
                  + C.END)
        print(C.RED + '#' + ' ' * spacer + name + ' ' * (spacer+1) + '#'
              + C.END)
        print(C.RED + '#' + ' ' * 72 + '#' + C.END)
        print(C.RED + '#' * 74 + C.END)
        print(C.RED + '#' * 74 + C.END)
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

# setup the comp player
    def comp_setup(self):
        self.comp.place_ships(self)
        self.print_blank_and_player_boards()
        self.player.get_target_from_user(self)

    # def check_for_win(self):
# identify if ship sunk, and return ship name
    def identify_ship(self, opponent, shot):
        # x = 1
        for ship in opponent.ships:
            # print(f"checking ship {x}")
            # print(ship.name)
            # print(ship.location)
            # x += 1
            # print(shot)
            # print("about to enter if statement")
            if shot in ship.location:
                # print(type(ship.health))
                # print(ship.name)
                # print(ship.length)
                # print(ship.health)
                ship.health -= 1
                # print(ship.health)
                if ship.health == 0:
                    if opponent == self.comp:
                        print(f'We sunk their {ship.name}!')
                    else:
                        print(f'They sunk our {ship.name}!')

# manage the turn of each player
# check board locations for ships
    def turn_loop(self, whichplayer, shot):
        print("start turn loop")
        if (whichplayer == self.player):
            print("matched player")
            print(self.comp.board.board[shot[0]][shot[1]])
            if self.comp.board.board[shot[0]][shot[1]] == '~':
                print("checked comp board ok")
                self.blank.board.board[shot[0]][shot[1]]\
                    = C.BGBLUE + '~' + C.END
                self.print_blank_and_player_boards()
                print('''
    You missed! Nothing but water! What a waste of some perfectly good
    iron. You better hope we win or you'll be swimming for that later!
    Your turn is over!\n''')
                time.sleep(1)
                self.comp.get_target_from_comp(self)
            else:
                self.blank.board.board[shot[0]][shot[1]]\
                    = C.RED + '#' + C.END
                self.print_blank_and_player_boards()
                print('''
    Direct Hit!!! The sound of screams and breaking wood is unmistakable!''')
                self.player.hit_counter += 1
                # check if ship sunk
                # print(shot)
                # print("checking ship from turn loop")
                self.identify_ship(self.comp, shot)
                # print("finished checking ship")
                # insert function call to check for player win
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
    It's our turn again, let's do some damage argh!\n''')
                time.sleep(1)
                self.player.get_target_from_user(self)
            else:
                self.player.board.board[shot[0]][shot[1]] = C.RED + '#' + C.END
                self.print_blank_and_player_boards()
                self.comp.last_shot_hit = True
                print('''
    Direct Hit!!! We took damage! Don't just stand their you filthy rats,
    did you expect them to just send over rum and wenches for a party? It's
    our turn now!\n''')
                self.comp.hit_counter += 1
                self.identify_ship(self.player, shot)
                # insert function call to check for player win
                time.sleep(1)
                if self.check_for_win(whichplayer):
                    self.end_game(whichplayer)
                else:
                    time.sleep(1)
                    self.player.get_target_from_user(self)

# display board
# display grids, one for targetting one for showing own ship locations
    def print_boards(self):
        letter = 0
        # prints five blank lines to create space
        # will need to be adjusted so that each time the print_boards is
        # called a fresh screen appears for the user, total line height = 24
        print('\n\n\n\n\n\n\n\n')
        # prints first line of board with numbers for column reference
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
            print(i, end=' ')
        # prints ending character for numbers area and gap to new board
        print('| ', ' '*20, end=' ')
        # prints first line of board with numbers for column reference board 2
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
            print(i, end=' ')
        print('| ')

        # prints player board to screen,
        for letter in range(self.dimensions):
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.player.board.board[letter])):
                print(self.player.board.board[letter][column], end=' ')
        # prints ending character for numbers area and gap to new board
        # MIDDLE TABLE information needs to go in here
            print('|', ' '*20, end='  ')
        # prints comp board to screen,
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.comp.board.board[letter])):
                print(self.comp.board.board[letter][column], end=' ')
            print('| ')
            letter += 1

    def print_blank_and_player_boards(self):
        letter = 0
        # prints five blank lines to create space
        # will need to be adjusted so that each time the print_boards is
        # called a fresh screen appears for the user, total line height = 24
        print('\n\n\n\n\n\n\n\n')
        # prints first line of board with numbers for column reference
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
            print(i, end=' ')
        # prints ending character for numbers area and gap to new board
        print('| ', ' '*20, end=' ')
        # prints first line of board with numbers for column reference board 2
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
            print(i, end=' ')
        print('| ')

        # prints player board to screen,
        for letter in range(self.dimensions):
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.blank.board.board[letter])):
                print(self.blank.board.board[letter][column], end=' ')
        # prints ending character for numbers area and gap to new board
        # MIDDLE TABLE information needs to go in here
            print('|', ' '*20, end='  ')
        # prints comp board to screen,
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.player.board.board[letter])):
                print(self.player.board.board[letter][column], end=' ')
            print('| ')
            letter += 1

    def print_player_board(self):
        letter = 0
        # prints five blank lines to create space
        # will need to be adjusted so that each time the print_boards is
        # called a fresh screen appears for the user, total line height = 24
        print('\n\n\n\n\n\n\n\n')
        print("PLAYER BOARD")
        # prints first line of board with numbers for column reference
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
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

    def print_blank_board(self):
        letter = 0
        # prints five blank lines to create space
        # will need to be adjusted so that each time the print_boards is
        # called a fresh screen appears for the user, total line height = 24
        print('\n\n\n\n\n\n\n\n')
        print("BLANK BOARD")
        # prints first line of board with numbers for column reference
        print(' '*2, end='| ')
        for i in range(self.dimensions):
            # print('    ')
            print(i, end=' ')
        # prints ending character for numbers area and gap to new board
        print('| ')
        # prints player board to screen,
        for letter in range(self.dimensions):
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(self.blank.board.board[letter])):
                print(self.blank.board.board[letter][column], end=' ')
            print('| ')
            letter += 1
# PLAY GAME LOGIC

# END OF GAME LOGIC
#   Display end of game screen
#   display message to user showing who won and final score
#   display thank you for playing message
#   ask user if they would like to play again
#   user input y for yes n for no
#   user input validation
#   if yes - restart game
#   if no - display a thank you for playing message and exit app


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
    print(number_of_ships)
    fleet = []
    x = 0
    hits = 0
    # generate list of ships for each player
    while x < number_of_ships:
        v = x % len(ships)
        fleet.append(ships[v])
        x += 1
        print(fleet)
    # reverse order of ships so players can assign them in
    # the order of largest ship first. It is needed due to
    # the list of ships being generated based on board size
    # this way small boards don't get three large ships.
    fleet = sorted(fleet, reverse=True, key=lambda x: x[1])
    print(fleet)
    print(len(fleet))
    # takes sum of the length of each ship to create win condition
    for ship in fleet:
        hits += ship[1]
    game.win_needs(hits)
    # creates Boat object for each ship within player objects
    for ship in fleet:
        player.ships.append(Boat(ship[0], ship[1]))
        comp.ships.append(Boat(ship[0], ship[1]))
    print(player.ships)
    print(comp.ships)


def create_players(dimensions, difficulty):
    player = Player('Calico Jack', dimensions)
    comp = Comp('Jonathan Barnet', dimensions, difficulty)
    blank = Blank(dimensions, comp)
    game = Game(dimensions, player, comp, blank)
    game.print_boards()
    game.print_player_board()
    game.print_blank_board()
    print(player.board)  # so there is a visible reference of the object
    print(comp.board)  # so there is a visible reference of the object
    create_player_ships(dimensions, player, comp, game)
    player.get_position_from_user(player, comp, game)


# SETUP function - establishes parameters for game
def setup():
    loading()
    print('''
    Good on ya, argh, we'll make a pirate out of ye yet!''')
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
            print('''
    Don't be getting all artistic with the choices like some scurvy landlover
    It's either '6' or '10' that be it. Try again!\n''')

# Difficulty options
# easy - comp selects tiles at random
# normal - comp selects tiles at random until a hit then targets nearby tiles
# hard - comp works on algorithm to determine next tile to target
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
                elif difficulty == 'e':
                    print('difficulty set to easy, dim=6')
# passes information on difficulty and dimensions to classes
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
                elif difficulty == 'n':
                    print('difficulty set to normal, dim=6')
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
                elif difficulty == 'h':
                    print('difficulty set to hard, dim=6')
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
            elif dimensions == 10:
                difficulty = input('''
    Hmm a full one, ye be a brave pirate to tryin to impress me? If you really
    want to impress me, you should try it on hard Select your difficulty,
    enter 'E' for easy, 'N' for normal or 'H' for hard:\n''').lower()
                if ((difficulty != 'e')
                        and (difficulty != 'n')
                        and (difficulty != 'h')):
                    raise Exception()
                elif difficulty == 'e':
                    print('difficulty set to easy, dim=10')
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
                elif difficulty == 'n':
                    print('difficulty set to normal, dim=10')
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
                elif difficulty == 'h':
                    print('difficulty set to hard, dim=10')
                    # player = Player('Calico Jack', dimensions)
                    # comp = Comp('Jonathan Barnet', dimensions, difficulty)
                    break
        except Exception:
            print('''
    There ye go getting artistic, are ye a pirate or a West Indian spy?
    Try again, before we make ye walk the plank, it's 'E', 'N' or 'H'\n''')
    create_players(dimensions, difficulty)


# START function - first function - welcome through to setup()
# Game start
# Display Welcome Message


def start():

    print('''
      . .    . .  . . .  . .  . .     ,((/. .    . .  . . .  . .  . .    . .
    . .    . .  . . .  . .  .. @@@@@@@@@@@@@@@@ . .  . . .  . .  . .    . .
    . .    . .  . . .  . . .@@@@@@@@@@@@@@@@@@@@@ .  . . .  . .  . .    . .
    @ . .    . .  . . .   @@@@@@@@@@@@@@@@@@@@@@@@@   . . .  . .  . .    . ,
    .@@ .    . .  . . .  .@@@@*@@@@@@@@@@@@@@@@@@@@@  . . .  . .  . .    .@@
    *@@@    . .  . . .  . .@/@@.     @@@/. .  %@ @@  . . .  . .  . .  /@@@
    .@@@@( . .  . . .  . .@/@@.    @@.@@@ .  @@ @.  . . .  . .  . .@@@.@ .
    . .@@@@@ .  . . .  . ..@@@@@@@@@ . /@@@@@@@@@.  . . .  . .  *@@@,@ . .
    . .  @@@@@@ .   .  .    %@@@@@@@&@@@@@@@ *%. .  . . .  . .@@@@%@   . .
            &@@@@@@.          ,@( (@@@@@@@@  @@            #@@@@,@,
    . .    . @@@@@#@@  .     @@    . .. . ,@(  .    ..@@&@@@@(  . .  . .
    .  . .  . .    %@@@@.@@@   . @@@@@@@@@@@@@/ . . *@@&.@@@@,.    . .  . .
    .  . .  . .    . . @@@@&,@@@&   @@@&@@@% . .@@@@ @@@@&  . .    . .  . .
    .  . .  . .    . .  .  @@@@@,%@@@@/ ..&@@@@,&@@@@# . .  . .    . .  . .
    .  . .  . .  @@@@@  . .    .@@@@@%.@@@@@&,%@# .    . .%@@@@    . .  . .
    .  . .  . .  @@@.@@@. ,%@@@@@& ,#*@@@@@@* (@@@@@@* .@@@%@@@.   . .  . .
    .  . .@@@ @@(@@*@&%@@@@ &@@@@@@#. . .  .*@@@@@@@*/@@@@ @,@@ @@ @@@  . .
    .  . @@@@@ @@@@@@@@%@@ *   . .  . . .  . .  . . . @@@/@@@@@@@,*@@@@ . .
        ,@@/          @@@ (#                    *% /@@          (@@#
                        @@@@@%                   @@@@@''')

    play = 'N'
    while play == 'N':
        try:
            play = input('''Would you like to play a game me 'arty?
(enter 'Y' to play or 'Q' to quit):\n''').lower()
            if (play != 'y') and (play != 'q'):
                raise Exception()
            elif play == "q":
                print('''
    Goodbye''')
                quit()
        except Exception:
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?\n''')
            play = 'N'

    setup()


start()
