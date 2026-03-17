class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.pokemons = []
        self.inventario = {"pocao": 2, "pokebola": 3}

    def escolher_pokemon(self):
        for i, p in enumerate(self.pokemons):
            print(f"{i} - {p} HP:{p.vida}/{p.vida_max}")
        return self.pokemons[int(input("Escolha: "))]

class Player(Pessoa):
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"Capturou {pokemon}")
