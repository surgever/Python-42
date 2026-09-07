from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    match operation:
        case "add":
            return reduce(add, spells)
        case "multiply":
            return reduce(mul, spells)
        case "max":
            return reduce(lambda x, y: x if x > y else y, spells)
        case "min":
            return reduce(lambda x, y: x if x < y else y, spells)
        case _:
            raise ValueError(f"Unknown operation: {operation}")


def basic_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} was hit by a {element} attack of power {power}."


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': partial(base_enchantment, power=50, element='fire'),
        'ice': partial(base_enchantment, power=50, element='ice'),
        'dragon': partial(base_enchantment, power=50, element='dragon'),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(s: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _1(s: int) -> str:
        return f"{s} damage"

    @dispatch.register(str)
    def _2(s: str) -> str:
        return f"{s}"

    @dispatch.register(list)
    def _3(s: list[Any]) -> str:
        return f"{len(s)} spells"

    return dispatch


if __name__ == "__main__":

    print("\nTesting spell reducer...")
    spell_powers = [20, 40, 30, 10]
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))

    print("\nTesting partial enchanter...")
    partial_spell = partial_enchanter(basic_enchantment)
    print(partial_spell['fire'](target="Fairy"))
    print(partial_spell['ice'](target="Dragon"))
    print(partial_spell['dragon'](target="Knight"))

    print("\nTesting memoized fibonacci...")
    print("Fib (0)", memoized_fibonacci(0))
    print("Fib (1)", memoized_fibonacci(1))
    print("Fib (10)", memoized_fibonacci(10))
    print("Fib (15)", memoized_fibonacci(15))
    # print("Fib (100)", memoized_fibonacci(100))
    # print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print("Damage spell:", dispatcher(54))
    print("Enchantment:", dispatcher("fireball"))
    print("Multi-cast:", dispatcher(spell_powers))
    print(dispatcher(partial))
