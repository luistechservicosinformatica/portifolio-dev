import json
import os

SAVE_FILE = "save.json"


def salvar(player):
    dados = {
        "nome": player.nome,
        "inventario": player.inventario,
        "pokemons": []
    }

    for p in player.pokemons:
        dados["pokemons"].append({
            "nome": p.nome,
            "tipo": p.tipo,
            "level": p.level,
            "xp": p.xp,
            "vida": p.vida,
            "vida_max": p.vida_max,
            "ataque": p.ataque,
            "status": p.status
        })

    with open(SAVE_FILE, "w") as f:
        json.dump(dados, f, indent=4)

    print("Jogo salvo!")


def carregar(Pokemon, Player):
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        dados = json.load(f)

    player = Player(dados["nome"])
    player.inventario = dados["inventario"]

    for p in dados["pokemons"]:
        poke = Pokemon(p["nome"], p["tipo"], p["level"])
        poke.xp = p["xp"]
        poke.vida = p["vida"]
        poke.vida_max = p["vida_max"]
        poke.ataque = p["ataque"]
        poke.status = p["status"]

        player.pokemons.append(poke)

    print("Save carregado!")
    return player
