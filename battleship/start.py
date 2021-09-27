from battleship.editscreen import clear_terminal
from battleship.editscreen import C
from battleship.setup import create_players
import time


# SETUP function - establishes parameters for game
def setup():
    clear_terminal()
    print("Good on ya, argh, we'll make a pirate out of ye yet!")
# USER OPTIONS LOGIC
# Grid dimension selection 6x6 or 10x10 message
    while True:
        try:
            # user input of desired dimension for board
            dimension_input = input('''
How brave are ye? Shall we play a full game or a little one?
Select a board size, enter '6' for a little one or '10' for normal:\n''')
            if dimension_input.lower() == 'quit':
                print('''
Argh! I see, you are not a true pirate, just a wannabe!
Time for you to walk the plank!''')
                time.sleep(3)
                start()
            else:
                dimensions = int(dimension_input)
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
                if (difficulty == 'quit'):
                    print('''
Hmm, did things just get a little too real for you? Gentlemen,
PREPARE the PLANK!!''')
                    time.sleep(3)
                    start()
                elif ((difficulty != 'e')
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
                print(C.RED + 'Controls' + C.END)
                print('''Follow the prompts that appear on the screen to
position your ships or to take shots. If you wish to turn and run at any
point you can, just enter 'quit' into any of the input fields. Be warned,
quitters do not get a second chance!''')
                print()
                play = 'N'
        except Exception:
            clear_terminal()
            print('''
    Argh! you woke me up for nothin... I should make ye walk the plank...
    Wait, shall we try that again?\n''')
            play = 'N'

    setup()
