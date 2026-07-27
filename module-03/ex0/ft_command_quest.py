#!/usr/bin/python3

import sys


def main() -> None:
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        i = 1
        argc = len(sys.argv)
        print(f"Arguments: {len(sys.argv) - 1}")
        while i < argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
