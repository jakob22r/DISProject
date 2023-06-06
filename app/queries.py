def select_winner_songs_last10years(conn):
    cur = conn.cursor()
    sql = """
    SELECT * From songs
    WHERE year > 2012 and year < 2020
    """
    cur.execute(sql)
    tuple_resultset = cur.fetchall()
    len = 0
    for item in tuple_resultset:
        len = len + 1
    cur.close()
    return tuple_resultset, len #Return to caller