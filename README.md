# django-rest-framework-todolist-api

This project is a Django-based application that implements a Todo list API using Django REST framework. It includes user authentication and provides endpoints to perform Create, Read, Update, and Delete (CRUD) operations on the Todo list items. Follow the instructions below to set up the project and start
using the API.

## frameworks used

- Django
- Django Rest Framework
- Postman
- Swagger

## Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.x
- Django 4.x (or the compatible version)
- Python virtual environment

## Setup Instructions

1. Clone the Repository:

   ```bash
   git clone https://github.com/Successinnovatia/drf-todolist-app.git
   cd drf-todolist-app
   ```

2. Create and Activate a Virtual Environment:
   python3 -m venv venv
   source venv/bin/activate
   windows: venv\scripts\activate
3. Install Dependencies:
   pip install -r requirements.txt
4. Create a .env File:
   Create a .env file in the project root directory.
   Add your Django SECRET_KEY to the .env file:
   SECRET_KEY=your_secret_key_here
5. Apply Database Migrations:
   python manage.py migrate
6. Run the Development Server:
   python manage.py runserver
7. view the api docs on swagger with `http://127.0.0.1:8000/swagger`

## Running the Tests

To run the tests for the authentication system and todos to evaluate security and functionality, follow these steps:

1. Ensure that the development server is running.

2. Open a new terminal window (if the virtual environment is active) or activate the virtual environment again:
   source venv\scripts\activate
3. Run the tests using Django's test runner:
   python manage.py test authentication.tests
   python manage.py test todos.tests
