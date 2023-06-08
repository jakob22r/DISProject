from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from config import config
from flask_login import UserMixin, LoginManager, current_user, login_user, login_required
from . import models, queries as q

# init SQLAlchemy so we can use it later in our models

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

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    cur.execute("SELECT userID, userName FROM s.users WHERE userID = %s", (user_id,))
    result = cur.fetchone()
    cur.close()

    if result:
        user_id, username = result
        #Return object based on ID with the proper attributes, it does not have to be exact same instance
        return models.User(user_id, username)
    else:
        return None


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



