from typing import List
from model.Player import Player
from repository.database import get_db_connection
from service.calculate_atr import calculate_atr
from service.calculate_ppg_ratio import calculate_ppg_ratio
from service.calculate_point_average_per_season import calculate_point_average_per_season
from repository.season_repository import convert_json_to_season
from model.Season import Season, season_fields
import toolz as t


def convert_json_to_player(json) -> List[Player]:
    return [Player(name=player["playerName"], player_id=player["playerId"]) for player in json]


def create_player(player):
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("""
                INSERT INTO players (name, player_id)
                VALUES (%s, %s) RETURNING player_id
            """, (player.name, player.player_id))
            res = cu.fetchone()['player_id']
            dbc.commit()
            return res


def get_all_players():
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("SELECT * FROM players")
            res = cu.fetchall()
            players = [Player(**p) for p in res]
            return players


def get_players_by_position_and_season(position, season):
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("SELECT * FROM players INNER JOIN seasons ON"
                       " players.player_id = seasons.player_id WHERE position = %s AND season = %s", (position, season))
            res = cu.fetchall()

            def only_season_keys(key: str):
                return key in season_fields

            all_seasons = t.pipe(
                res,
                t.partial(map, t.partial(t.keyfilter, only_season_keys)),
                t.partial(map, lambda s: Season(**s)),
                list
            )
            players = [{'name': p['name'], 'team': p['team_name'],
                        'position': p['position'], 'season': p['season'], 'points': p['points'],
                        'games': p['games_amount'], 'twoPercent': p['two_percent'], 'threePercent': p['three_percent'],
                        'atr': calculate_atr(p['assists'], p['turnovers']),
                        'PPG Ratio': calculate_ppg_ratio(p['points'], calculate_point_average_per_season(all_seasons))}
                       for p in res]
            return players
