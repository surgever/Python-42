#!/usr/bin/env python3

import random


def ft_data_alchemist() -> None:
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"\nInitial list of players: {players}")
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")
    scores = {
        name: random.randint(0, 1000)
        for name in all_capitalized
    }
    print(f"\nScore dict: {scores}")
    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")
    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    ft_data_alchemist()
