from dataclasses import dataclass


@dataclass
class FantasyTeam:
    position_C: int
    position_PF: int
    position_SF: int
    position_SG: int
    position_PG: int
    id: int = None