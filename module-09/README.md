_This project has been created as part of the 42 curriculum by seoliver._

# Module 09 🚀 Discover Pydantic Models & Validation

**Master Pydantic data validation to create robust models, implement custom validation and handle nested structures.**

Here you will learn how to validate data with Pydantic models and enforce rules through schema definitions. This module covers BaseModel, Field constraints, enums, and custom validation patterns for safe and structured application data.

## Module contents

| Exercises | Contents |
| ---------- |--------- |
| [ex0](ex0/space_station.py), [ex1](ex1/alien_contact.py), [ex2](ex2/space_crew.py) | Pydantic, BaseModel, Field, validation rules

## Learn:
* [Pydantic Validation Documentation](https://pydantic.dev/docs/validation/latest/get-started/)

## Notes
- Have you explored Pydantic at depth and understood why it saves some much time when parsing? 

## Code example
```python
from pydantic import BaseModel, Field

class SpaceMission(BaseModel):
    mission_name: str = Field(..., min_length=3, max_length=100)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
```
