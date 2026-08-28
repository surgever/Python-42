from .fabric import Creature, CreatureFactory


class Charmander(Creature):
    def __init__(self) -> None:
        super().__init__("Charmander", "Fire", "004")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Charmeleon(Creature):
    def __init__(self) -> None:
        super().__init__("Charmeleon", "Fire", "005")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Charizard(Creature):
    def __init__(self) -> None:
        super().__init__("Charizard", "Fire", "006")

    def attack(self) -> str:
        return f"{self.name} uses Fire Spin!"


class Squirtle(Creature):
    def __init__(self) -> None:
        super().__init__("Squirtle", "Water", "007")

    def attack(self) -> str:
        return f"{self.name} uses Bubble Gun!"


class Wartortle(Creature):
    def __init__(self) -> None:
        super().__init__("Wartortle", "Water", "008")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Blastoise(Creature):
    def __init__(self) -> None:
        super().__init__("Blastoise", "Water", "009")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Charmander()

    def create_evolved(self) -> Creature:
        return Charmeleon()

    def create_finalevolved(self) -> Creature:
        return Charizard()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Squirtle()

    def create_evolved(self) -> Creature:
        return Wartortle()

    def create_finalevolved(self) -> Creature:
        return Blastoise()
