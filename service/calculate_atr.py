def calculate_atr(assists, turnovers):
    if turnovers > 0:
        return assists / turnovers
    else:
        return assists

