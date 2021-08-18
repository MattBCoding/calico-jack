# import required modules here
import math
# python code goes here


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
        # horizontal orientation from column check
        horizontal_check = (self.dimensions
                            - column_coord_value
                            - ship.length >= 0)
        if horizontal_check:
            if vertical_check:
                # Ship fits both horizontally and vertically
                # check board to see if locations are clear
                # both vertically and horizontally
                # horizontal
                for i in range(ship.length):
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_horizontal.append((row_coord_value,
                                                      column_coord_value))
                        column_coord_value += 1
                    else:
                        column_coord_value += 1
                # vertical
                for i in range(ship.length):
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_vertical.append((row_coord_value,
                                                    column_coord_value))
                        row_coord_value += 1
                    else:
                        row_coord_value += 1
                if ship.length == len(clear_space_horizontal):
                    if ship.length == len(clear_space_vertical):
                        return 1
                    else:
                        return 2
                elif ship.length == len(clear_space_vertical):
                    return 3

            else:
                # Ship fits horizontally but not vertically
                # check board to see if locations are clear (only contain ~)
                for i in range(ship.length):
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_horizontal.append((row_coord_value,
                                                      column_coord_value))
                        column_coord_value += 1
                    else:
                        column_coord_value += 1
                if ship.length == len(clear_space_horizontal):
                    return 4
                else:
                    return 5

        else:
            if vertical_check:
                # ship fits vertically but not horizontally
                # check board to see if locations are clear (only contain ~)
                for i in range(ship.length):
                    if self.board[row_coord_value][column_coord_value] == '~':
                        clear_space_vertical.append((row_coord_value,
                                                    column_coord_value))
                        row_coord_value += 1
                    else:
                        row_coord_value += 1
                if ship.length == len(clear_space_vertical):
                    return 6
                else:
                    return 7
            else:
                return 8

    def set_ship_position(self, ship):
        width = 1
        height = 1
        if ship.orientation == 'h':
            width = ship.length
            print("width set ok")
            print(width)
        else:
            height = ship.length
            print("height set ok")

        for y in range(width):
            for x in range(height):
                self.board[ship.x + x][ship.y + y] = 'S'
                print(self.board)  # check object value against original


