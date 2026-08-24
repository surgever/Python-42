_This project has been created as part of the 42 curriculum by seoliver._

# Module 06 ⚗️ Mastering Python’s Import Mysteries

**Master package initialization, import pathways, absolute versus relative access and breaking circular dependencies.**

Here you will learn how Python imports work across modules and packages. This module explores import paths, relative and absolute imports, package structure, and the confusing cases where modules fail to load or behave differently than expected.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [alemb_0](ft_alembic_0.py), [1](ft_alembic_1.py), [2](ft_alembic_2.py), [3](ft_alembic_3.py), [4](ft_alembic_4.py), [5](ft_alembic_5.py) | import mechanics and package access
| [dist_0](ft_distillation_0.py), [1](ft_distillation_1.py), [transm_0](ft_transmutation_0.py), [1](ft_transmutation_1.py), [2](ft_transmutation_2.py) | package imports, module aliasing, import structure
| [kab_0](ft_kaboom_0.py), [1](ft_kaboom_1.py) | circular dependencies and import failures

## Learn:
* [Modules](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md)

## Notes
- Have you learn the several ways to avoid crashing because of circular dependencies?

## Code example

`alchemy/__init__.py`:
```python
from .elements import create_air

__all__ = ["create_air"]
```
`main.py`:
```python
from alchemy import create_air

if __name__ == "__main__":
    print(f"Testing create_air: {create_air()}")
```