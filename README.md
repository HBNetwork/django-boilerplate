# Django-boilerplate - HBNetwork


### Deploy a fully configured Django Application the fastest way!

This template includes:
* Django version: 4.1.x
* Easy settings setup with [Decouple](https://github.com/hbnetwork/python-decouple)  
* Use of URL's to manage database access : [dj-database-url](https://github.com/jazzband/dj-database-url)  
* [Black] (https://github.com/psf/black) 
* [Pytest](https://docs.pytest.org/)
* [Pytest-django](https://pytest-django.readthedocs.io/en/latest/)
* [Pytest-cov](https://github.com/pytest-dev/pytest-cov)


## Usage

Lets create your project, **you will not clone this repo**, just follow the instructions bellow.

**NOTE**: You may need need to replace **_myproject_** placeholder to your project's name, it can break the installation.


### Linux and Mac
```
mkdir myproject
cd myproject
python3 -m venv .venv 
source .venv/bin/activate
pip install django
```

### Windows
```
mkdir myproject
cd myproject
python -m venv .venv
.venv\Scripts\activate
pip install django
```

Now we can pull Django Boilerplate Structure to Project 

```
django-admin startproject --template https://github.com/HBNetwork/django-boilerplate/archive/main.zip --name=.env-sample,pytest.ini  myproject .
```


And then, proceed with the installation of the requirements. 

### [PROD]
```
pip install -r requirements.txt
```


### [DEV]
```
pip install -r requirements-dev.txt
```


## Configuring Settings 
- rename .env-sample to .env and adjust settings accordingly


## Tips
- python manage.py check  
- python manage.py migrate  
- python manage.py collectstatic  

## Future possibilities
- Default APP
- Poetry
- Containers (Docker)
- Bootstrap (5.2)
- Pre-commit hooks
- Github actions

