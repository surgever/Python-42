from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def add_mage() -> int:
        nonlocal count
        count += 1
        return count

    return add_mage


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def add_power(increase: int) -> int:
        nonlocal power
        power += increase
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    desc = enchantment_type

    def apply_enchantment(item: str) -> str:
        nonlocal desc
        desc += " " + item
        return desc

    return apply_enchantment


def memory_vault() -> dict[str, Callable]:

    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        vault[key] = value
        return value

    def recall(key: str) -> str:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("\nTesting mage counter...")
    fire_mages = mage_counter()
    water_mages = mage_counter()
    print("Count fire mages:", fire_mages())
    print("Count fire mages again:", fire_mages())
    print("Count water mages:", water_mages())

    print("\nTesting spell accumulator...")
    accumulated_power = spell_accumulator(100)
    print("Base 100, add 20:", accumulated_power(20))
    print("Base 100, add 30:", accumulated_power(30))

    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    print(fire("Sword"))
    ice = enchantment_factory("Frozen")
    print(ice("Shield"))

    print("\nTesting memory vault")
    memo = memory_vault()
    print("Store 'secret' =", memo["store"]("secret", "42"))
    print("Recall 'secret':", memo["recall"]("secret"))
    print("Recall 'unknown':", memo["recall"]("unknown"))
