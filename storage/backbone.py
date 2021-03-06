import sqlite3
import os
from flask import Flask, g

app = Flask(__name__)

# Load default config and override config from an environment variable
# Setup help https://github.com/mitsuhiko/flask/blob/master/examples/flaskr/flaskr.py
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'engine.db'),
    DEBUG=True,
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

    '''
        create table Bill(
            id integer NOT NULL PRIMARY KEY autoincrement,
            LastName varchar(255) NOT NULL,
            FirstName varchar(255),
            Address varchar(255),
            City varchar(255)
        );

        create table dbNames(
            id integer PRIMARY KEY autoincrement,
            name varchar(255) NOT NULL,
            description varchar(255) NOT NULL,
            datatype varchar(255),
            dateCreated DATE
        );
        Insert into Bill values (1,'Smith', 'Johny', 'Lancaster', 'Reynoldsburg');
    '''
