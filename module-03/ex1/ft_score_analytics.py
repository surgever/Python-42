#!/usr/bin/python3

import sys


def main() -> None:
    argc = len(sys.argv)
    scores = []
    if argc >= 1:
        i = 1
        while i < argc:
            try:
                new_score = int(sys.argv[i])
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            else:
                scores.append(new_score)
            finally:
                i += 1
    if len(scores) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> ...")
    else:
        print("Scores processed:", scores)
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / len(scores)):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
