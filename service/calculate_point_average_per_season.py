from typing import List
from statistics import mean
from model.Season import Season
from operator import attrgetter


def calculate_point_average_per_season(seasons: List[Season]):
    points = list(map(attrgetter("points"), seasons))
    return mean(points)