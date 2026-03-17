import random
from pokemon import Pokemon
from pessoa import Player, Pessoa
from batalha import batalha
from save import salvar, carregar

def gerar():
    tipos = ["fogo", "agua", "eletrico", "planta"]
    nomes = ["Charmander", "Squirtle", "Pikachu", "Bulbasaur"]
    i = random.randint(0, 3)
    return Pokemon(nomes[i], tipos[i], level=random.randint(1, 3))


if __name__ == "__main__":
    player = carregar(Pokemon, Player)

    if not player:
        nome = input("Seu nome: ")
        player = Player(nome)

    for _ in range(3):
        player.capturar(gerar())

    while True:
        print("\n1-Explorar  2-Batalhar  3-Equipe  0-Sair")
        op = input("> ")

        if op == "1":
            p = gerar()
            print(f"Encontrou {p}")
            salvar(player)

        elif op == "2":
            inimigo = Pessoa("Gary")
            inimigo.pokemons = [gerar()]
            batalha(player, inimigo)
            salvar(player)

        elif op == "3":
            player.escolher_pokemon()
            salvar(player)

        elif op == "0":
            salvar(player)
            break
