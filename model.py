"""
model.py 
"""
import sqlite3
import datetime

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, fname, lname):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?, ?)"""
	result = c.execute(query, (email, password, fname, lname))
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
		return dict(zip(fields, result))
	#Else return none
	return None

def new_task(db, title, user_id):
	c = db.cursor()
	#Insert new task into db
	query = """INSERT INTO Tasks VALUES (NULL, ?, NULL, NULL, NULL, ?)"""
	#run query
	result = c.execute(query, (title, user_id))
	#commit query
	db.commit()
	#return task
	return result.lastrowid

def get_user(db, id):
#Fetch a user's record based on his id. Return a user as a dictionary, like authenticate method
	c = db.cursor()
 	query = """SELECT * from Users where id = ?"""
 	c.execute(query, (id,))
 	result = c.fetchone()
 	if result:
 		keys = ["id", "email", "password", "first_name", "last_name"]
 		return dict(zip(keys, result))
 	return None

def complete_task(db, task_id):
# find task id 
	c = db.cursor()
	now = datetime.datetime.now()
	query = """UPDATE Tasks 
	SET completed_at = ?
	WHERE id = ?"""
	c.execute(query, (now, task_id))
	result = c.fetchone()
	db.commit()

def get_tasks(db, user_id=None):
# gets all the tasks for the given user id.	
	c = db.cursor()
	tasks_list = []
	
	#check if user id is NONE
	if user_id == None:
		#query all tasks
		query = """SELECT * from Tasks"""
		c.execute(query,)
	#if there is a user id, run query for that user
	else:
		query = """SELECT * from Tasks where user_id = ?"""
		c.execute(query,(user_id,))
	results = c.fetchall()
	#loop through results and create a dictionary of the results
	for result in results:
		holder_dict = {}
		holder_dict['id'] = result[0]
		holder_dict['title'] = result[1]
		holder_dict['create_at'] =result[2]
		holder_dict['due_date'] =result[3]
		holder_dict['completed_at'] =result[4]
		holder_dict['user_id'] =result[5]
		tasks_list.append(holder_dict)
	
	return tasks_list

def get_task(db, task_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id = ?"""
	c.execute(query, (task_id,))
	result = c.fetchone()
	if result:
		fields = ["id", "title", "created_at", "due_date", "completed_at", "user_id"]
		return dict(zip(fields, result))
	#Else return none
	return None



# def get_taske(db, task_id):

	
	
# CREATE TABLE Users (
# id INTEGER PRIMARY KEY,
# email varchar(64),
# password varchar(64),
# fname varchar(64),
# lname varchar(64)
# );

# CREATE TABLE Tasks (
# id INTEGER PRIMARY KEY,
# title varchar(128),
# created_at DATETIME,
# due_date DATETIME,
# completed_at DATETIME,
# user_id INT
# );
