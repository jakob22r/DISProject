--drop view commands, if any

--DROP schema IF EXISTS s CASCADE;

DROP TABLE IF EXISTS s.Votes CASCADE;
DROP TABLE IF EXISTS s.PreviousYearsSongs CASCADE;
DROP TABLE IF EXISTS s.UpcomingYearSongs CASCADE;
DROP TABLE IF EXISTS s.Users;
DROP TABLE IF EXISTS s.Songs CASCADE;
DROP TABLE IF EXISTS s.Performs CASCADE;
DROP TABLE IF EXISTS s.Countries; 
DROP TABLE IF EXISTS s.Artists;