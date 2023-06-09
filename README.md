# Overall
This project includes a web-application for a Eurovision Fanclub, developed using Flask and PostgreSQL 
for the Databases and Informations Systems course at UCPH 2023. For the frontend CSS styling, we use Bootstrap.

# Setup

## Requirements
### Prerequisites 
* Make sure to have postgreSQL installed and working with psql in the command line

### Installing requirements
Make sure the the modules specified in requirements.txt are installed. To do that run:

>$ pip install -r requirements.txt

It is recomended to install the requirements in a virtual environments. See https://virtualenv.pypa.io/en/latest/ 
for further documentation on virtual environments. 

## Initializing the database
1. Navigate to app/database.ini and configure your database with the proper settings. Remember to enter your password in database.ini
2. To load data into the database, navigate to the db_init directory and run schema.sql 
(Note that schema.sql will drop the existing schema 's' if a such exists)

Side note: In db_init clean.py is used to re-generate some of the .sql files from the dataset contestants.csv
The necessary sql has already been generated, and hence it should not be necessary to re-run clean.py

### Dataset used
The dataset used in the web application is downloaded from https://github.com/Spijkervet/eurovision-dataset/releases. 
The repository contains information about winners, placings and distibution of point from 1956-2019. 

Our database is built from the contestants.csv. In order to impliment meaningfull features such as allowing users 
to vote for their favourite song in the upcoming contest, the web server's historical setting is somewhere in april 2019,
before the show in Tel Aviv of that year.

# Running and interacting

## Running the web-application
Host and port for the web server can be configured in run.py.
To start the web server navigate to the app directory and execute python3 run.py
The actual project, html, css and routing is located in the subdirectory project
This will start the web server at the specified host and port. 

## Login
All pages except the front page are only accessible for members. Either use one of the following users to login

### Credentials
Username | Password
* Emily     hej1234
* Jakob     kodeordet
* Anders    sortKaffe
* test_usr  uis

or optionally you can create your own user to interact with the web server. Simply press 'Sign up' on the 'Login' page. 
From there you have to pick a username and a password, then all features of the web page is available.
Note that passwords are SHA-256 hashed!

## Features and interaction of the web application
* My profile (Only visible in menu bar when logged in)
    * See how many songs you have voted for this year
    * Update your password (Will check that old password is correct, and that new passwords match)
    * Delete your user profile

* Stats (Only accessible when logged in)
    * View the winners of the previous 10 years
    * View the all-time worst song (i.e. songs who got 0 points in the final)
    * Use the search function to query a year and find the Country and song who won that year

* Vote (Only accessible when logged in)
    * View the votes of the users
    * View what song(s) and country(ies) you have voted on 
    * Cast your own vote for your favourite song. 

* Login (Only visible from front page or when not logged in)
    * Login (i.e. authenticate a registered user) with the provided username and password
    * Click the Create user hyperlink

* Create user
    * Fillout the form to register a new user in the database 
    (Will check that userId and userName is not already taken)

* Logout (Button only visable in top right corner when logged in)
    * Logs the current user profile out

### Backend SQL
The backend SQL statements executed upon performing the abovementioned interactions are available in queries.py


