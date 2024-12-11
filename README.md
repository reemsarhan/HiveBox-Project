# TaskManagerWithCI

### Flask Task Manager

A simple task management web application built using Python's Flask framework. The application includes user authentication, task management functionality, and version tracking.

##Features

User authentication system (login and logout).

Add, edit, and delete tasks.

View tasks with their current status.

Persistent storage using JSON files (tasks.json and users.json).

Application versioning displayed dynamically from version.txt.

Dockerized application for easy deployment.

GitHub Actions workflow for CI/CD.

## Prerequisites

Ensure you have the following installed:
```
Python 3.8+

Docker

Git
```

Getting Started

Install Dependencies

Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
## Run the Application Locally

Start the Flask development server:
```
python app.py
```

Access the application at http://localhost:5000.

Run with Docker

Build the Docker image:
```
docker build -t flask-task-manager .
```
Run the Docker container:
```
docker run -d -p 5000:5000 --name flask-container flask-task-manager
```
Access the application at http://localhost:5000.

File Structure

.
├── app.py              # Main Flask application
├── tasks.json          # JSON file storing tasks
├── users.json          # JSON file storing user credentials
├── version.txt         # File storing the application version
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS, etc.)
└── .github/workflows/  # GitHub Actions workflows

Usage

User Authentication

Navigate to /login to log in with credentials stored in users.json.

Log out by clicking the logout button.

Manage Tasks

Add a task by filling out the form on the home page.

Edit a task's status by marking it as completed or pending.

Delete a task by clicking the delete button.

Version Tracking

The application version is displayed dynamically from version.txt.

Access the version at http://localhost:5000/version.

### Continuous Integration
---
The project includes a GitHub Actions workflow:

Builds the Docker image.

Runs the container.

Validates the application version against version.txt.

Runs tests to ensure functionality.
---
 
