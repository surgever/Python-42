#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError as exc:
        raise ValueError(f"{exc}")
    else:
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        else:
            return temp


def test_temperature() -> None:
    tests = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===")
    for t in tests:
        try:
            print(f"\nInput data is '{t}'")
            input_temperature(t)
        except ValueError as exc:
            print("Caught input_temperature error:", exc)
        else:
            print(f"Temperature is now {t}°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
