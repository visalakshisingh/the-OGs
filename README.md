# the-OGs
### Pomodoro To-Do List Application  

#### Video Demo: [https://youtu.be/xvFMNkp44yM]  

#### Description:  
This project focuses has resulted in building a productivity web application, which integrates task management and the Pomodoro Technique, and is hosted on Python Flask Framework. Users can create and manage tasks, which can help them focus through the Pomodoro system of time management. Scheduler works by allowing 25 minutes of focused work, followed by a 5-minute respite.  

 ## Project Overview  
 
The Pomodoro To-Do List application assists users in organizing their tasks by providing with various priority levels by helping to track progress through the Pomodoro Technique. The application adopts a clean, user-friendly design that features an interactive timer display of tasks. Users can gain insights about their productivity as umbers of completed Pomodoro sessions are tracked per individual tasks.

## Files and Functionality

### `project.py`

This is the primary file for the Flask app which 

- Sets up the Flask application and takes care of the routing.

- Specifies the essential functions for task management:  
  
  - `load_tasks()`: Loads tasks from a storage JSON file.  
 
  - `save_tasks()`: Saves tasks in the JSON storage file. 
  
  - `add_task()`: Initiates a new task by creating it with a title, description, and a priority. 
  
  - `complete_task()`: Updates a task to indicate it has been completed. 
  
  - `update_pomodoro_count()`: Increases the Pomodoro count for a task.
  
- Implements actions such as: routes for displaying tasks and the timer, adding a task, completing a task, and updating the Pomodoro count.  
  
For the sake of convenience, the application utilizes JSON file storage, which means it can retain its task data even without needing to set up a database.

### `test_project.py`

Has thorough examination of the main functions of the application:  

- Verification of all parameters interacting with `add_task()` to check its proper creation.
  
- Checking if `complete_task()` marks them as completed as intended.
  
- Testing `update_pomodoro_count()` for Pomodoro counter incrementation.  
  
The test, in this case, will be placed in a separate test JSON file to prevent interaction with the application's working data and will make use of proper setup and teardown procedures.

### Templates  

#### `index.html`
 
This is the overall interface that integrates the task manager and Pomodoro timer. Most notable features include:  
 
- A task creation form with title and description fields along with priority level selection.

- Display of task list with priorities color coded. High (Red), Medium (Orange) and Low (Blue).

- Pending tasks and completed tasks sections.

- Interactive Pomodoro timer with work and break modes.

- Visual feedback on current timer mode.

- Audio notifications when the timers are done.  

 
This HTML file contains self-contained CSS which styles and JavaScript which functions as a timer, augmenting the ease of use.

- `requirements.txt`
  
This document outlines the dependencies needed to maintain the application.

- Flask 2.0.1 for Web Framework

- pytest 7.0.0 for Testing Framework

### Design Decisions

#### JSON File Storage

I opted for file storage in JSON format instead of utilizing a database on the following grounds:

1. While user-friendly, the project required simplicity and ease of implementation.

2. The only prerequisites to undertake this project are Python’s built-in libraries.

3. The application’s scope and data needs were achievable.

4. Easy to backup and restore.

### Single HTML Template

One application is designed with one HTML page that links to its CSS and JavaScript. This is meant to:

- Keep the project structure organized.

- Make the code more comprehendible for learners.

- Offer a holistic perspective of the frontend construction.

- Remove the necessity of static files.

### Client-Side Timer Implementation

The Javascript Pomodoro timer has been designed in such a way to:

- Make the interface responsive without a need to ping the server.

- Continue working even if the server goes down temporarily.

- Lower the timing logic workload on the server.

- Smoothly switch visually from work to break modes.

### Two-Column Layout

The interface is shown in two columns as follows:

- A list of tasks organized and orderly available on the left side.

- Timer feature on the right hand side for uninterrupted access  

This layout helps users multitask and utilize the timer simultaneously.  

## Primary Execution Aspects  

### Task Data Structure  

Each task is saved as a JSON object with these fields:

```json

{

  "id": 1,

  "title": "Task Title",

  "description": "Task Description",

  "priority": "medium",

  "completed": false,

  "created_at": "2025-04-11 10:30:45",

  "pomodoros_completed": 0

}

```

### Pomodoro Timer Logic  

The timer implementation follows the rules of the Pomodoro Technique:  

1. 25-minute work sessions (dedicated to a task)
  
2. 5-minute pause sessions
  
3. Automatic switching between work and break modes
  
4. Current mode indicators (RED for  work, GREEN for break)
  
5. Timed announcements for specified durations  


### Task Priority System  

Tasks can be placed in three levels of priority:  

- High (red): tasks that are urgent and necessary to be attended to immediately.   

- Medium (orange): tasks that are important but not of utmost urgency.  

- Low (blue): tasks that are not urgent in nature.  

This assists in visual identification of urgent tasks with set colors.

## Problems and their Respective Solutions

### Task Data Persistence  

**Problem**: A database was not available for use, so attempts to store task data between sessions would be difficult.  

**Solution**: JSON files were created along with safeguards against failed file operations.

### Timer Implementation  

**Problem**: Need to have a reliable timer that was capable of tracking work/break cycles.  

**Solution**: JavaScript's setInterval was used for countdown purposes with state variables to track the current mode.

### Test Environment Isolation

**Problem**: Functions could be tested, but there was no way to do so without affecting application data.  

**Solution**: Tests were incorporated into a designated test file path and setup/teardown functions were used to ensure clean test environments.

## Enhancements on the Horizon  

Some improvements can be added for subsequent versions. They are as follows:  

- Adding a mobile version of the application for increased productivity on the go.
  
- User verification processes for assisting multiple users. 
 
- More advanced timers for varying Pomodoro preferences. 

- Enhanced data storage with the aid of a more robust database. 

- Customizable tags and categories for increased organizational productivity. 

- Productivity metrics through advanced visualization. 

- Support for dark mode and additional UI themes. 
 

## Application Instructions  

1. **Ensure Python version 3.6 and Flask are downloaded.**  

2. **Acquire the following dependencies:** `pip install -r requirements.txt`.  
 
3. **Start the application:** `python project.py`.  
 
4. **Open a browser and type:** `http://127.0.0.1:5000` to access the application. 
 

## Application Examination  
 
To utilize the application’s tests, employ pytest and execute:  
 
``` 
python project.py
``` 
 

## Application Overview  

The Flask web framework is combined with frontend technologies in this Pomodoro To-Do List application to showcase ingenuity. The project aims to provide productivity with the basic web development principles such as route management, data storage, server-client interaction, and GUI design. The modular design of the application along with its extensive testing guarantees dependability while enabling refinements and enhancements.
