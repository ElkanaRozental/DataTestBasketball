import pytest

from model.Player import Player
from repository.database import create_tables, get_db_connection
from repository.player_repository import create_player, get_all_players
from service.seed import seed_players_2024


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    seed_players_2024()
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DROP Table players cascade")
    connection.commit()
    cursor.close()
    connection.close()


def test_create_player(setup_database):
    player = Player(name="elkana", player_id="elkana22")
    res = create_player(player)
    print(res)
    assert res


def test_get_all_players(setup_database):
    res = get_all_players()
    print(res)
    assert len(res) > 0