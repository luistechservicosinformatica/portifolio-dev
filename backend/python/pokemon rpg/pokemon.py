import random

TIPOS = {
    "fogo": {"forte": ["planta"], "fraco": ["agua"]},
    "agua": {"forte": ["fogo"], "fraco": ["eletrico", "planta"]},
    "eletrico": {"forte": ["agua"], "fraco": ["terra"]},
    "planta": {"forte": ["agua"], "fraco": ["fogo"]},
}

class Pokemon:
    def __init__(self, nome, tipo, level=1):
        self.nome = nome
        self.tipo = tipo
        self.level = level
        self.xp = 0
        self.vida_max = level * 20
        self.vida = self.vida_max
        self.ataque = level * 5
        self.status = None

    def __str__(self):
        return f"{self.nome} (Lv.{self.level}) [{self.tipo}]"

    def esta_vivo(self):
        return self.vida > 0

    def aplicar_status(self):
        if self.status == "burn":
            dano = int(self.vida_max * 0.05)
            self.vida -= dano
            print(f"{self.nome} sofre {dano} de burn")
        elif self.status == "poison":
            dano = int(self.vida_max * 0.08)
            self.vida -= dano
            print(f"{self.nome} sofre {dano} de poison")

    def tentar_aplicar_status(self, alvo):
        chance = random.random()
        if chance < 0.2:
            alvo.status = random.choice(["burn", "poison", "stun"])
            print(f"{alvo.nome} foi afetado por {alvo.status}!")

    def ganhar_xp(self, xp):
        self.xp += xp
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.vida_max += 10
        self.ataque += 3
        self.vida = self.vida_max
        print(f"{self.nome} subiu para nível {self.level}!")

    def multiplicador(self, alvo):
        if alvo.tipo in TIPOS[self.tipo]["forte"]:
            return 1.5
        if alvo.tipo in TIPOS[self.tipo]["fraco"]:
            return 0.5
        return 1

    def atacar(self, alvo):
        if self.status == "stun":
            print(f"{self.nome} está atordoado!")
            self.status = None
            return False

        critico = 2 if random.random() < 0.1 else 1

        mult = self.multiplicador(alvo)

        dano = int(self.ataque * random.uniform(0.7, 1.3) * mult * critico)
        alvo.vida -= dano

        print(f"{self.nome} causou {dano} dano em {alvo.nome}")

        if critico > 1:
            print("CRÍTICO!")

        self.tentar_aplicar_status(alvo)

        if alvo.vida <= 0:
            print(f"{alvo.nome} foi derrotado!")
            self.ganhar_xp(50)
            return True

        return False
