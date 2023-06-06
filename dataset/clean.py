import pandas as pd

df = pd.read_csv("contestants.csv")

selected_columns = ['year', 'to_country','performer', 'song', 'place_final', 'points_final']
extracted_df = df[selected_columns]

print(extracted_df)  # Display the extracted data
extracted_df.to_csv('extracted_contestants.csv', index=True)  # Save the extracted data to a new CSV file


