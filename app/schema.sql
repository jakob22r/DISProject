-- \i schema_drop.sql

CREATE TABLE IF NOT EXISTS Artists
    (artistName CHAR(100),
    PRIMARY KEY (artistName));

CREATE TABLE IF NOT EXISTS Countries
    (countryName CHAR(50),
    PRIMARY KEY (countryName));  

CREATE TABLE IF NOT EXISTS Songs
    (year INTEGER,
    countryName CHAR(50) NOT NULL,
    title CHAR(50),
    PRIMARY KEY (year, countryName, title),
    FOREIGN KEY (countryName) REFERENCES Countries
    ON DELETE NO ACTION);

CREATE TABLE IF NOT EXISTS Performs
    (artistName CHAR(100),
    year INTEGER,
    title CHAR(50),
    countryName CHAR(50),
    PRIMARY KEY (artistName, title, year, countryName),
    FOREIGN KEY (artistName) REFERENCES Artists,
    FOREIGN KEY (title, year, countryName) REFERENCES Songs);

CREATE TABLE IF NOT EXISTS PreviousYearsSongs
    (title CHAR(50),
    year INTEGER,
    placingInFinal INTEGER DEFAULT NULL,
    pointsInFinal INTEGER DEFAULT NULL,
    countryName CHAR(50),
    PRIMARY KEY (title, year, countryName, placingInFinal),
    FOREIGN KEY (title, year, countryName) REFERENCES Songs);

CREATE TABLE IF NOT EXISTS UpcomingYearSongs
    (title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    PRIMARY KEY (title, year, countryName),
    FOREIGN KEY (title, year, countryName) REFERENCES Songs);

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

-- put this in its own file
-- \COPY Artists FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/artists.csv' DELIMITER ',';
-- \COPY Countries (countryName) FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/countries.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
-- \COPY Songs (year, countryName, title) FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/songs.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
\COPY Performs FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/performs.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
\COPY PreviousYearsSongs FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/previousYearsSongs.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';
\COPY UpcomingYearSongs FROM '/Users/jakobsve/Documents/GitHub/DISProject/dataset/upcommingYearSongs.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF-8';

-- yet to be made data
--COPY Users FROM '/dataset/users.csv' DELIMITER ',';
--COPY Votes FROM '/dataset/votes.csv' DELIMITER ',';