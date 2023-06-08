from . import forms, queries, models

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

def user_not_exists(conn, userid):
    cur = conn.cursor()
    sql = """SELECT u.userid FROM s.users u WHERE u.userid=%s;"""
    cur.execute(sql, (userid,))
    tuple_resultset = cur.fetchall()
    
    if len(tuple_resultset) == 0:
        return True
    
    return False

def lookup_user(conn, username):
    print("Lookup user")
    cur = conn.cursor()
    sql = """SELECT userID, password FROM s.users WHERE userName = %s;"""
    cur.execute(sql, (username,))  
    res = cur.fetchone()
    cur.close()
    return res

def count_votes(conn):
    cur = conn.cursor()
    sql = """SELECT v.countryName, v.title, COUNT(v.userid)
            FROM s.votes v 
            GROUP BY v.countryName, v.title
            ORDER BY (COUNT(v.userid)) DESC;"""
    cur.execute(sql)
    tuple_resultset = cur.fetchall()
    return tuple_resultset

def add_vote(conn, userID, title):
    cur = conn.cursor()
    #first find the country associated with the song
    country_sql = """SELECT u.countryName FROM s.upcomingyearsongs u
                    WHERE u.title=%s;"""
    cur.execute(country_sql, (title,))
    countryName = cur.fetchall()

    #now we add the vote to the database
    sql = """INSERT INTO s.votes(userID, title, year, countryName)
	        VALUES (%s, %s, 2019, %s);"""
    cur.execute(sql, (userID, title, countryName))
    res = cur.fetchall()
    return res


def upcomingsongs_titles(conn):
    cur = conn.cursor()
    sql = """SELECT u.title FROM s.upcomingyearsongs u;"""
    cur.execute(sql)
    res = cur.fetchall()
    return res