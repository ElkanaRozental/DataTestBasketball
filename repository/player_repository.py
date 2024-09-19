from typing import List
from model.Player import Player
from repository.database import get_db_connection


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