# create grid and store player ship locations
# create blanked out version of board to display in game
# add ships to board
# check board locations for ships

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

    def set_position(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation


class Player:
    '''
    Player object
    '''

    def __init__(self, name, dimensions):
        self.name = name
        self.board = Board(dimensions)
        self.ships = []

    def get_position_from_user(self, player, comp, game):
        game.PrintBoards()
        input('''
    Now we need to position our ships ready for battle! Are ye ready?
    Press 'Enter' to start! ''')
        for ship in self.ships:
            self.position_ship(ship, game)

    def position_ship(self, ship, game):
        while True:
            try:
                user_input_coords = input(f'''
    Please select the starting location for your {ship.name}, it is
    {ship.length} tiles long, in the format of row then column e.g. 'E4' : ''')
                # convert input to list
                user_input_coords_list = list(user_input_coords)
                # check input is the correct length
                if len(user_input_coords_list) != 2:
                    raise Exception
                # check input is in the correct format letter then number
                elif (not user_input_coords_list[0].isalpha()
                        or not user_input_coords_list[1].isdigit()):
                    raise Exception
                # need to check if input is valid board coords.
                elif self.board.on_board_test(user_input_coords_list):
                    # now need to check if ship can be placed Hor or Ver
                    # at location specified by user.
                    # check for space enough and clear
                    if self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 1:
                        print("Ask for orientation, can be H or V")
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 2:
                        print("Can only be H, V hits another ship")
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 3:
                        print("Can only be V, H hits another ship")
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 4:
                        # scenario 4 = ship can only be placed horizontally
                        # being used as a test case to assign ship to board
                        self.add_ship(ship, user_input_coords_list, 'h', game)
                        game.PrintBoards()
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 5:
                        print("Can not place ship H would hit another ship")
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 6:
                        print("Can only be V, Are you happy to place ship?")
                        break
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 7:
                        print("Can not place ship V would hit other ship")
                    elif self.board.can_ship_be_placed(
                            user_input_coords_list, ship) == 8:
                        print("Ship does not fit on board either H or V")
                else:
                    raise Exception
            except Exception:
                print('''
    The starting location needs to be entered in the format of row then
    column, e.g. 'F4' or 'A2' a letter followed by a number,
    no spaces, dashes, dots or bottles of rum before after or in the
    middle. Try again!''')

    def add_ship(self, ship, coords, orientation, game):
        x = (ord(coords[0].upper()) - 65)
        y = int(coords[1])
        ship.set_position(x, y, orientation)
        print("ship position just set")
        print(ship.x, ship.y, ship.orientation)
        self.board.set_ship_position(ship)
        print("ship added to board ok")
        game.PrintBoards()
        print(self.board)  # so I can check the object against original value


# GAME SETUP LOGIC
# display message informing user on next ship to be placed - name and size
# user input of starting location for next ship
# input validation of starting location for next ship
# display error message - repeat user input
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


class Comp:
    '''
    AI player - will need shot selection
    setting ship locations
    difficulty algorithms
    '''

    def __init__(self, name, dimensions, difficulty):
        self.name = name
        self.board = Board(dimensions)
        self.difficulty = difficulty
        self.ships = []

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

    def __init__(self, dimensions, player, comp):
        self.dimensions = dimensions
        self.player = player
        self.comp = comp

# display board
# display grids, one for targetting one for showing own ship locations
    def PrintBoards(self):
        letter = 0
        # prints five blank lines to create space
        # will need to be adjusted so that each time the PrintBoards is
        # called a fresh screen appears for the user, total line height = 24
        print('\n\n\n\n\n')
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


def create_player_ships(dimensions, player, comp):
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
    # creates Boat object for each ship within player objects
    for ship in fleet:
        player.ships.append(Boat(ship[0], ship[1]))
        comp.ships.append(Boat(ship[0], ship[1]))
    print(player.ships)
    print(comp.ships)


def create_players(dimensions, difficulty):
    player = Player('Calico Jack', dimensions)
    comp = Comp('Jonathan Barnet', dimensions, difficulty)
    game = Game(dimensions, player, comp)
    game.PrintBoards()
    print(player.board)  # so there is a visible reference of the object
    print(comp.board)  # so there is a visible reference of the object
    create_player_ships(dimensions, player, comp)
    player.get_position_from_user(player, comp, game)


# SETUP function - establishes parameters for game
def setup():
    print('''
    Good on ya, argh, we'll make a pirate out of ye yet!''')
# USER OPTIONS LOGIC
# Grid dimension selection 6x6 or 10x10 message
    while True:
        try:
            # user input of desired dimension for board
            dimensions = int(input('''
    How brave are ye? Shall we play a full game or a little one?
    Select a board size, enter '6' for a little one or '10' for normal : '''))
            #   validation of user input
            if (dimensions != 6) and (dimensions != 10):
                raise Exception()
            elif (dimensions == 6) or (dimensions == 10):
                break
        # display error message if input fails vaidation
        except Exception:
            print('''
    Don't be getting all artistic with the choices like some scurvy landlover
    It's either '6' or '10' that be it. Try again!''')

# Difficulty options
# easy - comp selects tiles at random
# normal - comp selects tiles at random until a hit then targets nearby tiles
# hard - comp works on algorithm to determine next tile to target
    while True:
        try:
            if dimensions == 6:
                difficulty = input('''
    A little one, suppose you want it easy as well? Select your difficulty,
    enter 'E' for easy, 'N' for normal or 'H' for hard : ''').lower()
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
    enter 'E' for easy, 'N' for normal or 'H' for hard : ''').lower()
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
    Try again, before we make ye walk the plank, it's 'E', 'N' or 'H' ''')
    create_players(dimensions, difficulty)


# START function - first function - welcome through to setup()
# Game start
# Display Welcome Message


def start():

    print('''
    Welcome to Pirate Battleships
    This is a test for the multi line string
    To see how it formats it when it runs
    ''')
    print('''
      . .    . .  . . .  . .  . .     ,((/. .    . .  . . .  . .  . .    . .
    . .    . .  . . .  . .  .@@@@@@@@@@@@@@@@@ . .  . . .  . .  . .    . .
    . .    . .  . . .  . . @@@@@@@@@@@@@@@@@@@@@ .  . . .  . .  . .    . .
    @ . .    . .  . . .  . .&@@@@@@@@@@@@@@@@@@@@@@   . . .  . .  . .    . ,
    .@@ .    . .  . . .  .  @@*@@@@@@@@@@@@@@@@@@@@@  . . .  . .  . .    .@@
    *@@@    . .  . . .  . .@/@@.     @@@/. .  %@ @@  . . .  . .  . .  /@@@
    .@@@@( . .  . . .  . .@/@@.    @@.@@@ .  @@ @.  . . .  . .  . .@@@.@ .
    . .@@@@@ .  . . .  . ..@@@@@@@@@ . /@@@@@@@@@.  . . .  . .  *@@@,@ . .
    . .  @@@@@@ .   .  .        %@@@@@&@@@@@ *%. .  . . .  . .@@@@%@   . .
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
                        @@@@@%                   @@@@@
    ''')

    play = 'N'
    while play == 'N':
        try:
            play = input('''
    Would you like to play a game me 'arty?
    (enter 'Y' to play or 'Q' to quit) : ''').lower()
            if (play != 'y') and (play != 'q'):
                raise Exception()
            elif play == "q":
                print('''
    Goodbye''')
                quit()
        except Exception:
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?''')
            play = 'N'

    setup()


start()
