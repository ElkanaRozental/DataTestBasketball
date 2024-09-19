import pytest

from model.Season import Season
from repository.database import create_tables, get_db_connection
from repository.player_repository import create_player
from repository.season_repository import create_season, get_all_seasons
from service.seed import seed_seasons_2024


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    seed_seasons_2024()
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DROP Table players cascade")
    connection.commit()
    cursor.close()
    connection.close()


def test_create_player(setup_database):
    season = Season(player_id="elkana22", team="www", position="w", season="2023", points=2345, games_amount=234,
                    three_attempts=123, three_percent=0.89, two_attempts=123, two_percent=0.78, assists=12, turnovers=12)
    res = create_season(season)
    print(res)
    assert res


def test_get_all_players(setup_database):
    res = get_all_seasons()
    print(res)
    assert res