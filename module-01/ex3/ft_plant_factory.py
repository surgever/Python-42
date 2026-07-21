#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = 2.5

    def show(self) -> str:
        return f'{self.name}: {self.height} cm, {self.days} days old'

    def grow(self, days_added: int) -> None:
        self.height += (days_added * 2.5)

    def age(self, days: int) -> None:
        days_added = int(days)
        self.days += days_added
        self.grow(days_added)


def ft_plant_factory() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    for plant in plants:
        print(f'Created: {plant.show()}')


if __name__ == "__main__":
    print('=== Plant Factory Output ===')
    ft_plant_factory()
