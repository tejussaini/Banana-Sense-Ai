RULES = {
    "Green": {"shelf_life_days": 7, "advice": "Not ready to eat yet."},
    "Semi-ripe": {"shelf_life_days": 4, "advice": "Ready in a day or two."},
    "Ripe": {"shelf_life_days": 2, "advice": "Best eaten now."},
    "Overripe": {"shelf_life_days": 0, "advice": "Use immediately for baking."},
}


class UnknownClassError(KeyError):
    pass


def estimate(predicted_class: str) -> dict:
    try:
        return RULES[predicted_class]
    except KeyError as error:
        raise UnknownClassError(predicted_class) from error
