from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    result = "INVALID"
    for i in allowed:
        if i.casefold() in ingredients.casefold():
            result = "VALID"
    return ingredients + " - " + result
