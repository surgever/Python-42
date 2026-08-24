from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    result = "INVALID"
    for i in allowed:
        if i.casefold() in ingredients.casefold():
            result = "VALID"
    return ingredients + " - " + result
