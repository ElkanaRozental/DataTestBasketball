def calculate_ppg_ratio(points, avg_position_per_year):
    if avg_position_per_year > 0:
        return points / avg_position_per_year
    else:
        return points