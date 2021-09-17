# Test Cases and Execution Report

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
    * [game.py file top](/assets/screenshots/game1.png) 
    * [game.py file lower](/assets/screenshots/game2.png) 
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
The orientation selection 

![Test Case 006c](/assets/testing/test-case-006c.png)

## Test Case 007

![Test Case 007](/assets/testing/test-case-007.png)

![Test Case 007b](/assets/testing/test-case-007b.png)

## Test Case 008

![Test Case 008](/assets/testing/test-case-008.png)

## Test Case 009

![Test Case 009](/assets/testing/test-case-009.png)

## Test Case 010

![Test Case 010](/assets/testing/test-case-010.png)

## Test Case 011

![Test Case 011](/assets/testing/test-case-011.png)
