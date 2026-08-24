
from alchemy.elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    return ("Healing potion brewed with "
            + f"'{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            + f"'{create_fire()}' and '{create_water()}'")
