def pokemonBattle(attacker, defender, atack, defense):
    effec_dic = {
        "Agua": {"Agua": 1, "Fuego": 2, "Planta": 0.5, "Eléctrico": 1},
        "Fuego": {"Agua": 0.5, "Fuego": 1, "Planta": 2, "Eléctrico": 1},
        "Planta": {"Agua": 2, "Fuego": 0.5, "Planta": 1, "Eléctrico": 1},
        "Eléctrico": {"Agua": 2, "Fuego": 1, "Planta": 1, "Eléctrico": 0.5}
    }

    damage = 50 * (atack / defense) * (effec_dic[attacker][defender])
    return damage


print(pokemonBattle("Agua", "Fuego", 56, 50))
