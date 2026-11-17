# Django Blog Project

A simple Blog Management Web Application built with Django. This project allows users to create blog posts and view all available posts using Django Templates and Function-Based Views (FBV).

## Features

- Create new blog posts.
- Display all blog posts.
- View blog title and description.
- UUID-based primary key.
- Automatic creation timestamp.
- Automatic update timestamp.
- Django Template rendering.
- CSRF protection for form submission.

## Technologies Used

- Python
- Django
- SQLite3
- HTML5
- Django Template Language

## Project Structure

```text
django-templete/
│
├── blog/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── blog.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── src/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd django-templete
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install all required packages from requirements.txt:

```bash
pip install -r requirements.txt
```

## Database Migration

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## Available URLs

| URL | Method | Description |
|---|---|---|
| `/` | GET | Display all blog posts |
| `/create/` | GET, POST | Create a new blog post |
| `/admin/` | GET | Django Admin Panel |

## Blog Model

The Blog model contains the following fields:

| Field | Type | Description |
|---|---|---|
| id | UUIDField | Unique primary key |
| title | CharField | Blog title |
| description | TextField | Blog description |
| created_at | DateTimeField | Creation timestamp |
| updated_at | DateTimeField | Last update timestamp |

## Django Template

This project uses Django Template Language (DTL) to display dynamic blog data.

Some template features used:

- `{{ blog.title }}` – Display blog title.
- `{{ blog.description }}` – Display blog description.
- `{{ blog.id }}` – Display blog ID.
- `{{ blog.created_at }}` – Display creation time.
- `{{ blog.updated_at }}` – Display update time.
- `{% for %}` – Iterate through blog posts.
- `{% empty %}` – Display a message when no posts exist.
- `{% csrf_token %}` – Protect form submissions.

## How to Use

1. Run the Django development server.
2. Visit the homepage to see all blog posts.
3. Navigate to `/create/` to create a new blog post.
4. Enter the blog title and description.
5. Submit the form.
6. Return to the homepage to see the newly created post.

## Future Improvements

- Update existing blog posts.
- Delete blog posts.
- Add blog detail pages.
- Add user authentication.
- Improve frontend design with CSS.
- Add pagination and search functionality.

## Author

Developed as a Django learning project.
