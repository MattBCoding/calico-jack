# import required modules here

# python code goes here

# class Board:
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

# class Boat:

# class Player:
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


# class Comp:

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


# class Game:
# display board

# PLAY GAME LOGIC
# display grids, one for targetting one for showing own ship locations

# END OF GAME LOGIC
#   Display end of game screen
#   display message to user showing who won and final score
#   display thank you for playing message
#   ask user if they would like to play again
#   user input y for yes n for no
#   user input validation
#   if yes - restart game
#   if no - display a thank you for playing message and exit app


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
    

# passes information on difficulty and dimensions to classes

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
