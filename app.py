from flask import Flask, render_template, request, redirect, url_for, session
import json
import click  # Flask uses Click for command-line utilities

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define the app version
APP_VERSION = "1.0.0"

# Helper functions for reading and writing JSON files
def read_tasks():
    with open('tasks.json', 'r') as file:
        return json.load(file)

def write_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def read_users():
    with open('users.json', 'r') as file:
        return json.load(file)

# CLI command to print the app version
@app.cli.command("version")
def print_version():
    """Print the current application version and exit."""
    click.echo(f"Current Task Manager version: {APP_VERSION}")

# Home route
@app.route('/')
def index():
    if 'username' in session:
        tasks = read_tasks()['tasks']
        return render_template('index.html', tasks=tasks)
    return redirect(url_for('login'))

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()['users']
        
        # Check if user exists and passwords match
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('index'))
        
        return 'Invalid credentials'
    
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Add task route
@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    title = request.form['title']
    description = request.form['description']
    
    tasks = read_tasks()
    task_id = len(tasks['tasks']) + 1
    tasks['tasks'].append({
        "id": task_id,
        "title": title,
        "description": description,
        "status": "pending"
    })
    
    write_tasks(tasks)
    return redirect(url_for('index'))

# Edit task route (mark as completed/pending)
@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    tasks = read_tasks()
    for task in tasks['tasks']:
        if task['id'] == task_id:
            task['status'] = request.form['status']
    
    write_tasks(tasks)
    return redirect(url_for('index'))

# Delete task route
@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    tasks = read_tasks()
    tasks['tasks'] = [task for task in tasks['tasks'] if task['id'] != task_id]
    
    write_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)