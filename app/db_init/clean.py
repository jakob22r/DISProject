import pandas as pd
import re
import numpy as np

def cleanPerformer(df):
    df['performer'] = df['performer'].apply(lambda x: re.sub(',', '', str(x)))
    df['performer'] = df['performer'].apply(lambda x: re.sub("'", '', str(x)))
    return df

def cleanSong(df):
    df['song'] = df['song'].apply(lambda x: re.sub(',', '', str(x)))
    df['song'] = df['song'].apply(lambda x: re.sub("'", '', str(x)))
    return df

df = pd.read_csv("contestants.csv")

df = df.dropna(subset=['song', 'performer', 'place_final', 'points_final'])
df = df.drop_duplicates()
df['points_final'] = df['points_final'].round().astype(int)
df['place_final'] = df['place_final'].round().astype(int)

# Apply the filter to remove rows with two consecutive commas
all_used_cols = ['year','to_country', 'song', 'place_final', 'points_final', 'performer']
df = df[all_used_cols]

#artist
artist_columns = ['performer']
artist_df = df[artist_columns]
artist_df = artist_df.drop_duplicates()
artist_df = cleanPerformer(artist_df)

with open('artist.sql', 'w', encoding='utf8') as artistSQL:
    for row in range(len(artist_df)):
        sql_statement = f"INSERT INTO s.artists (artistName) VALUES ('{str(artist_df.iloc[row].loc['performer'])}');\n"
        artistSQL.write(sql_statement)    

#countries
countries_colmns = ['to_country']
countries_df = df[countries_colmns]
countries_df = countries_df.drop_duplicates()

with open('countries.sql', 'w', encoding='utf8') as countriesSQL:
    for row in range(len(countries_df)):
        sql_statement = f"INSERT INTO s.countries (countryName) VALUES ('{str(countries_df.iloc[row].loc['to_country'])}');\n"
        countriesSQL.write(sql_statement) 

#songs
songs_colmns = ['year', 'to_country', 'song']
songs_df = df[songs_colmns]
songs_df = songs_df.drop_duplicates()
songs_df = cleanSong(songs_df)

with open('songs.sql', 'w', encoding='utf8') as songsSQL:
    for row in range(len(songs_df)):
        year = songs_df.iloc[row].loc['year']
        countryName = str(songs_df.iloc[row].loc['to_country'])
        title = str(songs_df.iloc[row].loc['song'])
        sql_statement = f"INSERT INTO s.songs (year, countryName, title) VALUES ({year}, '{countryName}', '{title}');\n"
        songsSQL.write(sql_statement)

#oldsong
PYsongs_colmns = ['song', 'year', 'place_final', 'points_final', 'to_country']
PYsongs_df = df[PYsongs_colmns]
PYsongs_df = PYsongs_df.drop_duplicates()
PYsongs_df = PYsongs_df[PYsongs_df['year'] <= 2018]
PYsongs_df = cleanSong(PYsongs_df)

with open('previousyearssongs.sql', 'w', encoding='utf8') as PYsongsSQL:
    for row in range(len(PYsongs_df)):
        title = str((PYsongs_df.iloc[row]).loc['song'])
        year = (PYsongs_df.iloc[row]).loc['year']
        placingInFinal = PYsongs_df.iloc[row].loc['place_final']
        pointsInFinal = PYsongs_df.iloc[row].loc['points_final']
        countryName = str((PYsongs_df.iloc[row]).loc['to_country'])
        sql_statement = f"INSERT INTO s.previousyearssongs (title, year, placingInFinal, pointsInFinal, countryName) VALUES ('{title}', {year}, {placingInFinal}, {pointsInFinal}, '{countryName}');\n"
        PYsongsSQL.write(sql_statement)

#new song
newsongs_colmns = ['song', 'year','to_country'] 
newSongs_df = df[newsongs_colmns]
newSongs_df = newSongs_df[newSongs_df['year'] > 2018]
newSongs_df = cleanSong(newSongs_df)

with open('upcomingyearsongs.sql', 'w', encoding='utf8') as newSongsSQL:
    for row in range(len(newSongs_df)):
        title = str((newSongs_df.iloc[row]).loc['song'])
        year = (newSongs_df.iloc[row]).loc['year']
        countryName = str((newSongs_df.iloc[row]).loc['to_country'])
        sql_statement = f"INSERT INTO s.upcomingyearsongs (title, year, countryName) VALUES ('{title}', {year}, '{countryName}');\n"
        newSongsSQL.write(sql_statement)

#preforms
performs_colmns = ['performer','year', 'to_country', 'song']
performs_df = df[performs_colmns]
performs_df = performs_df.drop_duplicates()
performs_df = cleanPerformer(performs_df)
performs_df = cleanSong(performs_df)

with open('performs.sql', 'w', encoding='utf8') as performsSQL:
    for row in range(len(performs_df)):
        artistName = str(performs_df.iloc[row].loc['performer'])
        year = (performs_df.iloc[row]).loc['year']
        countryName = str((performs_df.iloc[row]).loc['to_country'])
        title = str((performs_df.iloc[row]).loc['song'])
        sql_statement = f"INSERT INTO s.performs (artistName, year, countryName, title) VALUES ('{artistName}', {year}, '{countryName}', '{title}');\n"
        performsSQL.write(sql_statement)