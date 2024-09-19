from typing import List

from model.Season import Season
from repository.database import get_db_connection


def convert_json_to_season(json) -> List[Season]:
    return [Season(
        player_id=season["playerId"],
        team_name=season['team'],
        position=season['position'],
        season=season['season'],
        points=season['points'],
        games_amount=season['games'],
        three_attempts=season['threeAttempts'],
        three_percent=season['threePercent'],
        two_attempts=season['twoAttempts'],
        two_percent=season['twoPercent'],
        assists=season['assists'],
        turnovers=season['turnovers']
    ) for season in json]


def create_season(season):
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("""
                INSERT INTO seasons (player_id, team_name, position, season, points, games_amount, three_attempts,
                 three_percent, two_attempts, two_percent, assists, turnovers)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (season.player_id, season.team_name, season.position,season.season, season.points,
                  season.games_amount, season.three_attempts, season.three_percent,
                  season.two_attempts, season.two_percent, season.assists, season.turnovers))
            res = cu.fetchone()['id']
            dbc.commit()
            return res


def get_all_seasons():
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("SELECT * FROM seasons")
            res = cu.fetchall()
            seasons = [Season(**s) for s in res]
            return seasons
