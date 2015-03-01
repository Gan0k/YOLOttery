import sqlite3
from flask import g, Flask

DATABASE = '/database.db'
app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = connect_to_database()
	return db


def connect_to_database():
	return sqlite3.connect(DATABASE)

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

with app.app_context():
	for user in query_db('select * from prova'):
		print (user[0], 'has the id', user[1])