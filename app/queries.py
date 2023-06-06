def select_winner_songs_last10years(conn):
    cur = conn.cursor()
    sql = """
    SELECT * From s.songs NATURAL JOIN s.PreviousYearsSongs AS pys
    WHERE year > 2009 and year < 2020 AND pys.placingInFinal = 1 ORDER BY year DESC
    """
    cur.execute(sql)
    tuple_resultset = cur.fetchall()
    len = 0
    for item in tuple_resultset:
        len = len + 1
    cur.close()
    return tuple_resultset, len #Return to caller