# Software Engineering Project Spring 2023 - Team 6
Laser tag game created with Python and a Heroku database

## Table of Contents
* [General Info](#general-info)
* [Technologies Used](#general-info#technologies-used)
* [Setup](#general-info#setup)
* [File Descriptions](#general-info#file-descriptions)
* [Status](#general-info#status)

## General Info
* Project Contributors: Zachary Anderson, Joshua Hollis, James Riffel, Maci Danner, Michael Logal, and Drew Grove

## Technologies Used
Project created using:
* Python version: 3.11.1
* Pygame version: 2.1.3.dev8
* Pyscopg2 version: 2.9.5

## Features
* Splash Screen
* Player Entry Screen
* Game Action Screen (with countdown timer)

## Setup
* Pip-install python, pygame, psycopg2
* Run main.py to view the game

## File Descriptions
* button.py - The button class. This class allows for the creation of buttons that when pressed, perform an action assigned to them.
* database.py - This class handles interactions with the Heroku database including: connection testing, player creation, and codename retrieval.
* main.py - The main class which calls the separate screens.
* player_table.py - This class creates the player table and handles interactions with it. Players entered into the table (on the player screen) are added to 
                    the sql database (if they do not already exist). If a matching ID is entered, player codenames are auto-retrived from the database.
                    This class also displays and updates the timer for the player action screen.
* textbox.py - The textbox/"player" class. This class is used for the collection and organization of player data (id and codename) that is entered on 
               the player entry screen.
* Assets file - Contains images as well as font specifications for the player and splash screens.
* Pycache file - Contains auto-generated cache files generated by Python files.
* Screens file - Contains the splash, player, action, and countdown screens.

## Status
Project is in progress. Last Updated: 3/12/23
