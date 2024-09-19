import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)


def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Players (
                name VARCHAR(100),
                player_id VARCHAR(100) PRIMARY KEY
            )
            ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Seasons (
            id SERIAL PRIMARY KEY,
            player_id VARCHAR(100),
            team_name VARCHAR(100) NOT NULL,
            position VARCHAR(100),
            season INT,
            points INT,
            games_amount INT,
            three_attempts INT,
            three_percent DOUBLE PRECISION,
            two_attempts INT,
            two_percent DOUBLE PRECISION,
            assists INT,
            turnovers INT,
            FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS fantasy_teams (
                id SERIAL PRIMARY KEY,
                position_C VARCHAR(100),               
                position_PF VARCHAR(100),
                position_SF VARCHAR(100),
                position_SG VARCHAR(100),
                position_PG VARCHAR(100),
                FOREIGN KEY (position_C) REFERENCES players(player_id) ON DELETE CASCADE,
                FOREIGN KEY (position_PF) REFERENCES players(player_id) ON DELETE CASCADE,
                FOREIGN KEY (position_SF) REFERENCES players(player_id) ON DELETE CASCADE,
                FOREIGN KEY (position_SG) REFERENCES players(player_id) ON DELETE CASCADE,
                FOREIGN KEY (position_PG) REFERENCES players(player_id) ON DELETE CASCADE
            )
            ''')
    connection.commit()
    cursor.close()
    connection.close()