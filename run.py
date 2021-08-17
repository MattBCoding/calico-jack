# import required modules here
import math
# python code goes here


class Board:
    '''
    Creates and manages the playing boards
    '''

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.board = [
            ["~" for i in range(dimensions)] for i in range(dimensions)
            ]


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


class Player:
    '''
    Player object
    '''

    def __init__(self, name, dimensions):
        self.name = name
        self.board = Board(dimensions)
        self.ships = []

    def get_position_from_user(self, player, comp, game):
        game.PrintBoards(player, comp)
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
                else:
                    print(user_input_coords_list)
            except Exception:
                print('''
    The starting location needs to be entered in the format of row then
    column, e.g. 'F4' or 'A2' a letter followed by a number,
    no spaces, dashes, dots or bottles of rum before after or in the
    middle. Try again!''')


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
    AI player
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

# display board
# display grids, one for targetting one for showing own ship locations
    def PrintBoards(self, player, comp):
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
            for column in range(len(player.board.board[letter])):
                print(player.board.board[letter][column], end=' ')
        # prints ending character for numbers area and gap to new board
        # MIDDLE TABLE information needs to go in here
            print('|', ' '*20, end='  ')
        # prints comp board to screen,
            # puts a capital letter in front of each row of board
            print(chr(letter + 65), end=' | ')
            for column in range(len(comp.board.board[letter])):
                print(comp.board.board[letter][column], end=' ')
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
    number_of_ships_ratio = 0.6
    ships = [
        ('Brigantine', 2),
        ('Lugger', 3),
        ('Schooner', 3),
        ('Sloop', 4),
        ('Pinnace', 5)
    ]
    number_of_ships = math.floor(dimensions * number_of_ships_ratio)
    print(number_of_ships)
    fleet = []
    x = 0
    while x < number_of_ships:
        v = x % len(ships)
        fleet.append(ships[v])
        x += 1
        print(fleet)
    fleet = sorted(fleet, reverse=True, key=lambda x: x[1])
    print(fleet)
    print(len(fleet))
    for ship in fleet:
        player.ships.append(Boat(ship[0], ship[1]))
        comp.ships.append(Boat(ship[0], ship[1]))
    print(player.ships)
    print(comp.ships)


def create_players(dimensions, difficulty):
    player = Player('Calico Jack', dimensions)
    comp = Comp('Jonathan Barnet', dimensions, difficulty)
    game = Game(dimensions, player, comp)
    game.PrintBoards(player, comp)
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
