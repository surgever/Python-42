#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    tests = ["25", "abc"]
    print("=== Garden Temperature ===")
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
