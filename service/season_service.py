from repository.season_repository import get_all_seasons


def check_if_season_exists(season):
    return season not in get_all_seasons()