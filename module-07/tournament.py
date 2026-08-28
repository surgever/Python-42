from ex0 import CreatureFactory, FlameFactory, AquaFactory, print_screen
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, StrategyError,
    NormalStrategy, AggressiveStrategy, DefensiveStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print_screen(None, None, "Tournament. "
                 + f"{len(opponents)} opponents involved", ["Begin"])

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            fighter1 = factory1.create_base()
            fighter2 = factory2.create_base()
            print_screen(None, None, "Let's start the battle!", ["Start"])
            print_screen(fighter1, fighter2, fighter1.describe(), ["Versus"])
            print_screen(fighter1, fighter2, fighter2.describe(), ["Fight"])
            print_screen(fighter1, fighter2, "Now fight!", ["Action"])
            try:
                strategy1.act(fighter1, (fighter1, fighter2))
                strategy2.act(fighter2, (fighter1, fighter2))
            except StrategyError as e:
                print_screen(None, None,
                             f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print_screen(None, None, "Tournament 0 (basic)", ["Go"])
    print_screen(
        None, None, "Flame: Normal, Healing: Defensive", ["Go"])
    battle([
        (flame_factory, normal),
        (healing_factory, defensive)
    ])

    print_screen(None, None, "Tournament 1 (error)", ["Go"])
    print_screen(
        None, None, "Flame: Aggressive, Healing: Defensive", ["Go"])
    battle([
        (flame_factory, aggressive),
        (healing_factory, defensive)
    ])

    print_screen(None, None, "Tournament 2 (multiple)", ["Go"])
    print_screen(
        None, None,
        "Aqua: Normal, Healing: Defensive,"
        + "Transform: Aggressive", ["Go"])
    battle([
        (aqua_factory, normal),
        (healing_factory, defensive),
        (transform_factory, aggressive)
    ])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
