from functools import partial

from toolz import pipe

from api.players_api import get_players
from api.seasons_api import get_seasons
from repository.player_repository import convert_json_to_player, create_player, get_all_players
from repository.season_repository import convert_json_to_season, get_all_seasons


def seed_players_2024():
    return pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"),
        [create_player(player) for player in partial(convert_json_to_player)
         if player not in get_all_players()]
    )


def seed_seasons_2024():
    return pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"),
        [create_player(season) for season in partial(convert_json_to_season)
         if season not in get_all_seasons()]
    )


def seed_players_2023():
    return pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000"),
        [create_player(player) for player in partial(convert_json_to_player)
         if player not in get_all_players()]
    )


def seed_seasons_2023():
    return pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000"),
        [create_player(season) for season in partial(convert_json_to_season)
         if season not in get_all_seasons()]
    )


def seed_players_2022():
    return pipe(
        get_players("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000"),
        [create_player(player) for player in partial(convert_json_to_player)
         if player not in get_all_players()]
    )


def seed_seasons_2022():
    return pipe(
        get_seasons("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000"),
        [create_player(season) for season in partial(convert_json_to_season)
         if season not in get_all_seasons()]
    )