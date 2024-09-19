from flask import Flask

from controller.player_controller import players_blueprint
from repository.database import create_tables
from service.seed import seed_players_2024, seed_seasons_2024, seed_players_2023, seed_seasons_2023, seed_players_2022, \
    seed_seasons_2022

app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    seed_players_2024()
    seed_seasons_2024()
    seed_players_2023()
    seed_seasons_2023()
    seed_players_2022()
    seed_seasons_2022()
    app.register_blueprint(players_blueprint, url_prefix="/api/players")
    app.run(debug=True)