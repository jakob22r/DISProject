from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from config import config
import os


app = Flask(__name__)

# #Using a decorator to bind root URL to a function, i.e. navigating to root page, will execute the 
# #following function, which will load the hello.html page
# @app.route("/")
# def hello_world(name=None):

#     #Perform some SQL

#     return render_template('index.html', name='Emlily')


#Connect to database students

#Creates a new connection and returns instance of connection class
#connection = psycopg2.connect(host="localhost", port="5432", database="students", user="postgres", password="magnarp2")


#Function to connect to postgresql server
def connect():
    connection = None
    params = config()
    print("Connecting to PostgreSQL DB ...")
    #Params loaded via database.ini
    connection = psycopg2.connect(**params)

    #Create cursor
    crsr = connection.cursor()
    print("Postgres version ")
    crsr.execute('SELECT version()')
    db_verion = crsr.fetchone()
    print(db_verion)
    return connection


@app.route('/')
def index():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)

#Define html methods
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = connect()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


#Checks if scripts is executed directly from command line
if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')


