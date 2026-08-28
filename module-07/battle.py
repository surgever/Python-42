from ex0 import CreatureFactory, FlameFactory, AquaFactory, print_screen


def show_factory(factory: CreatureFactory) -> None:
    print_screen(None, None, "Opening creature factory...", ["Begin"])
    base = factory.create_base()
    print_screen(base, None, base.describe(), ["Attack"])
    print_screen(base, None, base.attack(), ["Evolve"])
    evolved = factory.create_evolved()
    print_screen(evolved, None, evolved.describe(), ["Attack"])
    print_screen(evolved, None, evolved.attack(), ["Evolve"])
    fevolved = factory.create_finalevolved()
    print_screen(fevolved, None, fevolved.describe(), ["Attack"])
    print_screen(fevolved, None, fevolved.attack(), ["Battle!"])


def show_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print_screen(None, None, "Now is time to let the battle begin!", ["Begin"])
    base1 = factory1.create_base()
    print_screen(base1, None, base1.describe(), ["Versus"])
    base2 = factory2.create_base()
    print_screen(base1, base2, base2.describe(), ["Fight!"])
    print_screen(base1, base2, base1.attack(),
                 [" Attack", "Evolve", " Switch", "Exit"])
    print_screen(base1, base2, base2.attack(), ["Exit"])


if __name__ == "__main__":
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        show_factory(flame_factory)
        show_factory(aqua_factory)
        show_battle(flame_factory, aqua_factory)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
