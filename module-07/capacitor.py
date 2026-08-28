from ex0 import CreatureFactory, print_screen
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability


def healing_action(factory: CreatureFactory) -> None:
    print_screen(
        None, None,
        "Opening Creature with healing capability", ["Begin"])
    base = factory.create_base()
    print_screen(base, None, base.describe(), ["Attack"])
    print_screen(base, None, base.attack(), ["Heal"])
    if isinstance(base, HealCapability):
        print_screen(base, None, base.heal(), ["Evolve"])

    evolved = factory.create_evolved()
    print_screen(evolved, None, evolved.describe(), ["Attack"])
    print_screen(evolved, None, evolved.attack(), ["Heal"])
    if isinstance(evolved, HealCapability):
        print_screen(evolved, None, evolved.heal(), ["Evolve"])

    fevolved = factory.create_finalevolved()
    print_screen(fevolved, None, fevolved.describe(), ["Attack"])
    print_screen(fevolved, None, fevolved.attack(), ["Heal"])
    if isinstance(fevolved, HealCapability):
        print_screen(fevolved, None, fevolved.heal(), ["End"])


def transform_action(factory: CreatureFactory) -> None:
    print_screen(
        None, None,
        "Opening Creature with transform capability", ["Begin"])
    base = factory.create_base()
    print_screen(base, None, base.describe(), ["Attack"])
    print_screen(base, None, base.attack(), ["Transform"])
    if isinstance(base, TransformCapability):
        print_screen(base, None, base.transform(), ["Attack"])

    print_screen(base, None, base.attack(), ["Revert"])
    if isinstance(base, TransformCapability):
        print_screen(base, None, base.revert(), ["Evolve"])

    evolved = factory.create_evolved()
    print_screen(evolved, None, evolved.describe(), ["Attack"])
    print_screen(evolved, None, evolved.attack(), ["Transform"])
    if isinstance(evolved, TransformCapability):
        print_screen(
            evolved, None, evolved.transform(),
            ["Attack", "Switch", "Evolve", "Exit"])

    print_screen(evolved, None, evolved.attack(), ["Revert"])
    if isinstance(evolved, TransformCapability):
        print_screen(evolved, None, evolved.revert(), ["End"])


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    healing_action(healing_factory)
    transform_action(transform_factory)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
