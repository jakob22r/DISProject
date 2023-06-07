import pandas as pd
import re
import numpy as np


df = pd.read_csv("contestants.csv")
#df = df.replace('', pd.NA).dropna()
#df.dropna(inplace=True)


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
artist_df['performer'] = artist_df['performer'].apply(lambda x: re.sub(',', '', str(x)))
artist_df.to_csv('artists.csv', index=False)

#countries
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
PYsongs_colmns = ['song', 'year', 'place_final', 'points_final', 'to_country']
PYsongs_df = df[PYsongs_colmns]
PYsongs_df = PYsongs_df.drop_duplicates()
PYsongs_df['song'] = PYsongs_df['song'].apply(lambda x: re.sub(',', '', str(x))) #FIX
PYsongs_df = PYsongs_df[PYsongs_df['year'] <= 2018]
PYsongs_df.to_csv('previousYearsSongs.csv', index=False)

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
