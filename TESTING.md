# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

The full testing spreadsheet containing all the tests performed during the testing phase of development can be found [here](/assets/testing/test-schedule.pdf)

## Test Case 001

![Test Case 001](/assets/testing/test-case-001.png)

### Python Validation
The Python code was checked using the pep8 validator available at [pep8online.com](https://pep8online.com). No errors were reported by the validator. The following files however did include warnings regarding a line break before binary operator
* list of files with warnings
    * board.py - 2 warnings
    * comp.py - 1 warning
    * game.py - 27 warnings
    * player.py - 2 warnings
    * setup.py - 4 warnings
The warning suggests that there should not be a line break before a binary operator, however on checking with the python pep 8 guidelines it explicitly states that the line break should be before the binary operator. 

The point in the PEP8 guidelines can be found [here](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)

* Screenshots of the validator reports are here 
    * [blank.py file](/assets/screenshots/blank.png) 
    * [board.py file](/assets/screenshots/board.png) 
    * [boat.py file](/assets/screenshots/boat.png) 
    * [comp.py file](/assets/screenshots/comp.png) 
    * [editscreen.py file](/assets/screenshots/editscreen.png) 
    * [game.py file top](/assets/screenshots/game.png)
    * [player.py file](/assets/screenshots/player.png) 
    * [run.py file](/assets/screenshots/run.png) 
    * [setup.py file](/assets/screenshots/setup.png) 
    * [start.py file](/assets/screenshots/start.png)

### CSS Validation
Whilst I only added a couple of lines of custom CSS to the Code Institute provided template, I tested the site using the Jigsaw CSS Validator service which returned no errors. Two warnings related to custom prefixes were identified.

The full CSS Validator report is available here on the [CSS Validator Site](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcalico-jack.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Validator Report](/assets/testing/css-validator.png)

### HTML Validation
In order to place the svg background onto the site, I inserted a div with a class name of background and pasted the svg code from Adobe Illustrator. This was the only alteration made to the Code Institute provided template.

When running the site through the HTML validator it flags 14 errors. The errors are relating to the template itself and not the elements I created. The errors that do appear relate to how the template is combining two different HTML files. As we are restricted from manipulating the template I am prevented from attempting to resolve these errors.

The full report is available here on the [HTML Validator Site](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcalico-jack.herokuapp.com%2F)

## Test Case 002

![Test Case 002](/assets/testing/test-case-002.png)

### Start Menu Functionality
The start menu input was tested for the correct validation of the user input. On correct input the screen will redirect to the correct screen. On incorrect input the input validation correctly displays an error message to the user to provide guidance on how to move on before repeating the initial input message.

## Test Case 003

![Test Case 003](/assets/testing/test-case-003.png)

### Instruction Screen Functionality
Input validation was also tested on the instructions screen along with testing that the user could launch the game from the screen. On incorrect input the screen displays the correct error message with guidance on how to correctly input the required values. On correct input the desired functionality proceeded as designed.

## Test Case 004

![Test Case 004](/assets/testing/test-case-004.png)

### Board Size Selection
The user is provided the ability in line with the user stories to select between two different board sizes. This provides the user the ability to control the time required to play the game. The game was tested to ensure a board of the correct size would ultimately display, and that the game recognised the dimensions of the board. The labelling of the board rows and columns was tested to ensure they correctly displayed inline with the dimensions of the board.

## Test Case 005

![Test Case 005](/assets/testing/test-case-005.png)

### Board Size Selection - Input Validation
The input validation was tested to ensure that only a correct input would allow the game to proceed, whilst incorrect inputs were handled correctly. On a correct input, the corresponding board size would display.

## Test Case 006

![Test Case 006](/assets/testing/test-case-006.png)

### Ship Creation and Placement 6x6 board
Within the ship creation and placement functionality there were a number of different areas of functionality that required testing. This was split over further sub sections where required. Initially required functionality was tested to be performing correctly, such as the correct number of ships being created for the size of the board, the ships having the correct names and size.

Automatic orientation of ships was tested by attempting to place ships in locations where they would only fit in the one direction. 

On completion of positioning the ships the game successfully enters the target selection mode.

![Test Case 006b](/assets/testing/test-case-006b.png)

### Ship Creation and Placement 6x6 board
The orientation selection functionality was tested to ensure that the ships would be placed in the orientation selected by the user. The orientation was tested to ensure that the game recognised when ships would overlap, or go off the board. It was also tested to ensure that in cases where only one orientation could be selected the ship would be automatically placed.

![Test Case 006c](/assets/testing/test-case-006c.png)

### Ship Creation and Placement 6x6 board
Once functionality was confirmed to be working, the input for ship location and orientation were tested to ensure the input validation captured any incorrect inputs and handled them correctly. During this phase a small bug was detected relating to the function that checked if the coordinates entered were on the board or not. It was a simple fix achieved through refactoring the code for the check to seperate out the on board check from the printing of the boards themselves. 

## Test Case 007

![Test Case 007](/assets/testing/test-case-007.png)

### Ship Creation and Placement 10x10 board
As there are two board sizes available within the game it was important to check the functionality on both sizes. This was done to ensure that the functionality performed in the same manner for both boards.
In the first part of testing on the 10x10 board, ship placement was tested for detection of automatic orientation and placement. 

![Test Case 007b](/assets/testing/test-case-007b.png)

### Ship Creation and Placement 10x10 board
For the second part of the 10x10 board testing, ship placement was tested to ensure the correct detection of board limits along with other ships. This was to ensure users could not place ships off the board and that ships could not overlap.

The ship creation and placement tests were repeated for lowercase entries and on all difficulties to ensure no differences occured.

## Test Case 008

![Test Case 008](/assets/testing/test-case-008.png)

### Shot Recognition - Game Turn Loop - Easy Difficulty
Initially a 10x10 board was used to test the shot location input validation. Various incorrect entries were submitted to ensure that off board locations, or incorrect entries were detected and handled correctly.
For valid inputs, tests were performed to ensure that the shot outcome was successfully processed and displayed to the user. For this the boards were visually confirmed to have updated with the correct location, messaging to the user conveyed the correct message corresponding to the shot outcome, and the symbol updated on the board to indicate the result was correct.
AI shot selection was also tested alongside user shot recognition. The AI shot pattern was tested to ensure that the easy mode selected targets at random, and that each shot was a valid shot. This was manually checked by counting the number of shots the AI had taken after each round to ensure the number increased by 1. The outcome of the AI shot was tested to ensure both the correct message to the user displayed along with the board being updated correctly.
The game was completed during each round of testing to ensure that the scoreboard updated correctly and that the win/lose condition correctly triggered and displayed.

## Test Case 009

![Test Case 009](/assets/testing/test-case-009.png)

### Shot Recognition - Game Turn Loop - Normal Difficulty
The input validation for shot selection was also tested with a normal difficulty level selected to ensure no differences in results occured. Once again, various incorrect entries were made to check off board locations and invalid input formats. This was tested to ensure all input validation methods continued to perform as expected on the different difficulty level.
AI shot selection was tested through multiple rounds of the game to ensure the correct shot selection pattern was apparent. For normal difficulty the AI should randomly select a target until it achieves a hit. Once a hit has been detected it should target the neighbouring tiles in a cross formation, one up, one right, one down and one left. User ships locations were deliberately placed around the edge of the board to ensure that the AI recognised that it could not select locations in the predefined pattern of shots.

## Test Case 010

![Test Case 010](/assets/testing/test-case-010.png)

### Shot Recognition - Game Turn Loop - Hard Difficulty
Again input validation for shot selection was tested with a hard difficulty level selected to ensure no differences in results occured.
AI shot selection was tested through multiple rounds of the game to ensure the correct pattern emerged. For hard difficulty the AI should evaluate the board and the remaining ships to calculate the probability of a ship being in a particular location. For the first shot, this should result in the top left of the middle four tiles being selected. From there it will recalculate the probability of a ship being in the remaining tiles for each round, once it finds a ship, it will target the surrounding tiles similar to the manner in which the normal difficulty does.
For each round of testing the game was completed to ensure the scoreboard updated correctly and the win/lose condition triggered at the appropriate point.

## Test Case 011

![Test Case 011](/assets/testing/test-case-011.png)

### Shot Recognition - Game Turn Loop - 6x6 board
Test cases 8 through 10 were repeated for the 6x6 board to ensure no differences were detected in the responses received. 

To navigate back to the main README click [here](README.md)