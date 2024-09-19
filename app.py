from flask import Flask

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

    app.run(debug=True)