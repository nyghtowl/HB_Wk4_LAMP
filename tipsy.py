"""
tipsy.py -- A flask-based todo list
"""

from flask import Flask, render_template, request, redirect
# importa model file
import model

#initializes program to be a Flask application
app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html", user_name="Marissa & Melanie")

# view which is also a function
@app.route("/tasks")
def list_tasks():
	db = model.connect_db()
	tasks_from_db = model.get_tasks(db, None)
	return render_template("list_tasks.html", tasks=tasks_from_db)

# take in user input to add tasks
@app.route("/new_task")
def new_tasks():
	#db = model.connect_db()
	# assign to variable the function from model file with the noted attributes
	#insert_tasks_db = model.new_task(db, title, userid)
	return render_template("new_task.html")

@app.route("/save_task", methods=["POST"])
def save_task():
	task_title = request.form['add_title']
	db = model.connect_db()
	# Assume that all tasks are attached to user 1.
	task_id = model.new_task(db, task_title, 1)
	return redirect("/tasks")


if __name__ == "__main__":
	app.run(debug=True)