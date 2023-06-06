import pandas as pd

df = pd.read_csv("contestants.csv")

#artist
artist_columns = ['performer']
artist_df = df[artist_columns]
artist_df = artist_df.drop_duplicates()
artist_df.to_csv('artists.csv', index=True)

#counties
countries_colmns = ['to_country']
countries_df = df[countries_colmns]
countries_df = countries_df.drop_duplicates()
countries_df.to_csv('countries.csv', index=True)

#songs
songs_colmns = ['year','to_country', 'song']
songs_df = df[songs_colmns]
songs_df.to_csv('songs.csv', index=True)


#oldsong
PYsongs_colmns = ['year','to_country', 'song', 'place_final', 'points_final']
PYsongs_df = df[PYsongs_colmns]
PYsongs_df = PYsongs_df[PYsongs_df['year'] <= 2023]
PYsongs_df.to_csv('previousYearsSongs.csv', index=True)

#new song
newsongs_colmns = ['year','to_country', 'song']
newSongs_df = df[newsongs_colmns]
PYsongs_df = newSongs_df[newSongs_df['year'] >= 2023]
PYsongs_df.to_csv('upcommingYearSongs.csv', index=True)

#preforms
performs_colmns = ['year','performer', 'song']
performs_df = df[performs_colmns]
performs_df.to_csv('performs.csv', index=True)
