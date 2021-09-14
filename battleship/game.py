# game file to contain game class and operations
from battleship.editscreen import clear_terminal
from battleship.editscreen import C
import time


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
        from battleship.start import setup
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
