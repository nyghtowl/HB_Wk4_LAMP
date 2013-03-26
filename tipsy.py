"""
tipsy.py -- A flask-based todo list
"""

#Added session, url_for, escape for username login
from flask import Flask, render_template, request, redirect, url_for, escape, session
# importa model file
import model

#initializes program to be a Flask application
app = Flask(__name__)
@app.route("/")
def index():
	if 'username' in session:
		return render_template("index.html", user_name=escape(session['username']))
	return 'You are not logged in'

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
	db = model.connect_db()
	# Assume that all tasks are attached to user 1.
	# Need to automate
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")

# view which is also a function that lists multiple tasks
@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks=tasks_from_db)

# view a single task
@app.route("/task/<int:id>", methods=["GET"])
def view_task(id):
	db = model.connect_db()
	task_from_db = model.get_task(db, id)
	return render_template("view_task.html", task=task_from_db)

#complete task
@app.route("/task/<int:id>", methods=["POST"])
def complete_task(id):
	db=model.connect_db()
	model.complete_task(db, id)
	return redirect("/tasks")

#Add ability to login as a particular user
#create login form (in login.html)
#def function called login
@app.route('/login', methods=['GET', 'POST'])
def login():
	db = model.connect_db()
	if request.method == 'POST':
		session['username'] = request.form['username']
		session['password'] = request.form['password']
		if model.authenticate(db, session['username'], session['password']):
			return redirect(url_for('index'))
	return '''
		<form action="" method="post">
			<p><input type=text name=username>
			<p><input type= text name=password>
			<p><input type=submit value=Login>
		</form>
	'''
#accept user login (user's email)
#compare user login to db, make sure user email exists
#check password
#create session


@app.route('/logout')
def logout():
	#remove the username from the session if it's there
	session.pop('username', None)
	return redirect(url_for('index'))

#set the secret key. keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH! jmN]LWX/ , ?RT'



if __name__ == "__main__":
	app.run(debug=True)