_This project has been created as part of the 42 curriculum by seoliver._

# Module 05 🧬 Polymorphic Data Streams in the Digital Matrix

**Master abstract classes, method overriding and subtype polymorphism.**

Here you will learn how to design flexible data-processing systems using abstraction and polymorphism. This module introduces abstract base classes, stream processing, and pipeline patterns that let different data types be handled through a shared design.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/data_processor.py), [ex1](ex1/data_stream.py), [ex2](ex2/data_pipeline.py) | polymorphism, abstract classes, method overriding

## Learn:
* [Python Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp), by W3 schools
* [Abstract Classes in Python](https://www.geeksforgeeks.org/python/abstract-classes-in-python/), by GeeksforGeeks

## Notes
- Have you understood what is polimorphism and why it is so useful?

## Code example
```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
```