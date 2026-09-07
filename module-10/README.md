_This project has been created as part of the 42 curriculum by seoliver._

# Module 10 🪄 Master the Ancient Arts of Functional Programming

**Master lambda and higher-order functions, scopes, functools library and decorators.**


Here you will learn how functional programming techniques can make your code more expressive and reusable. This module explores lambda functions, higher-order functions, closures, functools utilities, and decorators for writing elegant Python programs.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/lambda_spells.py) | lambda functions
| [ex1](ex1/higher_magic.py) | higher-order functions
| [ex2](ex2/scope_mysteries.py) | lexical scope, closures, nested functions, mutable state retention
| [ex3](ex3/functools_artifacts.py) | functools: reduce, partial, lru_cache, singledispatch
| [ex4](ex4/decorator_mastery.py) | decorator, decorator factories, functools.wraps

## Learn:
* [Higher Order Functions](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/14_Day_Higher_order_functions/14_higher_order_functions.md), by Asabeneh
* [*args and **kwargs ](https://www.geeksforgeeks.org/python/args-kwargs-python/), by GeeksforGeeks
* [First Class functions in Python](https://www.geeksforgeeks.org/python/first-class-functions-python/)
* [Lambda Functions](https://www.geeksforgeeks.org/python/python-lambda-anonymous-functions-filter-map-reduce/)
* [reduce() ](https://www.geeksforgeeks.org/python/reduce-in-python/)
* [Inner Functions](https://www.geeksforgeeks.org/python/python-inner-functions/)
* [Decorators](https://www.geeksforgeeks.org/python/decorators-in-python/)

## Notes
- Have you included and are you using add and mul from the operator module?

## Code example

```python
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print("Casting", func.__name__)
        output = func(*args, **kwargs)
        return output
    return wrapper


@spell_timer
def foo(amount: int) -> str:
    pass
```
