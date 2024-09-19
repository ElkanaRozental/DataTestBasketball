from dataclasses import dataclass


@dataclass
class Season:
   player_id: str
   team: str
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