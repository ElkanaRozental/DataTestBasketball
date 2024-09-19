from functools import partial

from toolz import pipe

from api.players_api import get_players
from api.seasons_api import get_seasons
from repository.player_repository import convert_json_to_player, create_player, get_all_players
from repository.season_repository import convert_json_to_season, get_all_seasons, create_season
from service.player_service import check_if_player_exists
from service.season_service import check_if_season_exists


def seed_players_2024():
    players = pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"),
        convert_json_to_player
    )
    for player in players:
        if check_if_player_exists(player):
            create_player(player)


def seed_seasons_2024():
    seasons = pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"),
        convert_json_to_season
    )
    for season in seasons:
        if check_if_season_exists(season):
            create_season(season)


def seed_players_2023():
    players = pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000"),
        convert_json_to_player
    )
    for player in players:
        if check_if_player_exists(player):
            create_player(player)

def seed_seasons_2023():
    seasons = pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000"),
        convert_json_to_season
    )
    for season in seasons:
        if check_if_season_exists(season):
            create_season(season)

def seed_players_2022():
    players = pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000"),
        convert_json_to_player
    )
    for player in players:
        if check_if_player_exists(player):
            create_player(player)

def seed_seasons_2022():
    seasons = pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000"),
        convert_json_to_season
    )
    for season in seasons:
        if check_if_season_exists(season):
            create_season(season)