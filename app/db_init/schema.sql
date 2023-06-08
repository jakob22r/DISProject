\i schema_drop.sql

CREATE schema s

CREATE TABLE IF NOT EXISTS s.Artists
    (artistName CHAR(100),
    PRIMARY KEY (artistName));

CREATE TABLE IF NOT EXISTS s.Countries
    (countryName CHAR(50),
    PRIMARY KEY (countryName));  

CREATE TABLE IF NOT EXISTS s.Songs
    (year INTEGER,
    countryName CHAR(50) NOT NULL,
    title CHAR(50),
    PRIMARY KEY (year, countryName, title),
    FOREIGN KEY (countryName) REFERENCES s.Countries
    ON DELETE NO ACTION);

CREATE TABLE IF NOT EXISTS s.Performs
    (artistName CHAR(100),
    year INTEGER,
    countryName CHAR(50),
    title CHAR(50),
    PRIMARY KEY (artistName, title, year, countryName),
    FOREIGN KEY (artistName) REFERENCES s.Artists,
    FOREIGN KEY (year, countryName, title) REFERENCES s.Songs);

CREATE TABLE IF NOT EXISTS s.PreviousYearsSongs
    (title CHAR(50),
    year INTEGER,
    placingInFinal INTEGER DEFAULT NULL,
    pointsInFinal INTEGER DEFAULT NULL,
    countryName CHAR(50),
    PRIMARY KEY (title, year, countryName, placingInFinal),
    FOREIGN KEY (year, countryName, title) REFERENCES s.Songs);

CREATE TABLE IF NOT EXISTS s.UpcomingYearSongs
    (title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    PRIMARY KEY (title, year, countryName),
    FOREIGN KEY (year, countryName, title) REFERENCES s.Songs);

CREATE TABLE IF NOT EXISTS s.Users
    (password VARCHAR(50),
    userName VARCHAR(50),
    userID INTEGER,
    PRIMARY KEY (userID));

CREATE TABLE IF NOT EXISTS s.Votes
    (userID INTEGER,
    title CHAR(50),
    year INTEGER,
    countryName CHAR(50),
    PRIMARY KEY (userID, title, year, countryName),
    FOREIGN KEY (userID) REFERENCES s.Users,
    FOREIGN KEY (title, year, countryName) REFERENCES s.UpcomingYearSongs);

-- Run scripts to insert data into tables
\i artist.sql
\i countries.sql
\i songs.sql
\i previousyearssongs.sql
\i upcomingyearsongs.sql
\i performs.sql
\i users.sql
\i votes.sql
