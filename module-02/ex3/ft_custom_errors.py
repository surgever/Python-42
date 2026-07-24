#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error") -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = "Unknown Garden Error") -> None:
        super().__init__(msg)


def plant_error(plant_name: str, health: int) -> None:
    if health < 3:
        raise PlantError(f"The {plant_name.lower()} plant is wilting!")


def water_error(water_amount: int) -> None:
    if water_amount < 5:
        raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        plant_error("tomato", 1)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_error(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_error("Tomato", 2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_error(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise GardenError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
