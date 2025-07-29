# Student Directory System

A modern web application for managing student records in educational institutions, built with Django and Python.


## 🏗️ Technology Stack

- **Backend**: Django 5.2.4 (Python)
- **Frontend**: HTML5, CSS3, Django Templates
- **Database**: SQLite (development) / PostgreSQL (production)
- **API**: Django REST Framework
- **Deployment**: Gunicorn + Cloud Platforms

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aayaz0/Student-Directory-with-Search-and-Filter-Django-.git
   cd Student-Directory-with-Search-and-Filter-Django-
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API endpoint: http://127.0.0.1:8000/api/students/

## 📊 Sample Data

The application comes with 50 sample student records across various departments including:

- Computer Science
- Information Technology
- Software Engineering
- Electronics
- Mechanical Engineering
- And more...

## 🔍 Usage

### Search Functionality

- Search by **student name**: "Aayush", "Sharma"
- Search by **student ID**: "001", "025"
- Search by **department**: "Computer", "Information"



### API Access

```bash
# Get all students (JSON)
curl http://127.0.0.1:8000/api/students/
```

## 🏛️ Project Structure

```
student_directory/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Procfile                     # Deployment configuration
├── runtime.txt                  # Python version specification
├── student_directory/           # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
└── students/                    # Student management app
    ├── models.py               # Data models
    ├── views.py                # Business logic
    ├── urls.py                 # App-specific URLs
    ├── admin.py                # Admin interface
    ├── serializers.py          # API serialization
    └── templates/students/     # HTML templates
        ├── base.html           # Base template
        ├── index.html          # Home page
        └── search_results.html # Search results
```

## 🔐 Security Features

- **Authentication Required**: All views protected with login decorators
- **CSRF Protection**: Built-in Django middleware prevents cross-site attacks
- **SQL Injection Prevention**: Django ORM automatically sanitizes queries
- **Password Hashing**: Passwords encrypted using Django's built-in system

## 🚀 Deployment

### Deployment-Ready Features

- ✅ Procfile for Gunicorn server
- ✅ requirements.txt with all dependencies
- ✅ runtime.txt specifying Python version
- ✅ Environment variables support

### Supported Platforms

- Heroku
- Render
- Railway
- DigitalOcean App Platform
- AWS Elastic Beanstalk

### Environment Variables (Production)

```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=your-domain.com


⭐ **If you find this project helpful, please give it a star!** ⭐
