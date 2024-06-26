from functools import reduce

# Punto 1: Crear una estructura de datos: Diccionario dentro de diccionario
def statistics (player_list, goals, goals_avoided, assists):
    # Create a list of stadistics by player
    stats = list(zip(goals, goals_avoided, assists))
    # Create a dictionary with player and stats
    stats_dict = dict(zip(player_list, stats))
    return stats_dict

# Punto 2: Identificar goleador
def high_scorer(stats):
    scored = max(stats[player][0] for player in stats)
    high_scorer = dict(filter(lambda x: (x[1][0]) == scored, stats.items()))
    return high_scorer


# Punto 3: Identificar jugador más influyente
def calc_influence(player_list, goal, avoided, assist):
    # Formula to calculate influence
    influence = lambda goal, avoided, assist: goal*1.5 + avoided*1.25 + assist
    # Create list of influence of all players 
    influence_list = list(map(influence, goal, avoided, assist))
    max_influence = max(influence_list)
    max_player = []
    # Identify all high influence players
    for player in player_list:
        if influence_list[player_list.index(player)] == max_influence:
            max_player.append(player)
    return max_player, max_influence

# Punto 4: Promedio de goles del equipo
def team_goals_average (match, goals):
    average_team = sum(goals)/match
    return average_team

# Punto 5: Promedio de goles del goleador
def player_goals_average (goals, match):
    average = goals/match
    return average