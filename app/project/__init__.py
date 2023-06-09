import psycopg2
from flask import Flask
from flask_bcrypt import Bcrypt
from config import config
from flask_login import LoginManager
from . import models

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


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
conn = connect()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

#To check user authentication
@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    cur.execute("SELECT userID, userName FROM s.users WHERE userID=%s;", (user_id,))
    result = cur.fetchone()
    cur.close()

    if result:
        user_id, username = result
        #Return object based on ID with the proper attributes, 
        return models.User(user_id, username)
    else:
        return None


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



