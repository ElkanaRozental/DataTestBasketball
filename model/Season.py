from dataclasses import dataclass


@dataclass
class Season:
    player_id: str
    team_name: str
    position: str
    season: int
    points: int
    games_amount: int
    three_attempts: int
    three_percent: float
    two_attempts: int
    two_percent: float
    assists: int
    turnovers: int
    id: int = None


season_fields = [
    "player_id",
    "team_name",
    "position",
    "season",
    "points",
    "games_amount",
    "three_attempts",
    "three_percent",
    "two_attempts",
    "two_percent",
    "assists",
    "turnovers",
    "id"
]
