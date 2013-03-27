"""
tipsy.py -- A flask-based todo list
"""

#Added session, url_for, escape for username login and g for global variables
from flask import Flask, render_template, request, redirect, url_for, escape, session, g
# importa model file
import model

#initializes program to be a Flask application
app = Flask(__name__)
# Flask function before_request that will be called before every view is executed.
@app.before_request
def set_up_db():
	# use g to help manage multiple users accessing the database
	g.db = model.connect_db()

#global teardown request that cleans up after each view
#passes e to cover errors and make sure they are ignored and db closed
@app.teardown_request
def disconnect_db(e):
	g.db.close()

#Add ability to login as a particular user
#create login form (in login.html)
#def function called login
@app.route("/authenticate", methods=["POST"])
def authenticate():
	email = request.form['email']
	password = request.form['password']
	user_id = model.authenticate(g.db, email, password)
	session['user_id'] = user_id

@app.route("/")
def index():
	user_id = session.get("user_id", None)
	if user_id:
		db_user = model.get_user(g.db, user_id)
		return render_template("index.html", user_name="George")
	return 'You are not logged in'
	
	# previous attempt at setting up login 
	# if 'username' in session:
	# 	return render_template("index.html", user_name=escape(session['username']))
	# return 'You are not logged in'

# take in user input to add tasks
@app.route("/new_task")
def new_tasks():
	#db = model.connect_db()
	# assign to variable the function from model file with the noted attributes
	#insert_tasks_db = model.new_task(db, title, userid)
	return render_template("new_task.html")

# runs function to save to the db
@app.route("/save_task", methods=["POST"])
def save_task():
	task_title = request.form['add_title']
#	db = model.connect_db() - took out when added global db call
	# Assume that all tasks are attached to user 1.
	# Need to automate
	task_id = model.new_task(g.db, task_title, 1)
	return redirect("/tasks")

# view which is also a function that lists multiple tasks
@app.route("/tasks")
def list_tasks():
#	db = model.connect_db() - took out when added global db call
	#following carries the session id through and requires it to lists the tasks
	user_id = session.get("user_id", None)
	tasks_from_db = model.get_tasks(g.db, user_id)
	return render_template("list_tasks.html", tasks=tasks_from_db)

# view a single task
@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
#	db = model.connect_db() - took out when added global db call
	task_from_db = model.get_task(g.db, id)
	return render_template("view_task.html", task=task_from_db)

#complete task
@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
#	db=model.connect_db()  - took out when added global db call
	model.complete_task(g.db, id)
	return redirect("/tasks")

@app.route("/login")
def login():
	return render_template("login.html")

#Block below shows our initial attempt at login
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#	db = model.connect_db()
	# if request.method == 'POST':
	# 	session['username'] = request.form['username']
	# 	session['password'] = request.form['password']
	# 	if model.authenticate(g.db, session['username'], session['password']):
	# 		return redirect(url_for('index'))
	# return '''
	# 	<form action="" method="post">
	# 		<p><input type=text name=username>
	# 		<p><input type= text name=password>
	# 		<p><input type=submit value=Login>
	# 	</form>
	# '''

# @app.route('/logout')
# def logout():
# 	#remove the username from the session if it's there
# 	session.pop('username', None)
# 	return redirect(url_for('index'))

# #set the secret key. keep this really secret:
# app.secret_key = 'A0Zr98j/3yX R~XHH! jmN]LWX/ , ?RT'



if __name__ == "__main__":
	app.run(debug=True)