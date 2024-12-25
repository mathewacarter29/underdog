"""
File that will populate local postgres database
"""

import csv
import psycopg2


def main():
    """
    get data from data.csv and populate database
    """
    games = []
    # open and read data.csv
    with open("data.csv", mode="r", encoding="utf-8") as file:
        csv_file = csv.reader(file)
        for i, line in enumerate(csv_file):
            # skip the title line
            if i == 0:
                continue
            # * is the "splat" operator, used for unpacking arguments
            game = Game(*line[:10])
            games.append(game)

    conn = psycopg2.connect(
        database="postgres",
        user="mathewcarter",
        password="password",
        host="localhost",
        port=5432,
    )
    cursor = conn.cursor()
    try:
        # create db tables
        create_schema = """
            CREATE SCHEMA underdog;
        """
        create_teams = """
            CREATE TABLE underdog.teams (
                name VARCHAR NOT NULL PRIMARY KEY
            );
        """
        create_sportsbook = """
            CREATE TABLE underdog.sportsbooks (
                name VARCHAR NOT NULL PRIMARY KEY
            );
        """
        create_regions = """
            CREATE TABLE underdog.regions (
                region VARCHAR NOT NULL PRIMARY KEY
            );
        """
        create_games = """
            CREATE TABLE underdog.games (
                home_team_name VARCHAR REFERENCES underdog.teams(name),
                away_team_name VARCHAR REFERENCES underdog.teams(name),
                year INTEGER,
                sportsbook VARCHAR REFERENCES underdog.sportsbooks(name),
                home_team_moneyline INTEGER,
                away_team_moneyline INTEGER,
                home_team_score INTEGER,
                away_team_score INTEGER,
                round INTEGER,
                region VARCHAR REFERENCES underdog.regions(region),
                PRIMARY KEY (home_team_name, away_team_name, year)
            );
        """
        commands = [
            create_schema,
            create_teams,
            create_sportsbook,
            create_regions,
            create_games,
        ]
        for command in commands:
            cursor.execute(command)

        # populate tables
        # 1. get unique sportsbooks, team names, and regions
        books = set()
        teams = set()
        regions = set()
        game: Game
        for game in games:
            books.add(game.sportsbook)
            teams.add(game.home_team_name)
            teams.add(game.away_team_name)
            regions.add(game.region)
        insert_book = """
            INSERT INTO underdog.sportsbooks (name) VALUES (%s);
        """
        for name in books:
            cursor.execute(insert_book, (name,))

        insert_team = """
            INSERT INTO underdog.teams (name) VALUES (%s);
        """
        for name in teams:
            cursor.execute(insert_team, (name,))

        insert_region = """
            INSERT INTO underdog.regions (region) VALUES (%s);
        """
        for name in regions:
            cursor.execute(insert_region, (name,))

        # 2. insert games into database
        insert_game = """
            INSERT INTO underdog.games (home_team_name, away_team_name, year, sportsbook, home_team_moneyline, away_team_moneyline, home_team_score, away_team_score, round, region)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for game in games:
            cursor.execute(
                insert_game,
                (
                    game.home_team_name,
                    game.away_team_name,
                    game.year,
                    game.sportsbook,
                    game.home_team_moneyline,
                    game.away_team_moneyline,
                    game.home_team_score,
                    game.away_team_score,
                    game.round,
                    game.region,
                ),
            )
        print("Populated database successfully!")
    except psycopg2.DatabaseError as e:
        print("Error creating database:", e)

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
