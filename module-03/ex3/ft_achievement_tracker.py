#!/usr/bin/env python3

import random


def gen_player_achievements(achi: list[str]) -> set[str]:
    count = random.randint(2, len(achi) - 1)
    return set(random.sample(achi, count))


def ft_achievement_tracker() -> None:
    achi = ['Crafting Genius', 'Strategist', 'World Savior',
            'Speed Runner', 'Survivor', 'Master Explorer',
            'Treasure Hunter', 'Unstoppable', 'First Steps',
            'Collector Supreme', 'Untouchable',
            'Sharp Mind', 'Boss Slayer']
    alice = gen_player_achievements(achi)
    bob = gen_player_achievements(achi)
    charlie = gen_player_achievements(achi)
    dylan = gen_player_achievements(achi)

    print("\nPlayer Alice::", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    all_distinct = alice.union(bob, charlie, dylan)
    print("\nAll distinct achievements:", all_distinct)
    print("\nCommon achievements:", alice.intersection(bob, charlie, dylan))

    print("\nOnly Alice has:", alice.difference(bob, charlie, dylan))
    print("Only Bob has:", bob.difference(alice, charlie, dylan))
    print("Only Charlie has:", charlie.difference(alice, bob, dylan))
    print("Only Dylan has:", dylan.difference(alice, bob, charlie))

    print("\nAlice is missing:", all_distinct.difference(alice))
    print("Bob is missing:", all_distinct.difference(bob))
    print("Charlie is missing:", all_distinct.difference(charlie))
    print("Dylan is missing:", all_distinct.difference(dylan))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    ft_achievement_tracker()
