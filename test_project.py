import os
import json
import pytest
from project import add_task, complete_task, update_pomodoro_count

# Use a test file instead of the main one
TEST_TASKS_FILE = 'test_tasks.json'

# Override the tasks file for testing
import project
project.TASKS_FILE = TEST_TASKS_FILE

def setup_function():
    """Setup function that runs before each test"""
    # Create an empty test tasks file
    with open(TEST_TASKS_FILE, 'w') as f:
        json.dump([], f)

def teardown_function():
    """Teardown function that runs after each test"""
    # Remove the test tasks file
    if os.path.exists(TEST_TASKS_FILE):
        os.remove(TEST_TASKS_FILE)

def test_add_task():
    """Test adding a task"""
    # Add a task
    tasks = add_task("Test Task", "Test Description", "high")
    
    # Check if the task was added correctly
    assert len(tasks) == 1
    assert tasks[0]['title'] == "Test Task"
    assert tasks[0]['description'] == "Test Description"
    assert tasks[0]['priority'] == "high"
    assert tasks[0]['completed'] == False
    assert tasks[0]['pomodoros_completed'] == 0
    
    # Add another task and check if the ID is incremented
    tasks = add_task("Another Task")
    assert len(tasks) == 2
    assert tasks[1]['id'] == 2
    assert tasks[1]['title'] == "Another Task"
    assert tasks[1]['priority'] == "medium"  # Default value

def test_complete_task():
    """Test completing a task"""
    # Add a task
    add_task("Test Task")
    
    # Complete the task
    tasks = complete_task(1)
    
    # Check if the task was marked as completed
    assert tasks[0]['completed'] == True

def test_update_pomodoro_count():
    """Test updating the pomodoro count of a task"""
    # Add a task
    add_task("Test Task")
    
    # Update the pomodoro count
    tasks = update_pomodoro_count(1)
    
    # Check if the pomodoro count was incremented
    assert tasks[0]['pomodoros_completed'] == 1
    
    # Update again
    tasks = update_pomodoro_count(1)
    
    # Check if the pomodoro count was incremented again
    assert tasks[0]['pomodoros_completed'] == 2