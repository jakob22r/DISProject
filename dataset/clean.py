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
df.to_csv("aud.csv", index=False)

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
PYsongs_df = cleanSong(PYsongs_df)
PYsongs_df = PYsongs_df[PYsongs_df['year'] <= 2018]

with open('previousyearssongs.sql', 'w', encoding='utf8') as PYsongsSQL:
    for row in range(len(PYsongs_df)):
        title = str((PYsongs_df.iloc[row]).loc['song'])
        year = (PYsongs_df.iloc[row]).loc['year']
        placingInFinal = PYsongs_df.iloc[row].loc['place_final'] #måske () problem
        pointsInFinal = PYsongs_df.iloc[row].loc['points_final']
        countryName = str((PYsongs_df.iloc[row]).loc['to_country'])
        sql_statement = f"INSERT INTO s.previousyearssongs (title, year, placingInFinal, pointsInFinal, countryName) VALUES ('{title}', {year}, {placingInFinal}, {pointsInFinal}, '{countryName}');\n"
        PYsongsSQL.write(sql_statement)


#PYsongs_df.to_csv('previousYearsSongs.csv', index=False)

#new song
newsongs_colmns = ['song', 'year','to_country'] 
newSongs_df = df[newsongs_colmns]
newSongs_df = newSongs_df[newSongs_df['year'] > 2018]
newSongs_df.to_csv('upcommingYearSongs.csv', index=False)

#preforms
performs_colmns = ['performer','year', 'to_country', 'song']
performs_df = df[performs_colmns]
# performs_df = df[performs_colmns].replace('', pd.NA).dropna()
# performs_df = df[performs_colmns].replace(',,', pd.NA).dropna()
# performs_df = df[performs_colmns]
performs_df = performs_df.drop_duplicates()
performs_df['performer'] = performs_df['performer'].apply(lambda x: re.sub(',', '', str(x))) #FIX
performs_df['song'] = performs_df['song'].apply(lambda x: re.sub(',', '', str(x))) #FIX
performs_df.to_csv('performs.csv', index=False)
