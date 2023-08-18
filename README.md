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

Edit env.example, rename it to env.sh, and run it:
```bash
vim env.example
mv env.example env.sh
. ./env.sh
```

Apply migrations
```bash
cd app
python3 manage.py migrate
```

Run server 
```bash
python3 manage.py runserver
```

## TO DO:
* Unit tests 
* There is an error when you access the site through the admin  
