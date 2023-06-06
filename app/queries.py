def select_winner_songs_last10years(conn):
    cur = conn.cursor()
    sql = """
    SELECT year, artist, song FROM PreviousYearsSongs
    WHERE year > 2012 and year < 2023 
    """
    cur.execute('SELECT * FROM books;')
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset #Return to caller