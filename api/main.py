"""
API driver file
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
import psycopg2


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    runs on API startup - sets up database connection
    """
    #TODO put username and password in .env
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port=5432,
    )
    app.state.db_connection = conn
    yield
    app.state.db_connection.close()


server = FastAPI(lifespan=lifespan)

@server.get("/games", status_code=status.HTTP_200_OK)
def get_games(year: int, response: Response):
    """
    main get endpoint
    """
    try:
        conn = server.state.db_connection
        cursor = conn.cursor()
        # create cursor
        get_games_query = """
            SELECT * FROM underdog.games WHERE year=%s;
        """
        cursor.execute(get_games_query, (year,))
        result = cursor.fetchall()
        games = {"games": []}
        for db_game in result:
            games["games"].append(create_game_dict(db_game))

        cursor.close()
        return games

    except psycopg2.OperationalError:
        response.status_code = status.HTTP_424_FAILED_DEPENDENCY
        return {"message": "error connecting to database"}
    
####################
# HELPER FUNCTIONS #
####################

def create_game_dict(game):
    """
    create a game dictionary object out of the tuple returned from the database query
    game[0] = home team name
    game[1] = away team name
    game[2] = year of tournament
    game[3] = sportsbook (as of now, just Fanduel)
    game[4] = home team moneyline odds
    game[5] = away team moneyline odds
    game[6] = home team final score
    game[7] = away team final score
    game[8] = round of tournament where game took place
    game[9] = region of tournament (east, midwest, national, etc.)
    """
    result = {
        "homeTeamName": game[0],
        "awayTeamName": game[1],
        "year": game[2],
        "sportsbook": game[3],
        "homeTeamMoneyline": game[4],
        "awayTeamMoneyline": game[5],
        "homeTeamScore": game[6],
        "awayTeamScore": game[7],
        "round": game[8],
        "region": game[9],
    }
    return result
