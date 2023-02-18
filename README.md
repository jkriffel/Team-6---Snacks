**Software Engineering Project Spring 2023 - Team 6**
* Last Edited: 2/17/23
* Project Contributors: Zachary Anderson, Joshua Hollis, James Riffel, Maci Danner, Michael Logal, and Drew Grove

**Project Description**:
* A laser tag game interface including splash, player entry, and game action screens.

**File Breakdown**:
* proton.py - Essentially the main class. This class initially displays the splash screen and allows the user to move between it and the player screen.
* textbox.py - The textbox/"player" class. This class is used for the collection and organization of player data (id, firstname, lastname, and codename) 
               that is entered on the player entry screen.
* connect.py - 
* player.py -
* main.py - This class imports the Flask web framework.
* button.py - The button class. This class allows for the creation of buttons that when pressed, perform an action assigned to them in proton.py.
* player.sql - This sql file creates a player table consisting of ID, firstname, lastname, and codename. There are also two test "players" inserted into the table.
* requirements.txt - Allows us to locally host Heroku using Flask.
* Assets file - Contains images as well as font specifications for the player and splash screens.
* Pycache file - Contains auto-generated cache files generated by python files.
