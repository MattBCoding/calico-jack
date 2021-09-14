# setup file to contain setup functions
import math
from battleship.player import Player
from battleship.comp import Comp
from battleship.blank import Blank
from battleship.game import Game
from battleship.boat import Boat


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
    # the order of largest ship first.
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
