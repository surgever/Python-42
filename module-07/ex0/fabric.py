from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(
            self, name: str, creature_type: str, number: str = "150"
    ) -> None:
        self.name: str = name.upper()
        self.type: str = creature_type
        self.number: str = number.zfill(3)

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    def info(self) -> str:
        return f"{self.name:<10}{self.type:>10}"[:20]

    def render(self, photogram: str = "f1") -> str:
        return f"ex0/sprites/{self.number}-{photogram}.txt"
        pass


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass

    @abstractmethod
    def create_finalevolved(self) -> Creature:
        pass
