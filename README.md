
# Online Course Platform Backend

This project is a Django-based backend for an online course platform. It provides RESTful APIs for managing users, courses, lessons, homework, payments, and more. The backend is designed for scalability, security, and easy integration with frontend clients.

## Features

- **User Management:** Custom user model with roles (admin, teacher, student), registration, authentication (JWT), and profile management.
- **Course & Category Management:** Create, update, and organize courses into categories.
- **Lesson & Module Structure:** Courses are divided into modules and lessons, each with video links and progress tracking.
- **Student Enrollment:** Students can enroll in courses, track their progress, and access lessons.
- **Homework System:** Assignments per lesson, with file uploads and submission tracking.
- **Payment Integration:** Multiple payment types supported (cart, cash, click, payme, coin) for course enrollment.
- **Feedback & Progress:** Students can leave feedback on lessons and track their completion status.
- **Admin Panel:** Full-featured Django admin for managing all resources.
- **API Security:** JWT authentication, CORS support, and secure endpoints.

## Tech Stack

- Python 3.x
- Django 6.x
- Django REST Framework
- SQLite (default, can be swapped for PostgreSQL/MySQL)
- JWT Authentication

## Project Structure

```
category/   # Course categories
course/     # Courses, modules, and enrollment
lesson/     # Modules and lessons
student/    # Student progress and feedback
homework/   # Homework assignments and submissions
payment/    # Payment records
user/       # Custom user model and authentication
config/     # Django project settings
templates/  # HTML templates (if any)
db.sqlite3  # Default database
```

## Installation & Setup

1. **Clone the repository:**
	```bash
	git clone <repo-url>
	cd course
	```
2. **Create and activate a virtual environment:**
	```bash
	python -m venv venv
	source venv/Scripts/activate  # On Windows
	# or
	source venv/bin/activate      # On macOS/Linux
	```
3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```
4. **Configure environment variables:**
	- Copy `.env.example` to `.env` and set your `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS`.
5. **Apply migrations:**
	```bash
	python manage.py migrate
	```
6. **Create a superuser:**
	```bash
	python manage.py createsuperuser
	```
7. **Run the development server:**
	```bash
	python manage.py runserver
	```

## API Overview

- All endpoints are prefixed by `/api/` (see `urls.py` in each app).
- JWT authentication is required for most endpoints.
- Example endpoints:
  - `/api/user/` — User registration, login, profile
  - `/api/course/` — List, create, enroll in courses
  - `/api/lesson/` — Access lessons and modules
  - `/api/homework/` — Submit and review homework
  - `/api/payment/` — Payment processing

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Running Tests

Run all tests with:
```bash
python manage.py test
```

## License

This project is licensed under the MIT License.