# Calico Jack

## Introduction

Calico Jack is a browser based game built in Python. It is based on the classic game of Battleships and is themed loosely around the infamous pirate Calico Jack and the night he was captured by Jonathan Barnet.

As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

## Insert screenshot of game

[View the live website on Heroku](https://calico-jack.herokuapp.com/)
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents


## UX
### The Strategy Plane
* Calico Jack is intended to be a fun strategy battleships game, suitable for individual users looking to play a game for short or medium periods of time. Given the limitations of the terminal based interface, care will need to be taken to incorporate visual stimulous, along with an engaging narrative to convey an element of fun to the user. 

#### Site Goals
* To provide users with a fun and simple strategy game to play.
* To provide users with alternative board dimensions to increase or decrease the time commitment required to complete a game.
* To provide users with alternative difficulty levels to increase or decrease the challenge offered.

### User Stories
* As a user I want an online version of battleships to play
* As a user I want to be able to control the amount of time it takes to play the game.
* As a user I want to challenge myself against a tough computer opponent.

### The Scope Plane
**Features planned:**
* As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal emulator, the site should site be visually stimulating and clear to the user that it is a game.
* Three difficulty levels should be available to the user.
    * Easy - Normal - Hard
* Two different size boards should be available to the user.
    * The traditional 10 tile by 10 tile board size along with a smaller board for quicker gameplay.

### The Structure Plane

User Story:

> As a user, I want a fun and simple strategy game to play

Acceptance Criteria:
* It should be clear to the user that this is a game, what it is about and how to play.

Implementation:
* The layout, use of colour and in game narrative will all be designed to immerse the user into the game world. Conveying a sense of fun to the user through out the interactions with the game. Instructions on how to play will be available at the start of the game, along with clear prompts and validation for each user input.

User Story:

> As a user, I want to be able to control the amount of time it takes to play the game.

Acceptance Criteria:
* The user should be able to control the amount of time it takes to play a game.

Implementation:
* The user will have the ability to choose between two different board sizes. The smaller board will contain a smaller number of potential target tiles, along with a smaller number of ships to potentially hit, thus reducing the amount of time required to complete the game. The larger board size will contain more ships, which combined with the larger number of potential tile targets will extend the game play. The three difficulty levels offered will also impact the game time due to the algorithm controling how the AI selects its targets. Harder difficulty levels will potentially result in shorter time periods required to play the game.

User Story:

> As a user, I want to challenge myself against a tough computer opponent.

Acceptance Criteria:
* The user should have the option to play the game on different difficulty level settings.

Implementation:
* The user will have the ability to choose between three different difficulty levels. Each level will alter the challenge that the AI player provides.

#### Opportunities
Arising from user stories
| Opportunities | Importance | Viability / Feasibility
| ------ | :------: | :------: |
| ** Provide a fun game environment ** | 5 | 5 |
| ** Provide different difficulty levels ** | 5 | 5 |
| ** Provide ability to control the time the game takes ** | 5 | 5 |

### The Skeleton Plane
#### Wireframe mockups
Given that the application will be run within a terminal emulator provided within the template, there are limited options available with regards to the layout of the webpage itself. Early on within the development of the theme, I located a suitable background graphic on iStock. In order to position the terminal appropriately for the background graphic, and keeping user experience in mind, I decided to center the terminal horizontally on the screen. This positions the terminal window within the lower part of the rail around the ship in the background graphic. The run program button was centrally positioned to above the terminal window to emphasis its importance.

![Home Page Wireframe](/assets/wireframes/homepage-wireframe-900.png)

For the terminal window itself, I also produced a wireframe in the well known design package Microsoft Excel. Whilst not tradionally used for this purpose, the terminal window dimensions of 80 columns wide by 24 rows high provided a restriction that I could duplicate in excel easily. This enabled me to work out the spacing requirements and dimensions of the elements on screen during the gameplay. Given that all the elements that would be displayed in the terminal are ASCII characters, creating a 80 x 24 grid in excel with one character per tile it enabled me to easily see if I could fit the total information required on each line. This was especially useful whilst calculating how to print the two game boards with a scoreboard in between them, given the line by line method in which the terminal prints.

![Terminal Game Play Wireframe](/assets/wireframes/wireframe-game-screen.png)

#### Logic Flow
In order to figure out the logical steps required within the game, along with gaining an understanding of how the different game elements would interact, I created a flow chart detailing the individual steps for the game. Given the scope of the game logic involved the full flow chart resulted in a large image. The full image can be viewed here [Logic Flow Diagram](/assets/logic/logic-flow-full.png)

The game logic can be broken down into three distinction sections. The initial setup of the game, taking a turn and checking the turn result before moving to the next player. For ease of reference I have broken up the logic flow diagram into these three sections.

##### Setup Logic

![Setup Logic](/assets/logic/logic-flow-setup.png)

##### Target Selection and Validation

![Target Logic](/assets/logic/logic-flow-target-validation.png)

##### Game Loop

![Game Turn Loop](/assets/logic/logic-flow-game-loop.png)

### The Surface Plane

#### Design

Once I was happy with the overall layout of the page, I created a full colour mockup within Adobe XD.

![Full Colour Mockup](/assets/wireframes/full-colour-mockup-900.png)

## Features

## Future Enhancements

## Testing

### Testing Strategy

#### Testing Overview

#### Validator Testing

#### Notable Bugs

## Deployment

## Credits

### Content

### Acknowledgements



![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome MattBCoding,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
