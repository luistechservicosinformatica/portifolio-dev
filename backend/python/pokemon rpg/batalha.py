from save import salvar, carregar
from colorama import Fore, Style, init
init(autoreset=True)


def batalha(player, inimigo):
    p1 = player.escolher_pokemon()
    p2 = inimigo.escolher_pokemon()

    print(Fore.YELLOW + f"\nBATALHA: {p1} VS {p2}\n")

    while p1.esta_vivo() and p2.esta_vivo():
        p1.aplicar_status()
        p2.aplicar_status()

        print(Fore.CYAN + f"\nSeu Pokémon: {p1.nome} HP: {p1.vida}/{p1.vida_max}")
        print(Fore.RED + f"Inimigo: {p2.nome} HP: {p2.vida}/{p2.vida_max}")

        print(Style.BRIGHT + "\n1-Atacar  2-Item  3-Fugir")
        escolha = input("> ")

        if escolha == "1":
            if p1.atacar(p2):
                print(Fore.GREEN + "\nVocê venceu!")
                return

            if p2.atacar(p1):
                print(Fore.RED + "\nVocê perdeu!")
                return

        elif escolha == "2":
            print(Fore.YELLOW + f"\nInventário: {player.inventario}")
            item = input("Item (pocao/pokebola): ").lower()

            if item == "pocao":
                if player.inventario.get("pocao", 0) > 0:
                    p1.vida += 20
                    if p1.vida > p1.vida_max:
                        p1.vida = p1.vida_max
                    player.inventario["pocao"] -= 1
                    salvar(player)
                    print(Fore.GREEN + f"{p1.nome} curou 20 de vida!")
                else:
                    print(Fore.RED + "Você não tem poções!")

            elif item == "pokebola":
                if player.inventario.get("pokebola", 0) > 0:
                    player.inventario["pokebola"] -= 1
                    print(Fore.YELLOW + "Tentando capturar...")

                    import random
                    chance = 0.5 if p2.vida < (p2.vida_max / 2) else 0.2

                    if random.random() < chance:
                        print(Fore.GREEN + f"Você capturou {p2.nome}!")
                        player.pokemons.append(p2)
                        salvar(player)
                        return
                    else:
                        print(Fore.RED + "Falhou!")

                else:
                    print(Fore.RED + "Você não tem pokebolas!")

            else:
                print(Fore.RED + "Item inválido!")

        elif escolha == "3":
            print(Fore.YELLOW + "Fugiu!")
            salvar(player)
            return

        else:
            print(Fore.RED + "Opção inválida!")
