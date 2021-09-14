# blank file to contain blank board class
from battleship.board import Board


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
