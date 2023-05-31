# TravelMemo
A web application that people can use to store their impressions of the places they've visited.

## Quick start

Install poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Clone the project
```bash
git clone https://github.com/n1ce7ry/place-remember
```

Go to the project folder and install the dependencies
```bash
cd place-remember
poetry shell
poetry install
```

Or by using the pip
```bash
cd place-remember
python3 -m venv venv
pip install django==4.2.1; pip install django-allauth==0.54.0
```

Run server with secret key
```bash
cd app
SECRET_KEY="<SECRET_KEY>" python3 manage.py runserver
```

## Not implemented
* Unit tests 
