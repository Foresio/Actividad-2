from src.scores import score

def recorrer_rondas(rounds):
    
    # Nuevo diccionario para almacenar la información de los players durante cada ronda
    players_de_cada_ronda = {}

    # Por cada ronda se van sacando datos
    for i, ronda_actual in enumerate(rounds, 1):
        print(f"Ranking ronda {i}:\n")
        max_score_ronda = 0

        # Se procesan los jugadores de la ronda actual
        for jugador in ronda_actual:         
            # Obtener las estadísticas del jugador en la ronda actual
            jugador_data = ronda_actual[jugador]
            jugador_score = score(jugador_data)
        
            # Se guarda la informacion del MVP de la ronda
            if jugador_score > max_score_ronda:
                max_score_ronda = jugador_score
                player_MVP = jugador
        
            # Si el jugador no está en players_de_cada_ronda, lo agregamos
            if jugador not in players_de_cada_ronda:
                players_de_cada_ronda[jugador] = {'kills': 0, 'assists': 0, 'deaths': 0, 'points': 0, 'mvps': 0}
        
            # Actualizamos los datos del jugador
            players_de_cada_ronda[jugador]['kills'] += jugador_data['kills']
            players_de_cada_ronda[jugador]['assists'] += jugador_data['assists']
            if jugador_data['deaths']:
                players_de_cada_ronda[jugador]['deaths'] += 1
            players_de_cada_ronda[jugador]['points'] += jugador_score
    
        # Incrementa el contador de MVP del jugador
        # Y de paso lo anuncia en la misma ronda
        players_de_cada_ronda[player_MVP]['mvps'] += 1
        print(f"¡Felicidades '{player_MVP}' por hacer '{max_score_ronda}' puntos y salir MVP en esta ronda!\n")

        # Hacemos el ranking de la ronda
        ranking_actual = sorted(players_de_cada_ronda.items(), key=lambda x: x[1]['points'], reverse=True)

        # Imprimimos el ranking de la ronda
        for player, data in ranking_actual:
            print(f"{player}: {data['kills']} kills, {data['assists']} assists, {data['deaths']} muertes, {data['points']} puntos, {data['mvps']} MVPs")
        print("\n")