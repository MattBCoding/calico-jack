# editscreen file to contain colours class and clear terminal function
import os


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
    '''
    C class contains the terminal color shortcuts
    for use when printing things to the terminal
    '''
    END = '\33[0m'
    RED = '\33[91m'
    YELLOW = '\33[93m'
    BGBLUE = '\33[44m'


def restart():
    from battleship.start import start
    start()
