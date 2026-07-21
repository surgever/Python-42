_This project has been created as part of the 42 curriculum by seoliver._

# Module 01 🌳 Object-Oriented Garden Systems

**Master classes, attributes and methods.**

Here you will learn how to design and organize code with classes, objects, and methods. This module introduces the foundations of object-oriented programming, including attributes, encapsulation, and inheritance patterns used to model garden systems effectively.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/ft_garden_intro.py), [ex1](ex1/ft_garden_data.py), [ex2](ex2/ft_plant_growth.py), [ex3](ex3/ft_plant_factory.py), [ex4](ex4/ft_garden_security.py) | classes, methods, attributes
| [ex5](ex5/ft_plant_types.py), [ex6](ex6/ft_garden_analytics.py) | inheritance, @staticmethod, @classmethod

## Learn:
* [Classes and Objects](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md), 30 days of Python by Asabeneh
* [Class method vs Static method](https://www.geeksforgeeks.org/python/class-method-vs-static-method-python/), by GeeksforGeeks

## Notes
- Have you learn the differences between instance method, static method and class method?

## Code example
```python
class Plant:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def show(self) -> str:
        return f"Name: {self.name}"


my_plant = Plant("Rose")
print(my_plant.show())
```