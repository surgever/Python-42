#!/usr/bin/python3

def garden_operations(test: int) -> None:
    if (test == 0):
        int("abc")
    elif (test == 1):
        10/0
    elif (test == 2):
        open("missing.txt")
    elif (test == 3):
        "2" + 2  # type: ignore # ignore: [TypeError]
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    tests = [0, 1, 2, 3, 4]
    for error in tests:
        try:
            print(f"Testing operation {error}...")
            garden_operations(error)
        except ValueError as exc:
            print(f"Caught ValueError: {exc}")
        except ZeroDivisionError as exc:
            print(f"Caught ZeroDivisionError: {exc}")
        except FileNotFoundError as exc:
            print(f"Caught FileNotFoundError: No such file \'{exc.filename}\'")
        except TypeError as exc:
            print(f"Caught TypeError: {exc.args[0]}")
        else:
            print("Operation completed successfully")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
