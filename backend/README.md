# Backend

backend of Point of Sales system.

## Prerequisites

Navigate to this folder and create a virutal environment (using conda or venv) possible way of doing that:

```bash
pyhon -m venv .venv
```

activate the newly created environement: 

```bash
./venv/Scripts/activate
```

install the project dependecies:

```bash
pip install -r requirements.txt
```

create the `.env` file in the `django-server` folder with following parameters (continually updating list):

```
DEBUG=True
```

This file holds configurations that change depending on the environement the server is running.

## Running the server

```bash
python manage.py runserver
```
