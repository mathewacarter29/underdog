# Getting started

## Initialize database
1. Follow README instructions in data/README.md to set up local postgres instance
2. Ensure database is running with make command
```
> make db-start
```
3. Populate database with `populate.py` script
```
> make db-populate
```

## Setting up virtualenv
Install up virtual environment
> python -m venv env
> pip install -r requirements.txt

Start virtual environment
> source env/bin/activate

End virtual environment
> deactivate

Write requirements.txt
> pip freeze > requirements.txt

In order to run scripts in the virtual environment, must set python interpreter to
<current directory>/env/bin/python

## Setting up API
> make api-start