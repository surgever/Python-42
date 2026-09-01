from datetime import datetime
from enum import Enum
from typing import Any, List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(
            member.rank in (Rank.commander, Rank.captain)
            for member in self.crew
        )

        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                member.years_experience >= 5
                for member in self.crew
            )

            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    "crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def test_mission(mission_data: Any) -> None:

    try:
        mission = SpaceMission(**mission_data)
    except ValidationError as exc:
        print("Expected validation error:")
        for error in exc.errors():
            print(error["msg"])
    else:
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"| {member.specialization}"
            )
        print()


def main() -> None:
    print("Space Mission Crew Validation")

    commander = CrewMember(
        member_id="C001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=45,
        specialization="Mission Command",
        years_experience=15,
        is_active=True,
    )

    navigator = CrewMember(
        member_id="R002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=25,
        specialization="Navigation",
        years_experience=2,
        is_active=True,
    )

    officer = CrewMember(
        member_id="O003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=30,
        specialization="Engineering",
        years_experience=6,
        is_active=True,
    )

    missions_data = [
        {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": datetime.now(),
            "duration_days": 900,
            "crew": [commander, navigator, officer],
            "budget_millions": 2500.0,
        },
        {
            "mission_id": "M_FAIL_01",
            "mission_name": "Rookie Mistake",
            "destination": "Moon",
            "launch_date": datetime.now(),
            "duration_days": 30,
            "crew": [navigator, officer],
            "budget_millions": 50.0,
        }
    ]

    for data in missions_data:
        print(f"{'='*38}")
        test_mission(data)


if __name__ == "__main__":
    main()
