_This project has been created as part of the 42 curriculum by seoliver._

# Module 03 🎮 Mastering Python Collections

**Master Python’s data structures and processing data.**

Here you will learn how to work with Python collections and command-line data. This module introduces argument parsing, validation, and practical use of lists, sets, dictionaries, and generators for transforming and analyzing information.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/ft_command_quest.py) | arguments, data parsing
| [ex1](ex1/ft_score_analytics.py), [ex2](ex2/ft_coordinate_system.py), [ex3](ex3/ft_achievement_tracker.py), [ex4](ex4/ft_inventory_system.py) | list, tuple, set, dict
| [ex5](ex5/ft_data_stream.py) | generator, yield
| [ex6](ex6/ft_data_alchemist.py) | comprehensions

## Learn:
* [Lists](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_lists.md)
* [Tuples](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/06_Day_Tuples/06_tuples.md)
* [Sets](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/07_Day_Sets/07_sets.md)
* [Dictionaries](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/08_Day_Dictionaries/08_dictionaries.md)
* [List Comprehension](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md)
* [yield Keyword](https://www.geeksforgeeks.org/python/python-yield-keyword/), by GeeksforGeeks

## Notes
- Have you check all possible validation errors, such as receiving no arguments?
- Have you protected the program from crashing when interrupted by the user keyboard?

## Code example
```python
    print(f"Initial list of players: {players_list}")
    all_capitalized_list = [name.capitalize() for name in players_list]
    print(f"New list with all names capitalized: {all_capitalized_list}")
```