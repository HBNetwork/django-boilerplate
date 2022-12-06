# Django-boilerplate - HBNetwork


### Deploy a fully configured Django Application the fastest way!

This template includes:
* Easy settings setup with [Decouple](https://github.com/hbnetwork/python-decouple)
* Use of URL's to manage database access

## Usage

Lets create your project, **you will not clone this repo**, just follow the instructions bellow.

**NOTE**: You may need need to replace _myproject_ placeholder to your project's name, it can break the installation.
```
mkdir myproject
cd myproject
python3 -m venv .venv or python -m venv .venv
source .venv/bin/activate or .venv/Scripts/activate
pip install django
```

Now we can pull Django Boilerplate Structure to Project 

```
django-admin startproject --template https://github.com/HBNetwork/django-boilerplate/archive/main.zip --name=.env-sample myproject .
```


And then, proceed with the installation of the requirements. 

```

pip install -r requirements.txt
```


## Configuring Settings 
- rename .env-sample to .env and adjust settings accordingly

## Tips
python .\manage.py check
python .\manage.py migrate
python .\manage.py collectstatic



MENU 
https://github.com/HBNetwork/django-boilerplate/archive/main.zip
Base (main.zip)
com-app (com-app.zip)
