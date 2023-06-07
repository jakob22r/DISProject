def select_winner_songs_last10years(conn):
    cur = conn.cursor()
    sql = """
    SELECT * From s.songs NATURAL JOIN s.PreviousYearsSongs AS pys
    WHERE year > 2009 and year < 2020 AND pys.placingInFinal = 1 ORDER BY year DESC
    """
    cur.execute(sql)
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset #Return to caller


def select_null_points(conn):
    cur = conn.cursor()
    sql = """SELECT p.year, p.countryName, p.title FROM s.previousyearssongs p
    WHERE p.pointsInFinal = 0;"""
    cur.execute(sql)
    tuple_resulset = cur.fetchall()
    return tuple_resulset

def select_winner_by_year(conn, year):
    cur = conn.cursor()
    sql = """SELECT p.countryName, p.title FROM s.previousyearssongs p
    WHERE p.placingInFinal = 1 AND p.year = %s;"""
    cur.execute(sql, (year,))
    tuple_resultset = cur.fetchall()
    return tuple_resultset
