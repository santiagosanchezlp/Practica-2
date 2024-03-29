from functools import reduce

# Punto 1: Crear una estructura de datos: Diccionario dentro de diccionario
def statistics (player_list, goals, goals_avoided, assists):
    stats = {}
    for player in range(0, len(player_list)):
        stats[player_list[player]] = player_stats(goals[player], goals_avoided[player], assists[player])
    return stats

def player_stats (goals, goals_avoided, assists):
    st = {}
    st["Goals"] = goals
    st["Goals avoided"] = goals_avoided
    st["Assist"] = assists
    return st

# Punto 2: Identificar goleador
def high_scorer(player_list, goals):
"""Dado un listado de jugadores y un listado de goles convertidos ordenados de forma que los elementos en la misma posición corresponden a un mismo jugador o jugadora,
devuelve el nombre del goleador o goleadora y la cantidad de goles convertidos"""
    scored = max(goals)
    goal_scorer = player_list[goals.index(max(goals))]
    return goal_scorer, scored

# Punto 4
def team_goals_average (match, goals):
    average_team = sum(goals)/match
    return average_team

# Punto 5
def player_goals_average (goals, match):
    average = goals/match
    return average