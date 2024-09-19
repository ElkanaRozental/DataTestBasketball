from repository.player_repository import get_all_players


def check_if_player_exists(player):
    return player not in get_all_players()