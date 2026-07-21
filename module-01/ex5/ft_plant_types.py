#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.update_height(height)
        self.update_age(age)

    def update_height(self, height: float) -> int:
        if height < 0:
            return 0
        else:
            self._height = height
            return 1

    def update_age(self, age: int) -> int:
        if age < 0:
            return 0
        else:
            self._age = age
            return 1

    def set_height(self, height: int) -> None:
        if self.update_height(height):
            print(f'Height updated: {height} cm')
        else:
            print(f'{self.name}: Error, height can\'t be negative')
            print('Height update rejected')

    def set_age(self, age: int) -> None:
        if self.update_age(age):
            print(f'Age updated: {age} days')
        else:
            print(f'{self.name}: Error, age can\'t be negative')
            print('Age update rejected')

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f'{self.name}: '
              f'{self.get_height():.1f} cm, {self.get_age()} days old')


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        super().show()
        print(f'Color: {self.get_color()}')
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name}, has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of '
              f'{self.get_trunk_diameter() * 40:.1f} cm long '
              f'and {self.get_trunk_diameter():.1f} cm wide.')

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        super().show()
        print(f'Trunk diameter: {self.get_trunk_diameter():.1f} cm')


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = season
        self._nut_value = 0

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nut_value(self) -> int:
        return self._nut_value

    def grow(self, days: int) -> None:
        print(f"[make {self.name.lower()} grow and age for {days} days]")
        self.update_height(self._height + (days * 2.10))
        self.update_age(self._age + days)
        self._nut_value = int(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.get_harvest_season()}")
        print(f"Nutritional value: {self.get_nut_value()}")


def ft_plant_types() -> None:
    print("=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    print('[asking the rose to bloom]')
    flower.bloom()
    flower.show()
    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    print('[asking the oak to produce shade]')
    tree.produce_shade()
    print("\n=== Vegetables")
    vegetable = Vegetable("Tomato", 5, 10, "April")
    vegetable.show()
    vegetable.grow(20)
    vegetable.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
