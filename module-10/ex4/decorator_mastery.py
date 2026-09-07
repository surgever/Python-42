from functools import wraps
from collections.abc import Callable
import re
import time

# Master's Tower Test Data
test_powers = [15, 29, 22, 29]
spell_names = ['earthquake', 'heal', 'flash', 'lightning']
mage_names = ['Rowan', 'Alex', 'Ash', 'Kai', 'Morgan', 'Nova']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:

        print("Casting", func.__name__)
        start_time = time.time()
        output = func(*args, **kwargs)
        timer = time.time() - start_time
        print(f"Spell completed in {timer:.3f} seconds")
        return output
    return wrapper


def power_validator(min_power: int) -> Callable[[Callable], Callable]:
    '''A decorator factory takes arguments
    and has the decorator function inside'''
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:

            if isinstance(args[0], int):
                power = args[0]
            else:
                power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except TypeError:
                    print(f"Spell failed, retrying... ({1+i}/{max_attempts})")
                    continue
                else:
                    break
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pattern = r"[a-zA-Z\s]+"
        if len(name) >= 3 and re.fullmatch(pattern, name):
            return True
        else:
            return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def add_a_lot(end: int) -> str:
    sum = 0
    for n in range(0, end):
        sum += n
    return f"Result: total spell is {sum}!"


@power_validator(20)
def attack(power: int, move: str) -> str:
    return f"Foe used {move} for {power} damage"


@retry_spell(3)
def burn(type: str) -> str:
    if type == "fire":
        return "Foe burned with real fire"
    else:
        raise TypeError("Burn couldn't be performed!")


if __name__ == "__main__":
    print("Testing spell timer...")
    print(add_a_lot(50000))

    print("Testing power validator...")
    print(attack(10, "Tail whip"))
    print(attack(25, "Scratch"))
    print(attack(155, "Hyper power"))

    print("Testing retrier...")
    print(burn("water"))
    print(burn("fire"))

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Paco"))
    print(guild.validate_mage_name("Paco23"))
    print(guild.cast_spell("Fireball", 25))
    print(guild.cast_spell("Fireball", 9))
