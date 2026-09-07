from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def burn(target: str, power: int) -> str:
    return f"Burn scorch {target} for {power} damage"


def aura(target: str, power: int) -> str:
    return f"Aura enhanced {target} for {power} HP"


def attack(target: str, power: int) -> str:
    return f"Atacked {target} for {power} damage"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditioned_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditioned_spell


def dragon_protects(target: str, power: int) -> bool:
    '''Other targets always receive damage but dragons only over 25'''
    return target != "Dragon" or power > 25


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def row_of_spells(target: str, power: int) -> list[str]:
        spells_output: list[str] = []
        for spell in spells:
            spells_output.append(spell(target, power))
        return spells_output
    return row_of_spells


def main() -> None:
    test_targets = ['Wizard', 'Knight', 'Dragon', 'Goblin']

    print("\nTesting spell combiner...")
    combined = spell_combiner(heal, aura)
    print("Combined spell result:", combined(test_targets[0], 10))

    print("\nTesting power amplifier...")
    triple_burn = power_amplifier(burn, 3)
    print("Amplified spell result:", triple_burn(test_targets[1], 10))

    print("\nTesting conditional caster...")
    dragon_protected = conditional_caster(dragon_protects, attack)
    print("Conditional spell result:", dragon_protected(test_targets[3], 10))
    print("Conditional spell result:", dragon_protected(test_targets[2], 10))
    print("Conditional spell result:", dragon_protected(test_targets[2], 50))

    print("\nTesting sequence of spells...")
    sequencer = spell_sequence([burn, attack, heal])
    print("Spell sequence result:", sequencer(test_targets[3], 20))


if __name__ == "__main__":
    main()
