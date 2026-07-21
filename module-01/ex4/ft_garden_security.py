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

    def show(self) -> str:
        return (f'{self.name}: '
                f'{self.get_height()} cm, {self.get_age()} days old')


def ft_garden_security() -> None:
    plant = Plant("Rose", 15, 10)
    print(f'Plant created: {plant.show()}\n')
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-25)
    plant.set_age(-30)
    print(f'\nCurrent state: {plant.show()}\n')


if __name__ == "__main__":
    print('=== Garden Security System ===')
    ft_garden_security()
