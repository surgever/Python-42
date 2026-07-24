#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, msg: str = "Unknown Garden Error") -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = "Unknown Plant Error") -> None:
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    plant_list_ok = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plant_list_ok)
    print("\nTesting invalid plants...")
    plant_list_bad = ["Tomato", "lettuce", "carrots"]
    test_watering_system(plant_list_bad)
    print("\nCleanup always happens, even with errors!")
