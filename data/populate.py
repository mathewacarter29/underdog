"""
File that will populate local postgres database
"""

import csv
import psycopg2


def main():
    """
    get data from data.csv and populate database
    """
    rows = []
    # open and read data.csv
    with open("data.csv", mode="r", encoding="utf-8") as file:
        csv_file = csv.reader(file)
        for i, line in enumerate(csv_file):
            if i in (0, 1):
                continue
            # * is the "splat" operator, used for unpacking arguments
            game = Game(*line[:10])
            rows.append(game)

    conn = psycopg2.connect(
        database="postgres",
        user="mathewcarter",
        password="password",
        host="localhost",
        port=5432,
    )
    cursor = conn.cursor()
    create_schema = """
        CREATE SCHEMA underdog;
    """
    create_teams = """
        CREATE TABLE underdog.teams (
            name VARCHAR NOT NULL PRIMARY KEY
        );
    """
    create_sportsbook = """
        CREATE TABLE underdog.sportsbook (
            name VARCHAR NOT NULL PRIMARY KEY
        );
    """
    create_games = """
        CREATE TABLE underdog.games (
            home_team_name VARCHAR REFERENCES underdog.teams(name),
            away_team_name VARCHAR REFERENCES underdog.teams(name),
            year INTEGER,
            sportsbook VARCHAR REFERENCES underdog.sportsbook(name),
            home_team_moneyline INTEGER,
            away_team_moneyline INTEGER,
            home_team_score INTEGER,
            away_team_score INTEGER,
            PRIMARY KEY (home_team_name, away_team_name, year)
        );
    """
    commands = [create_schema, create_teams, create_sportsbook, create_games]
    for command in commands:
        cursor.execute(command)

    # Fetch all rows from database
    # record = cursor.fetchall()
    # print("Data from Database:- ", record)
    conn.commit()
    conn.close()
    cursor.close()



class Game:
    """
    Class representing one row from csv file
    """

    def __init__(
        self,
        home_team_name,
        away_team_name,
        year,
        sportsbook,
        home_team_moneyline,
        away_team_moneyline,
        home_team_score,
        away_team_score,
        tournament_round,
        region,
    ):
        self.home_team_name = home_team_name
        self.away_team_name = away_team_name
        self.year = year
        self.sportsbook = sportsbook
        self.home_team_moneyline = home_team_moneyline
        self.away_team_moneyline = away_team_moneyline
        self.home_team_score = home_team_score
        self.away_team_score = away_team_score
        self.round = tournament_round
        self.region = region

    def __str__(self):
        result = f"[{self.year} - "
        result += f"{self.home_team_name} ({int(self.home_team_moneyline):+g}) vs. "
        result += f"{self.away_team_name} ({int(self.away_team_moneyline):+g})"
        result += "]"
        return result


if __name__ == "__main__":
    main()
