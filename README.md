# Underdog
This project attempts to simulate what a project in a professional environment would look like. Using a locally hosted Postgres v17.2 Database, a Python FastAPI, and a main project set up using a hexagonal architecture pattern, Underdog determines whether it is profitable to bet on the underdog of every March Madness game of a certain year.

## Getting started

### Setting up virtualenv
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

### Initialize database
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

### Setting up API
```
> make api-start
```

Send a GET request to get all database data in formatted output
```
GET http://localhost:8000/games?year=2024
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

## Commands to note for development
Write requirements.txt
```
pip freeze > requirements.txt
```

In order to run scripts in the virtual environment, must set python interpreter to
\<current directory\>/env/bin/python

## Source for data before 2023
https://www.oddsportal.com/

## Sources for Fanduel Data
### 2024
#### 1st round
- https://www.fanduel.com/research/2024-ncaa-tournament-first-round-betting-odds-predictions-spreads-moneylines-totals
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-under-for-wagner-vs-north-carolina
- https://www.fanduel.com/research/ncaa-tournament-betting-can-florida-cover-the-spread-against-colorado
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-can-colorado-state-upset-texas
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-can-colorado-state-upset-texas

2nd round
- https://www.fanduel.com/research/ncaa-tournament-betting-will-dayton-fly-to-an-upset-win-against-arizona
- https://www.fanduel.com/research/ncaa-tournament-betting-can-baylor-cover-the-spread-against-clemson
- https://www.fanduel.com/research/ncaa-tournament-betting-grand-canyon-vs-alabama-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-michigan-state-vs-north-carolina-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-colorado-vs-marquette-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-oakland-vs-nc-state-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-james-madison-vs-duke-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-texas-a-and-m-vs-houston-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-can-texas-cover-the-spread-against-tennessee
- https://www.fanduel.com/research/ncaa-tournament-betting-can-oregon-keep-things-close-against-creighton
- https://www.fanduel.com/research/ncaa-tournament-betting-odds-favor-gonzaga-over-kansas
- https://www.fanduel.com/research/ncaa-tournament-betting-utah-state-vs-purdue-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-washington-state-vs-iowa-state-picks-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-duquesne-vs-illinois-picks-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-yale-vs-san-diego-state-prediction-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-northwestern-vs-uconn-picks-prop-bets-and-odds

3rd round
- https://www.fanduel.com/research/ncaa-tournament-betting-san-diego-state-vs-connecticut-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-illinois-vs-iowa-state-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-over-for-gonzaga-vs-purdue
- https://www.fanduel.com/research/ncaa-tournament-betting-creighton-vs-tennessee-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-duke-vs-houston-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-nc-state-vs-marquette-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-alabama-vs-north-carolina-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-clemson-vs-arizona-picks-prop-bets-and-odds

4th round
- https://www.fanduel.com/research/ncaa-tournament-betting-can-clemson-upset-alabama-in-the-elite-eight
- https://www.fanduel.com/research/ncaa-tournament-betting-will-nc-state-upset-duke-in-an-acc-clash
- https://www.fanduel.com/research/ncaa-tournament-betting-tennessee-vs-purdue-picks-prop-bets-and-odds
- https://www.fanduel.com/research/ncaa-tournament-betting-illinois-vs-uconn-picks-prop-bets-and-odds

5th round
- https://www.fanduel.com/research/ncaa-tournament-betting-can-alabama-upset-uconn
- https://www.fanduel.com/research/ncaa-tournament-betting-picks-target-the-over-for-purdue-vs-nc-state

6th round (finals)
- https://www.fanduel.com/research/national-championship-betting-picks-will-uconn-cover-against-purdue

### 2023
#### 1st round
- https://www.fanduel.com/research/theduel/unc-asheville-vs-ucla-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gve49tzbvm/
- https://www.fanduel.com/research/theduel/boise-state-northwestern-prediction-odds-best-bet-march-16-ncaa-tournament-game-don-t-expect-fireworks-01gvcde05g03/
- https://www.fanduel.com/research/theduel/gonzaga-grand-canyon-prediction-odds-best-bet-march-17-ncaa-tournament-game-bulldogs-fail-to-pull-away-01gvcddrc5c1/
- https://www.fanduel.com/research/theduel/tcu-vs-arizona-state-prediction-odds-best-bet-for-march-17-ncaa-tournament-01gvms6y9n5n/
- https://www.fanduel.com/research/theduel/uconn-iona-prediction-odds-best-bet-march-17-ncaa-tournament-game-defense-decides-who-advances-01gvcde64hnw/
- https://www.fanduel.com/research/theduel/saint-mary-s-ca-vcu-prediction-odds-best-bet-march-17-ncaa-tournament-game-expect-a-defensive-battle-01gvcddt0tpq/
- https://www.fanduel.com/research/theduel/arkansas-illinois-prediction-odds-best-bet-march-16-ncaa-tournament-game-fighting-illini-cannot-keep-up-01gvcddtqr18/
- https://www.fanduel.com/research/theduel/kansas-vs-howard-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcdedyac2/
- https://www.fanduel.com/research/theduel/marquette-vermont-prediction-odds-best-bet-march-17-ncaa-tournament-game-back-a-high-scoring-first-half-01gvcde2k9s3/
- https://www.fanduel.com/research/theduel/michigan-state-vs-usc-prediction-odds-best-bet-march-17-ncaa-tournament-game-01gvcde1wwj5/
- https://www.fanduel.com/research/theduel/kansas-state-montana-state-prediction-odds-best-bet-march-17-ncaa-tournament-game-expect-fireworks-01gveb7k4yma/
- https://www.fanduel.com/research/theduel/kentucky-providence-prediction-odds-best-bet-march-17-ncaa-tournament-game-friars-can-t-guard-wildcats-01gvcde4r6q9/
- https://www.fanduel.com/research/theduel/tennessee-louisiana-prediction-odds-best-bet-march-16-ncaa-tournament-game-offenses-quiet-in-orlando-01gvdxfqs4yg/
- https://www.fanduel.com/research/theduel/duke-vs-oral-roberts-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcddvd2ww/
- https://www.fanduel.com/research/theduel/memphis-florida-atlantic-prediction-odds-best-bet-march-17-ncaa-tournament-game-tigers-shine-on-offense-01gvcv51qqac/
- https://www.fanduel.com/research/theduel/purdue-vs-fairleigh-dickinson-prediction-odds-best-bet-march-17-ncaa-tournament-01gvmjbg097j/
- https://www.fanduel.com/research/theduel/texas-vs-colgate-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcdechw9z/
- https://www.fanduel.com/research/theduel/texas-a-m-penn-state-prediction-odds-best-bet-march-16-ncaa-tournament-game-aggies-cannot-capitalize-01gvdxfmzfen/
- https://www.fanduel.com/research/theduel/xavier-kennesaw-state-prediction-odds-best-bet-march-17-ncaa-tournament-game-musketeers-hold-off-owls-01gvcde7rs26/
- https://www.fanduel.com/research/theduel/iowa-state-vs-pittsburgh-prediction-odds-best-bet-march-17-ncaa-tournament-game-cyclones-get-tested-early-01gvj6t5bwgw/
- https://www.fanduel.com/research/theduel/indiana-kent-state-prediction-odds-best-bet-march-17-ncaa-tournament-game-can-hoosiers-create-distance-01gvcv53460c/
- https://www.fanduel.com/research/theduel/miami-drake-prediction-odds-best-bet-march-17-ncaa-tournament-game-don-t-expect-fireworks-at-mvp-arena-01gvcddyma67/
- https://www.fanduel.com/research/theduel/iowa-vs-auburn-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcddx2fkf/
- https://www.fanduel.com/research/theduel/houston-vs-northern-kentucky-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvdpm6h8h9/
- https://www.fanduel.com/research/theduel/arizona-vs-princeton-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcde43zyd/
- https://www.fanduel.com/research/theduel/utah-state-missouri-prediction-odds-best-bet-march-16-ncaa-tournament-game-aggies-rebounding-pays-off-01gvcde972gn/
- https://www.fanduel.com/research/theduel/baylor-vs-ucsb-prediction-odds-best-bet-march-17-ncaa-tournament-game-bears-come-out-firing-denver-01gvcdefek9n/
- https://www.fanduel.com/research/theduel/creighton-vs-nc-state-prediction-odds-best-bet-march-17-ncaa-tournament-game-bluejays-thrive-paint-01gvcddzdb5p/
- https://www.fanduel.com/research/theduel/virginia-vs-furman-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcdeg5dxe/
- https://www.fanduel.com/research/theduel/san-diego-state-vs-charleston-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcdeagk9s/
- https://www.fanduel.com/research/theduel/west-virginia-vs-maryland-prediction-odds-best-bet-march-16-ncaa-tournament-game-01gvcdeby6cn/
- https://www.fanduel.com/research/theduel/alabama-vs-texas-am-cc-prediction-odds-best-bet-march-16-ncaa-tournament-game-crimson-tide-take-control-01gvj6tfzhv3/

#### 2nd round
- https://www.fanduel.com/research/theduel/ucla-northwestern-prediction-odds-best-bet-march-18-ncaa-tournament-game-bruins-punch-sweet-16-ticket-01gvqjfe8ny5/
- https://www.fanduel.com/research/theduel/gonzaga-tcu-prediction-odds-best-bet-march-19-ncaa-tournament-game-bulldogs-elevated-by-strong-start-01gvt4w93akb/
- https://www.fanduel.com/research/theduel/uconn-saint-mary-s-ca-prediction-odds-best-bet-march-19-ncaa-tournament-game-huskies-start-off-hot-01gvsq4mqtdj/
- https://www.fanduel.com/research/theduel/kansas-arkansas-prediction-odds-best-bet-march-18-ncaa-tournament-game-trust-jayhawks-to-start-hot-01gvq4r6z1w8/
- https://www.fanduel.com/research/theduel/marquette-michigan-state-prediction-odds-best-bet-march-19-ncaa-tournament-game-msu-shocks-the-world-01gvsq4qsnhq/
- https://www.fanduel.com/research/theduel/kentucky-kansas-state-prediction-odds-best-bet-march-19-ncaa-tournament-game-expect-close-fought-battle-01gvt4vxn2tn/
- https://www.fanduel.com/research/theduel/duke-vs-tennessee-prediction-odds-best-bet-march-18-ncaa-tournament-game-blue-devils-secure-sweet-16-spot-01gvqbkn2zx1/
- https://www.fanduel.com/research/theduel/fau-fairleigh-dickinson-prediction-odds-best-bet-march-19-ncaa-tournament-game-expect-a-close-game-01gvt4w8632z/
- https://www.fanduel.com/research/theduel/texas-penn-state-prediction-odds-best-bet-march-18-ncaa-tournament-game-fireworks-at-wells-fargo-arena-01gvqjfe9w0a/
- https://www.fanduel.com/research/theduel/xavier-pittsburgh-prediction-odds-best-bet-march-19-ncaa-tournament-game-musketeers-given-another-scare-01gvsq4jx731/
- https://www.fanduel.com/research/theduel/indiana-miami-prediction-odds-best-bet-march-19-ncaa-tournament-game-points-hard-to-come-by-in-albany-01gvt4w9rkhm/
- https://www.fanduel.com/research/theduel/houston-vs-auburn-prediction-odds-best-bet-march-18-ncaa-tournament-game-cougars-offense-steps-up-01gvqbkks8nh/
- https://www.fanduel.com/research/theduel/missouri-vs-princeton-prediction-odds-best-bet-march-18-ncaa-tournament-game-back-the-favorite-saturday-01gvq4r5svq2/
- https://www.fanduel.com/research/theduel/baylor-creighton-prediction-odds-best-bet-march-19-ncaa-tournament-game-offenses-thrive-in-denver-01gvsq4pcma0/
- https://www.fanduel.com/research/theduel/san-diego-state-vs-furman-prediction-odds-best-bet-march-18-ncaa-tournament-game-aztecs-defense-steps-up-01gvq4r444qh/
- https://www.fanduel.com/research/theduel/alabama-vs-maryland-prediction-odds-best-bet-march-18-ncaa-tournament-game-crimson-tide-score-with-ease-01gvq4r5nd4b/

#### 3rd round
- https://www.fanduel.com/research/theduel/ucla-gonzaga-prediction-odds-best-bet-march-23-ncaa-tournament-game-bruins-bulldogs-put-on-a-show-01gvz9ndrjw1/
- https://www.fanduel.com/research/theduel/uconn-arkansas-prediction-odds-best-bet-march-23-ncaa-tournament-game-huskies-can-t-be-slowed-down-01gvyvy5r5z8/
- https://www.fanduel.com/research/theduel/michigan-state-kansas-state-prediction-odds-best-bet-march-23-ncaa-tournament-game-wildcats-win-in-msg-01gvyvy2eps8/
- https://www.fanduel.com/research/theduel/tennessee-florida-atlantic-prediction-odds-best-bet-march-23-ncaa-tournament-game-trust-the-favorite-01gvzy949e04/
- https://www.fanduel.com/research/theduel/texas-xavier-prediction-odds-best-bet-march-24-ncaa-tournament-game-offenses-thrive-in-first-half-01gvyvy45dv9/
- https://www.fanduel.com/research/theduel/houston-miami-prediction-odds-best-bet-march-24-ncaa-tournament-game-can-the-hurricanes-play-spoiler-01gvz2sz5d06/
- https://www.fanduel.com/research/theduel/creighton-princeton-prediction-odds-best-bet-march-24-ncaa-tournament-game-defenses-shine-in-louisville-01gvyvy2hq1n/
- https://www.fanduel.com/research/theduel/alabama-vs-san-diego-state-prediction-odds-best-bet-march-24-ncaa-tournament-01gvwzanchva/

#### 4th round
- https://www.fanduel.com/research/theduel/uconn-vs-gonzaga-prediction-odds-best-bet-march-25-ncaa-elite-8-game-offenses-trade-buckets-las-vegas-01gw9k86bgf4/
- https://www.fanduel.com/research/theduel/kansas-state-vs-florida-atlantic-prediction-odds-best-bet-march-25-ncaa-elite-8-game-wildcats-punch-ticket-01gw9cckxxfk/
- https://www.fanduel.com/research/theduel/texas-miami-fl-prediction-odds-best-bet-march-26-ncaa-tournament-game-01gwc5n4km8v/
- https://www.fanduel.com/research/theduel/creighton-san-diego-state-prediction-odds-best-bet-march-26-ncaa-tournament-01gwbysc152j/

#### 5th round
- https://www.fanduel.com/research/theduel/san-diego-state-vs-florida-atlantic-prediction-odds-best-bet-april-1-ncaa-tournament-game-01gwgezkhy1p/
- https://www.fanduel.com/research/theduel/uconn-vs-miami-fl-prediction-odds-best-bet-april-1-ncaa-final-four-game-01gwgnvq5vw4/

#### 6th round (finals)
- https://www.fanduel.com/research/theduel/uconn-vs-san-diego-state-prediction-odds-best-bet-ncaa-championship-game-can-aztecs-upset-huskies-01gx10r71r89/
