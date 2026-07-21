#!/usr/bin/python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._stats = Plant.PlantStats()
        self.update_height(height)
        if age < 0:
            self._age = 0
        else:
            self._age = age

    class PlantStats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def display(self) -> str:
            return (f"Stats: {self._grow_calls} grow, "
                    f"{self._age_calls} age, {self._show_calls} show")

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
            self._stats.increment_age()
            return 1

    def set_height(self, height: int) -> None:
        if self.update_height(height):
            print(f'Height updated: {height} cm')
        else:
            print(f"{self.name}: Error, height can't be negative")
            print('Height update rejected')

    def set_age(self, age: int) -> None:
        if self.update_age(age):
            print(f'Age updated: {age} days')
        else:
            print(f"{self.name}: Error, age can't be negative")
            print('Age update rejected')

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self.name}: "
              f"{self.get_height():.1f} cm, {self.get_age()} days old")

    def get_stats(self) -> str:
        return self._stats.display()

    @staticmethod
    def check_is_year_age(age: int) -> bool:
        return age >= 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def grow(self) -> None:
        self._stats.increment_grow()
        self.update_height(self._height + 8.0)
        self.bloom()

    def get_color(self) -> str:
        return self._color

    def show(self) -> None:
        self._stats.increment_show()
        print(f'{self.name}: '
              f'{self.get_height():.1f} cm, {self.get_age()} days old')
        print(f'Color: {self.get_color()}')
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0

    def grow(self) -> None:
        self._stats.increment_grow()
        self.update_height(self._height + 30.0)
        self.update_age(self._age + 20)
        self.bloom()
        self._seeds = 42

    def show(self) -> None:
        self._stats.increment_show()
        print(f'{self.name}: '
              f'{self.get_height():.1f} cm, {self.get_age()} days old')
        print(f'Color: {self.get_color()}')
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk
        self._tree_stats = Tree.TreeStats()

    class TreeStats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0
            self._shade_calls = 0

        def increment_grow(self) -> None:
            self._grow_calls += 1

        def increment_age(self) -> None:
            self._age_calls += 1

        def increment_show(self) -> None:
            self._show_calls += 1

        def increment_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> str:
            return (f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                    f"{self._show_calls} show\n{self._shade_calls} shade")

    def produce_shade(self) -> None:
        print(f'Tree {self.name} now produces a shade of '
              f'{self.get_trunk_diameter() * 40:.1f} cm long '
              f'and {self.get_trunk_diameter():.1f} cm wide.')
        self._tree_stats.increment_shade()

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def show(self) -> None:
        self._tree_stats.increment_show()
        print(f'{self.name}: '
              f'{self.get_height():.1f} cm, {self.get_age()} days old')
        print(f'Trunk diameter: {self.get_trunk_diameter():.1f} cm')

    def get_stats(self) -> str:
        return self._tree_stats.display()


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
        self._stats.increment_grow()
        self.update_height(self._height + (days * 2.10))
        self.update_age(self._age + days)
        self._nut_value = int(days)

    def show(self) -> None:
        self._stats.increment_show()
        print(f'{self.name}: '
              f'{self.get_height():.1f} cm, {self.get_age()} days old')
        print(f"Harvest season: {self.get_harvest_season()}")
        print(f"Nutritional value: {self._nut_value}")


def ft_display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(plant.get_stats())


def ft_garden_analytics() -> None:
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_is_year_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_is_year_age(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    ft_display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.show()
    ft_display_plant_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    ft_display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    ft_display_plant_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.show()
    ft_display_plant_statistics(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    ft_display_plant_statistics(anonymous)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_garden_analytics()
