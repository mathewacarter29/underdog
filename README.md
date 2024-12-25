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
If you wish to reset the database, you can erase it with the `wipe.py` script
```
> make db-wipe
```

## Setting up virtualenv
1. Install up virtual environment
```
> python -m venv env
> pip install -r requirements.txt
```
2. Start virtual environment
```
> source env/bin/activate
```

Stop virtual environment when you are done running the program
```
> deactivate
```

## Setting up API
```
> make api-start
```

Send a GET request to get all database data in formatted output
```
GET http://localhost:8000/games
```

# Commands to note for development
Write requirements.txt
```
pip freeze > requirements.txt
```

In order to run scripts in the virtual environment, must set python interpreter to
\<current directory\>/env/bin/python
