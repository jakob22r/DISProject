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
    cur.close()
    return tuple_resulset

def select_winner_by_year(conn, year):
    cur = conn.cursor()
    sql = """SELECT p.countryName, p.title FROM s.previousyearssongs p
    WHERE p.placingInFinal = 1 AND p.year = %s;"""
    cur.execute(sql, (year,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def user_not_exists(conn, userid):
    cur = conn.cursor()
    sql = """SELECT u.userid FROM s.users u WHERE u.userid=%s;"""
    cur.execute(sql, (userid,))
    tuple_resultset = cur.fetchall()
    cur.close()
    if len(tuple_resultset) == 0:
        return True
    
    return False

def lookup_user_on_name(conn, username):
    print("Lookup user")
    cur = conn.cursor()
    sql = """SELECT userID, password FROM s.users WHERE userName = %s;"""
    cur.execute(sql, (username,))  
    res = cur.fetchone()
    cur.close()
    return res

def lookup_userpw_on_ID(conn, userID):
    print("Lookup user")
    cur = conn.cursor()
    sql = """SELECT password FROM s.users WHERE userID = %s;"""
    cur.execute(sql, (userID,))  
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
    cur.close()
    return tuple_resultset

def count_my_votes(conn, userID):
    cur = conn.cursor()
    sql = """SELECT v.countryName, v.title
            FROM s.votes v 
            WHERE v.userid = %s"""
    cur.execute(sql, (userID,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset
    


def add_vote(conn, userID, title):
    cur = conn.cursor()
    countryName = country_from_song(conn, title)
    #now we add the vote to the database
    sql = """INSERT INTO s.votes(userID, title, year, countryName)
	        VALUES (%s, %s, 2019, %s);"""
    cur.execute(sql, (userID, title, countryName))
    cur.close()
    return

def country_from_song(conn, title):
    print("Query title")
    print(title)
    cur = conn.cursor()
    country_sql = """SELECT u.countryName FROM s.upcomingyearsongs u
                    WHERE u.title=%s;"""
    cur.execute(country_sql, (title,))
    query_result = cur.fetchone()
    cur.close()
    if query_result != None:
        print("query result")
        print(query_result[0])
        return query_result[0]

def unique_vote(conn, title, userID):
    cur = conn.cursor()
    countryName = country_from_song(conn, title)
    sql = """SELECT v.userid FROM s.votes v
            WHERE v.userid=%s AND v.title=%s AND v.countryName=%s"""
    cur.execute(sql, (userID, title, countryName))
    conn.commit()
    tuple_resultset = cur.fetchall()
    cur.close()
    if len(tuple_resultset) == 0:
        return True
    return False

def upcomingsongs_titleNCountry(conn):
    cur = conn.cursor()
    sql = """SELECT u.title, u.countryName FROM s.upcomingyearsongs u;"""
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    return res

def insert_user(conn, id, username, password_hash):
    cur = conn.cursor()
    sql = """INSERT INTO s.users(password, userName, userID)
	VALUES (%s, %s, %s);"""
    cur.execute(sql, (password_hash, username, id))
    conn.commit()
    cur.close()

def check_userid_and_name_not_taken(conn, id, username):
    cur = conn.cursor()
    sql = """SELECT u.userid FROM s.users u WHERE u.userid=%s OR u.userName=%s;"""
    cur.execute(sql, (id, username))
    tuple_resultset = cur.fetchall()
    cur.close()
    if len(tuple_resultset) == 0:
        return True
    return False

def personal_votes_count(conn, userID):
    cur = conn.cursor()
    sql = """SELECT COUNT(userid) FROM s.votes WHERE userid = %s"""
    cur.execute(sql, (userID,))
    res = cur.fetchone()
    cur.close()
    return res

def update_password(conn, userID, password_hash):
    cur = conn.cursor()
    sql = """UPDATE s.users SET password = %s WHERE userID = %s"""
    cur.execute(sql, (password_hash, userID))
    conn.commit()
    cur.close()