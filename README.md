GitHub User Manager API
A FastAPI-based project to manage GitHub users, allowing you to create, read, update, delete, and list GitHub user data. 
This application integrates with GitHub's API to fetch user details and stores them in a PostgreSQL database.

Features
Create Users: Add a GitHub user to the database by username.
Fetch User: Retrieve stored details of a GitHub user.
List Users: List all users in the database, optionally sorted.
Update User: Modify details of an existing GitHub user.
Delete User: Remove a user from the database.

Tech Stack
Backend: FastAPI, SQLAlchemy
Database: PostgreSQL
Frontend: HTML, CSS, JavaScript (Simple Fetch API Integration)

Setup Instructions
Prerequisites
Python 3.10+
PostgreSQL Database
GitHub Personal Access Token (if needed for GitHub API rate limits)

Installation
Clone the repository:
git clone https://github.com/Autonomize_task.git
cd Autonomize_task

Set up the database:
Create a PostgreSQL database and update the DATABASE_URL in the environment file:
DATABASE_URL=postgresql://<username>:<password>@localhost/<database_name>

Install dependencies:
pip install -r requirements.txt
Run database migrations (during development):
python -m app.main
Running the Application

Backend (FastAPI)
Navigate to the Backend directory:
cd Backend
Start the FastAPI server:
uvicorn app.main:app --reload
Access API docs:
Open http://127.0.0.1:8000/docs

Frontend

cd Frontend

Start a local server:
python -m http.server 8000
Open the app in your browser:
http://127.0.0.1:8000/index.html

API Endpoints

Method	Endpoint	Description
POST	/users/	Add a new GitHub user
GET	/users/{username}	Fetch details of a user
GET	/users/	List all users
PUT	/users/{username}	Update a user's details
DELETE	/users/{username}	Delete a user from the DB
Example Usage
To test the backend, use tools like Postman or cURL.
Example cURL request to fetch a user:
curl -X GET http://127.0.0.1:8000/users/mralexgray
