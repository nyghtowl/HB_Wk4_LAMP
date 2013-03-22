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
	query = """SELECT title, due_date, completed_at from Tasks where user_id = ?"""
	c.execute(query, (user_id,))
	results = c.fetchall()
	if results:
		for result in results:
			holder_dict = {}
			holder_dict['tite'] = result[0]
			holder_dict['due_date'] = result[1]
			holder_dict['completed'] =result[2]
			tasks_list.append(holder_dict)
		return tasks_list
	else:
		query2 = """SELECT title, due_date, completed_at from Tasks"""
		c.execute(query2,)
		results2 = c.fetchall()
		for result in results2:
			holder_dict = {}
			holder_dict['tite'] = result[0]
			holder_dict['due_date'] = result[1]
			holder_dict['completed'] =result[2]
			tasks_list.append(holder_dict)
		return tasks_list



# def get_taske(db, task_id):

	
	
