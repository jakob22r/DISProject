from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from queries import *
from forms import *
import psycopg2
from config import config
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff05' #Not the safest solution

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

conn = connect()


@app.route('/')
def index():
    #conn = connect()
    # cur = conn.cursor()
    # cur.execute('SELECT * FROM books;')
    # tuples_lst = cur.fetchall()
    # cur.close()
    # conn.close()
    return render_template('index.html')


@app.route('/stats', methods=('GET', 'POST'))
def stats():
    winners = select_winner_songs_last10years(conn)
    null_p = select_null_points(conn)


    form = SearchYearForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            year = form.year.data
            #Process data as needed
            winner_year_x = select_winner_by_year(conn,year)
            return render_template('stats.html', winner_tups=winners, null_tups=null_p, form=form, qrs=winner_year_x)

    return render_template('stats.html', winner_tups=winners, null_tups=null_p, form=form)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/vote', methods=('GET', 'POST'))
def vote():
    if request.method=='POST':
        #do nothing right now
        return "something"
    
    return render_template('vote.html')


#Below code is less relevant

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


