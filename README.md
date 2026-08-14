# LearnDjango

Minimal Django starter project for learning and experimenting.

## Overview

This repository contains a small Django project named `learndjango` with a single app `blog` intended as a learning/example project. It includes the project settings, URLs, and a simple app scaffold so you can practice migrations, views, and templates.

## Features

- Minimal Django project scaffold
- Example `blog` app for adding models, views, and tests

## Prerequisites

- Python 3.8+ installed
- pip available
- (Optional) virtual environment tooling such as `venv` or `virtualenv`

## Quick setup

1. Create and activate a virtual environment:

```
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS / Linux
```

2. Install dependencies:

```
pip install -r requirements.txt
# If you don't have a requirements file yet, install Django:
pip install django
```

3. Apply database migrations and create a superuser:

```
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Common development commands

- Run tests:

```
python manage.py test
```

- Make and apply migrations after changing models:

```
python manage.py makemigrations
python manage.py migrate
```

## Project structure

Top-level layout:

```
learndjango/
    db.sqlite3
    manage.py
    blog/
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
        migrations/
            __init__.py
    learndjango/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

- Main Django settings: [learndjango/learndjango/settings.py](learndjango/learndjango/settings.py)
- Project entrypoint / management: [manage.py](manage.py)
- Example app: [blog/](blog)

## Notes

- If you plan to share or deploy this project, add a `requirements.txt` (e.g. `pip freeze > requirements.txt`) and move sensitive settings (like `SECRET_KEY` and `DATABASES`) to environment variables or a separate configuration.
- SQLite is used by default for simplicity. For production use, switch to PostgreSQL or another production-ready database.

- Maintenance: This README will be kept up to date as the project evolves — updates will capture new features, configuration changes, and setup instructions so the documentation stays accurate.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Open a pull request with a clear description

## License

This project is provided as-is for learning purposes. Add a proper license file if you intend to publish or distribute it.

## Next steps

- Add example templates and static files
- Add sample models and admin registrations in `blog/models.py` and `blog/admin.py`
- Add `requirements.txt` to pin dependencies
