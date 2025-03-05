from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime
import json
import os

app = Flask(__name__)

# Path to store the tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from the JSON file
    
    Returns:
        list: List of task dictionaries
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file
    
    Args:
        tasks (list): List of task dictionaries to save
    """
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

def add_task(title, description='', priority='medium'):
    """
    Add a new task to the tasks list
    
    Args:
        title (str): Title of the task
        description (str, optional): Description of the task. Defaults to ''.
        priority (str, optional): Priority of the task. Defaults to 'medium'.
    
    Returns:
        list: Updated list of tasks
    """
    tasks = load_tasks()
    
    # Create new task
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'priority': priority,
        'completed': False,
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'pomodoros_completed': 0
    }
    
    tasks.append(task)
    save_tasks(tasks)
    return tasks

def complete_task(task_id):
    """
    Mark a task as completed
    
    Args:
        task_id (int): ID of the task to mark as completed
    
    Returns:
        list: Updated list of tasks
    """
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
            
    save_tasks(tasks)
    return tasks

def update_pomodoro_count(task_id):
    """
    Increment the pomodoro count for a task
    
    Args:
        task_id (int): ID of the task to update
    
    Returns:
        list: Updated list of tasks
    """
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['pomodoros_completed'] = task.get('pomodoros_completed', 0) + 1
            break
            
    save_tasks(tasks)
    return tasks


@app.route('/')
def index():
    """Main route that displays the Pomodoro To-Do List"""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def handle_add_task():
    """Route to handle adding a new task"""
    title = request.form.get('title')
    description = request.form.get('description', '')
    priority = request.form.get('priority', 'medium')
    
    if title:
        add_task(title, description, priority)
    
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def handle_complete_task(task_id):
    """Route to handle marking a task as completed"""
    complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update_pomodoro/<int:task_id>', methods=['POST'])
def handle_update_pomodoro(task_id):
    """Route to handle updating a task's pomodoro count"""
    tasks = update_pomodoro_count(task_id)
    return jsonify({'success': True})

def main():
    """Main function to run the Flask application"""
    app.run(debug=True)

if __name__ == '__main__':
    main()