import pandas as pd
import re

df = pd.read_csv("contestants.csv")

#artist
artist_columns = ['performer']
artist_df = df[artist_columns]
artist_df = artist_df.drop_duplicates()
artist_df['performer'] = artist_df['performer'].apply(lambda x: re.sub(',', '', str(x)))
artist_df.to_csv('artists.csv', index=False)

#counties
countries_colmns = ['to_country']
countries_df = df[countries_colmns]
countries_df = countries_df.drop_duplicates()
countries_df.to_csv('countries.csv', index=False)

#songs
songs_colmns = ['year', 'to_country', 'song']
songs_df = df[songs_colmns]
songs_df = songs_df.drop_duplicates()
songs_df['song'] = songs_df['song'].apply(lambda x: re.sub(',', '', str(x))) #FIX
songs_df.to_csv('songs.csv', index=False)

#oldsong
PYsongs_colmns = ['year','to_country', 'song', 'place_final', 'points_final']
PYsongs_df = df[PYsongs_colmns]
PYsongs_df = PYsongs_df[PYsongs_df['year'] <= 2019]
PYsongs_df.to_csv('previousYearsSongs.csv', index=False)

#new song
newsongs_colmns = ['year','to_country', 'song'] 
newSongs_df = df[newsongs_colmns]
newSongs_df = newSongs_df[newSongs_df['year'] > 2019]
newSongs_df.to_csv('upcommingYearSongs.csv', index=False)

#preforms
performs_colmns = ['performer','year', 'song', 'to_country']
performs_df = df[performs_colmns]
performs_df = performs_df.drop_duplicates()
performs_df['performer'] = performs_df['performer'].apply(lambda x: re.sub(',', '', str(x))) #FIX
performs_df.to_csv('performs.csv', index=False)
