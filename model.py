"""
model.py 
"""
import sqlite3

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, fname, lname):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):

	#open a connection to the database and assign to variable c
	c = db.cursor()
	#sets the query to run by pulling all information based on email and password
	query = """SELECT * from Users where email = ? and password = ?"""
	#executes the query on the database with the passed parameters
	c.execute(query, (email, password))
	# should only assign one result from the database query to result var
	result = c.fetchone()
	# If result exists, create a dictionary
	if result:
		fields = ["id", "email", "password", "first_name", "last_name"]
		return dict(zip(result,fields))
	#Else return none
	return None

def new_task(db, title, user_id):
	c = db.cursor()
	#Insert new task into db
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?)"""
	#run query
	result = c.execute(query, (title, user_id))
	#commit query
	db.commit()
	#return task
	return result.lastrowid

# def get_user(db, user_id):
# 	#Fetch a user's record based on his id. Return a user as a dictionary, like authenticate method
# 	c = db.cursor()
# 	query = """SELECT """

# def complete_task(db, task_id):
# def get_tasks(db, user_id):
# def get_taske(db, task_id):

	
	
