import re
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
	 
app = Flask(__name__)

items = []

@app.route("/")
def load_items():
	return render_template('layout.html', items=items)

@app.route("/submit", methods=['POST'])
def add_item():
	task = request.form['task']
	email = request.form['email']
	priority = request.form['priority']
	
	if task == '':
		return redirect('/')
	elif priority != "High" and priority != 'Medium' and priority != 'Low':
		return redirect('/')
	elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
		return redirect('/')	
	
	items.append((task, priority, email))
	return redirect('/')

@app.route("/clear", methods=['POST'])
def clear_items():
	del items[:]
	return redirect('/')
	
if __name__ == "__main__":
    app.run(debug=True)