def score(player):
    # Devuelve los puntos del jugador según su estadística
    kill_score = player.get("kills") * 3
    assist_score = player.get("assists") * 1
    if player.get("death"):
        death_score = -1
    else:
        death_score = 0
    return kill_score + assist_score + death_score