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

### The Surface Plane

#### Design

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
