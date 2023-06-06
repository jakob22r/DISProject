\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Artists
    (artistName CHAR(50),
    PRIMARY KEY (artistName));

CREATE TABLE IF NOT EXISTS Countries
    (countryName CHAR(50),
    PRIMARY KEY (countryName));  

CREATE TABLE IF NOT EXISTS Songs
    (title CHAR(50),
    year INTEGER,
    countryName CHAR(50) NOT NULL,
    PRIMARY KEY (title, year, countryName),
    FOREIGN KEY (countryName) REFERENCES Countries
    ON DELETE NO ACTION);

CREATE TABLE IF NOT EXISTS Performs
    (artistName CHAR(50),
    title CHAR(50),
    year INTEGER,
    PRIMARY KEY (artistName, title, year),
    FOREIGN KEY (artistName) REFERENCES Artists,
    FOREIGN KEY (title, year) REFERENCES Songs);

CREATE TABLE IF NOT EXISTS PreviousYearsSongs
    (title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    rank INTEGER,
    PRIMARY KEY (title, year, countryName, rank),
    FOREIGN KEY (title, year) REFERENCES Songs,
    FOREIGN KEY (countryName) REFERENCES Countries);

CREATE TABLE IF NOT EXISTS UpcomingYearSongs
    (title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    PRIMARY KEY (title, year, countryName),
    FOREIGN KEY (title, year) REFERENCES Songs,
    FOREIGN KEY (countryName) REFERENCES Countries);

CREATE TABLE IF NOT EXISTS Users
    (password CHAR(50),
    userName CHAR(50),
    userID CHAR(20),
    PRIMARY KEY (userID));

CREATE TABLE IF NOT EXISTS Votes
    (userID CHAR(20),
    title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    PRIMARY KEY (userID, title, year, countryName),
    FOREIGN KEY (userID) REFERENCES Users,
    FOREIGN KEY (title, year, countryName) REFERENCES UpcomingYearSongs);