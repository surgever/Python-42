from abc import ABC, abstractmethod
from ex0 import Creature, print_screen
from ex1 import HealCapability, TransformCapability


class StrategyError(Exception):
    def __init__(self, creature_name: str, strategy_name: str) -> None:
        self.message = "Invalid Creature "
        f"for this {strategy_name} strategy"
        super().__init__(self.message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature,
            oponents: tuple[Creature, Creature]) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature,
            oponents: tuple[Creature, Creature]) -> None:
        if not self.is_valid(creature):
            StrategyError(creature.name, "normal")
        print_screen(oponents[0], oponents[1], creature.attack(), ["Next"])


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature,
            oponents: tuple[Creature, Creature]) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature.name, "aggressive")

        if isinstance(creature, TransformCapability):
            print_screen(oponents[0], oponents[1], creature.transform())
            print_screen(oponents[0], oponents[1], creature.attack())
            print_screen(oponents[0], oponents[1], creature.revert(), ["Next"])


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature,
            oponents: tuple[Creature, Creature]) -> None:
        if not self.is_valid(creature):
            raise StrategyError(creature.name, "defensive")

        if isinstance(creature, HealCapability):
            print_screen(oponents[0], oponents[1], creature.attack())
            print_screen(oponents[0], oponents[1], creature.heal(), ["Next"])
