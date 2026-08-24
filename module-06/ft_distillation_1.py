#!/usr/bin/python3

import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.potions.strength_potion()}")
    print(f"Testing heal alias: {alchemy.heal()}")
