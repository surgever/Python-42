from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def test_station(station_data: Any) -> None:

    try:
        station = SpaceStation(**station_data)
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            print(error["msg"])
    else:
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            f"Status: "
            f"{'Operational' if station.is_operational else 'Non-operational'}"
        )
        print()


def main() -> None:
    print("Space Station Data Validation")

    stations_data = [
        {
            "station_id": "ISS001",
            "name": "International Space Station",
            "crew_size": 6,
            "power_level": 85.5,
            "oxygen_level": 92.3,
            "last_maintenance": datetime.now()
        },
        {
            "station_id": "DS-01",
            "name": "Deep Space Station",
            "crew_size": 30,
            "power_level": 100.0,
            "oxygen_level": 100.0,
            "last_maintenance": datetime.now(),
        }
    ]

    for data in stations_data:
        print(f"{'='*38}")
        test_station(data)


if __name__ == "__main__":
    main()
