#!/usr/bin/python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def main() -> None:
    print("=== Garden Temperature ===")
    tests = ["25", "abc"]
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
    main()
