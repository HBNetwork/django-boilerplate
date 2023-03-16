# Django-boilerplate with App Core Configured - HBNetwork

Following the instructions bellow to create a fast project Django configured with a app core.

This project help you a create a new project in Django framework using the lib **[copier](https://copier.readthedocs.io/en/stable/)**

### Deploy a fully configured Django Application the fastest way!

This template includes:
* Django version: 4.1.x
* Easy settings setup with [Decouple](https://github.com/hbnetwork/python-decouple)
* Use of URL's to manage database access : [dj-database-url](https://github.com/jazzband/dj-database-url)
* [Black] (https://github.com/psf/black)
* [Pytest](https://docs.pytest.org/)
* [Pytest-django](https://pytest-django.readthedocs.io/en/latest/)
* [Pytest-cov](https://github.com/pytest-dev/pytest-cov)
* Pyproject.toml  
* Pre-commit  


## Usage

Lets create your project, **you will not clone this repo**, just follow the instructions bellow.

**REQUISITES**
```
pip install --upgrade pip  
```
* Install the lib **[copier](https://copier.readthedocs.io/en/stable/)**  in your system  
* Using Python ^3.8
* Git version ^2.28

* Copier
```
pip install copier
```

* Poetry  
```
pip install poetry

```
* Pre-commit
```
pip install pre-commit  

```

## STEPS: 

* Adjust the config virtualenvs to save *.venv* inside in your folder project

```
$ poetry config virtualenvs.in-project true

```

* Using command **copier** to create the folder project and copy any file in origin repository and replace values dynamically using the CLI 
Questionaries

**RUN COMAND ...>**
```
copier https://github.com/HBNetwork/django-boilerplate path/to/project_folder

```

## The CLI Questionary:
* What is your project name?
* What is your first app name? (default is core)
* What is your package name? (same your project name)
* What is your package version? (default 1.0.0)
* What is your package description? (default none)
* What is your name? (author)
* What is your email? (author)
* What is your package module? (same your project name)
* Wait for a few minutes to install all apps and finish the process. You need to create your README.md file

-----------------------------

## Instruction to run the new project

### Linux and Mac
```
cd path/to/project_folder
source .venv/bin/activate
python3 manage.py check
python3 manage.py migrate
python3 manage.py runserver

```

### Windows
```
cd path/to/project_folder
.venv\Scripts\activate
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Commands Tips
- python manage.py check
- python manage.py runserver
- python manage.py migrate
- python manage.py collectstatic