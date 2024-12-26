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

Sample response
```
{
  "games": [
    {
      "homeTeamName": "UConn",
      "awayTeamName": "Stetson",
      "year": 2024,
      "sportsbook": "Fanduel",
      "homeTeamMoneyline": -20000,
      "awayTeamMoneyline": 3500,
      "homeTeamScore": 91,
      "awayTeamScore": 52,
      "round": 1,
      "region": "East"
    },
    ...
```

# Commands to note for development
Write requirements.txt
```
pip freeze > requirements.txt
```

In order to run scripts in the virtual environment, must set python interpreter to
\<current directory\>/env/bin/python

# Sources for Fanduel Data
2024
1st round
https://www.fanduel.com/research/2024-ncaa-tournament-first-round-betting-odds-predictions-spreads-moneylines-totals
https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-under-for-wagner-vs-north-carolina
https://www.fanduel.com/research/ncaa-tournament-betting-can-florida-cover-the-spread-against-colorado
https://www.fanduel.com/research/ncaa-tournament-betting-picks-can-colorado-state-upset-texas
https://www.fanduel.com/research/ncaa-tournament-betting-picks-can-colorado-state-upset-texas

2nd round
https://www.fanduel.com/research/ncaa-tournament-betting-will-dayton-fly-to-an-upset-win-against-arizona
https://www.fanduel.com/research/ncaa-tournament-betting-can-baylor-cover-the-spread-against-clemson
https://www.fanduel.com/research/ncaa-tournament-betting-grand-canyon-vs-alabama-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-michigan-state-vs-north-carolina-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-colorado-vs-marquette-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-oakland-vs-nc-state-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-james-madison-vs-duke-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-texas-a-and-m-vs-houston-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-can-texas-cover-the-spread-against-tennessee
https://www.fanduel.com/research/ncaa-tournament-betting-can-oregon-keep-things-close-against-creighton
https://www.fanduel.com/research/ncaa-tournament-betting-odds-favor-gonzaga-over-kansas
https://www.fanduel.com/research/ncaa-tournament-betting-utah-state-vs-purdue-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-washington-state-vs-iowa-state-picks-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-duquesne-vs-illinois-picks-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-picks-yale-vs-san-diego-state-prediction-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-northwestern-vs-uconn-picks-prop-bets-and-odds

3rd round
https://www.fanduel.com/research/ncaa-tournament-betting-san-diego-state-vs-connecticut-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-illinois-vs-iowa-state-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-over-for-gonzaga-vs-purdue
https://www.fanduel.com/research/ncaa-tournament-betting-creighton-vs-tennessee-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-duke-vs-houston-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-nc-state-vs-marquette-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-alabama-vs-north-carolina-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-clemson-vs-arizona-picks-prop-bets-and-odds

4th round
https://www.fanduel.com/research/ncaa-tournament-betting-can-clemson-upset-alabama-in-the-elite-eight
https://www.fanduel.com/research/ncaa-tournament-betting-will-nc-state-upset-duke-in-an-acc-clash
https://www.fanduel.com/research/ncaa-tournament-betting-tennessee-vs-purdue-picks-prop-bets-and-odds
https://www.fanduel.com/research/ncaa-tournament-betting-illinois-vs-uconn-picks-prop-bets-and-odds

5th round
https://www.fanduel.com/research/ncaa-tournament-betting-can-alabama-upset-uconn
https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-over-for-purdue-vs-nc-state

6th round (finals)
https://www.fanduel.com/research/national-championship-betting-picks-will-uconn-cover-against-purdue
