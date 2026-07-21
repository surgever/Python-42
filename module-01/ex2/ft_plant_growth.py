#!/usr/bin/python3

class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0
        self.days: int = 0
        self.growth_rate: float = 2.5

    def show(self) -> str:
        return f'{self.name}: {self.height:.1f} cm, {self.days} days old'

    def grow(self, days_added: int) -> None:
        self.height += days_added * self.growth_rate

    def age(self, days_added: int) -> None:
        self.days += days_added


def ft_plant_growth() -> None:
    days_passed = 0
    plant1 = Plant()
    plant1.name = "Rose"
    plant1.height = 25
    plant1.days = 30
    plant1.growth_rate = 0.8
    start_height = plant1.height
    print(plant1.show())

    while (days_passed < 7):
        days_passed += 1
        print(f"=== Day {days_passed} ===")
        plant1.age(1)
        plant1.grow(1)
        print(plant1.show())

    print('Growth this week:')
    growth = plant1.height - start_height
    print(f"{plant1.name}: {growth:.1f} cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
