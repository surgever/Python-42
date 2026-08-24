
def light_spell_allowed_ingredients() -> list[str]:
    return [
        "earth", "air", "fire", "water"
    ]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    val_ing = validate_ingredients(ingredients)
    return f"Spell recorded: 🪄 {spell_name} ({val_ing})"
