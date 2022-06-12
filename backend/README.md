# Backend

backend of Point of Sales system.

## Prerequisites

Navigate to this folder and create a virutal environment (using conda or venv). One possible way of doing that:

```bash
pyhon -m venv .venv
```

Now activate the newly created environement:

On Windows
```bash
./venv/Scripts/activate
```

On Mac
```bash
. venv/bin/activate
```

Once the environement is running, install the project dependecies:

```bash
pip install -r requirements.txt
```

finally, create the `.env` file in the `django-server` folder with following parameters (continually updating list):

```
DEBUG=True
```

This file holds configurations that change depending on the environement the server is running in (db connection strings, secrets...).

## Running the server

```bash
python manage.py runserver
```
