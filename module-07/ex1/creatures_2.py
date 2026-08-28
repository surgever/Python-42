from ex0 import CreatureFactory, Creature
from .ability import HealCapability, TransformCapability


class Bulbasaur(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bulbasaur", "Grass/Poison", "001")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a small amount"


class Ivysaur(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Ivysaur", " Grass/Poison", "002")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Venusaur(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Venusaur", " Grass/Poison", "003")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Bulbasaur()

    def create_evolved(self) -> Creature:
        return Ivysaur()

    def create_finalevolved(self) -> Creature:
        return Venusaur()


class Pikachu(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Pikachu", "Electric", "025")
        self.is_trans = False

    def attack(self) -> str:
        if self.is_trans is False:
            return f"{self.name} atacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.is_trans = True
        super().__init__("Pikachu", "Electric", "025z")
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_trans = False
        super().__init__("Pikachu", "Electric", "025")
        return f"{self.name} returns to normal."


class Raichu(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Raichu", "Electric", "026")
        self.is_trans = False

    def attack(self) -> str:
        if self.is_trans is False:
            return f"{self.name} atacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.is_trans = True
        super().__init__("Raichu", "Dragon/Flying", "149")
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_trans = False
        super().__init__("Raichu", "Electric", "26")
        return f"{self.name} stabilizes its form."


class Mewtwo(Creature):
    def __init__(self) -> None:
        super().__init__("Mewtwo", "Psychic", "150")

    def attack(self) -> str:
        return f"{self.name} uses Psychic!"


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Pikachu()

    def create_evolved(self) -> Creature:
        return Raichu()

    def create_finalevolved(self) -> Creature:
        return Mewtwo()
