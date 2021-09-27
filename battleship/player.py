# player file to contain player class
from battleship.board import Board
from battleship.editscreen import clear_terminal
from battleship.editscreen import restart
import time


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
                # check for empty input
                if user_target == '':
                    raise TypeError
                # check for user quit
                elif user_target.lower() == 'quit':
                    print('''
What? Are you scared of the noise a cannon makes? Fine, get out of here!
HAHAHAHA you didn't really think we let quitters off that easily did you?
Boy's get the PLANK!!!''')
                    time.sleep(3)
                    restart()
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
                # ability to quit out of game
                if user_input_coords.lower() == 'quit':
                    print('''
I knew you were just a landlover, I could smell the scurvy from here!
Men, get the plank, we'll have some fun before we fight!''')
                    time.sleep(3)
                    restart()
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
