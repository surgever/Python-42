from typing import Any


class RawData:
    def __init__(self):
        # Lambda Sanctum Test Data
        self.artifacts = [
                {'name': 'Dragon Fury', 'power': 76, 'type': 'accessory'},
                {'name': 'Lightning Rod', 'power': 85, 'type': 'armor'},
                {'name': 'Fire Staff', 'power': 92, 'type': 'armor'},
                {'name': 'Earth Shield', 'power': 72, 'type': 'weapon'}
            ]
        self.mages = [
                {'name': 'Ash', 'power': 63, 'element': 'water'},
                {'name': 'Nova', 'power': 87, 'element': 'earth'},
                {'name': 'Alex', 'power': 55, 'element': 'wind'},
                {'name': 'Ember', 'power': 100, 'element': 'ice'},
                {'name': 'Luna', 'power': 57, 'element': 'fire'}
            ]
        self.spells = ['blizzard', 'tornado', 'earthquake', 'shield']


def artifact_sorter(artifacts: list[dict]) -> list[dict[str, Any]]:
    return list(sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} * ", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda x: x['power'], mages))
    return {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    data = RawData()

    print("\nTesting artifact sorter...")
    artifact = artifact_sorter(data.artifacts)
    print(
        f"* {artifact[0]['name']} ({artifact[0]['power']} power) comes before "
        + f"{artifact[1]['name']} ({artifact[1]['power']} power)"
    )

    print("\nTesting mages filter...")
    for mage in power_filter(data.mages, 60):
        print(f"* {mage['name']} ({mage['power']} power)")

    print("\nTesting spell transformer...")
    for spell in spell_transformer(data.spells):
        print(spell, end="")

    print("\n\nTesting mage stats...")
    stats = mage_stats(data.mages)
    print(f"* Max power: {stats['max_power']}")
    print(f"* Min power: {stats['min_power']}")
    print(f"* Average power: {stats['avg_power']:.2f}")
