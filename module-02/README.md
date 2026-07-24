_This project has been created as part of the 42 curriculum by seoliver._

# Module 02 💦 Data Engineering for Smart Agriculture

**Master error handling.**

Here you will learn how to handle errors and build resilient Python programs. This module focuses on exceptions, custom error classes, and cleanup patterns that keep applications stable even when unexpected input or failures occur.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/ft_first_exception.py), [ex1](ex1/ft_raise_exception.py), [ex2](ex2/ft_different_errors.py) | errors, try/except, raise
| [ex3](ex3/ft_custom_errors.py), [ex4](ex4/ft_finally_block.py) | custom error classes, finally cleanup

<img src="https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/try_except.png" alt="Block: try/except/else/finally."/>

## Learn:
* [Python Errors](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/15_Day_Python_type_errors/15_python_type_errors.md)
* [Exception Handling](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/17_Day_Exception_handling/17_exception_handling.md)

## Notes
- Have you provided a default message for your custom error classes?

## Code example
```python
    try:
        for plant in plant_list:
            water_plant(plant)
    except PlantError as exc:
        print(f"Caught PlantError: {exc}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
```
