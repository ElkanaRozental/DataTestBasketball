from typing import List

from model.FantasyTeam import FantasyTeam
from repository.database import get_db_connection


def create_team(team: FantasyTeam):
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("""
                INSERT INTO fantasy_team (position_C, position_PF, position_SF, position_SG, position_PG)
                VALUES (%s, %s) RETURNING id
            """, (team.position_C, team.position_PF, team.position_SF, team.position_SG, team.position_PG))
            res = cu.fetchone()['id']
            dbc.commit()
            return res


def get_all_teams():
    with get_db_connection() as dbc:
        with dbc.cursor() as cu:
            cu.execute("SELECT * FROM fantasy_team")
            res = cu.fetchall()
            team = [FantasyTeam(**p) for p in res]
            return team