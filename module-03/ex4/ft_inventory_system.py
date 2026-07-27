#!/usr/bin/env python3

import sys


class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv = {}
    argc = len(sys.argv)
    if argc == 1:
        print(bcolors.WARNING +
              "Error - Please provide inventory parameters." + bcolors.ENDC)
        print("Usage: python3 ft_inventory_system.py item_a:3 item_b:12")
        return

    for arg in sys.argv[1:]:
        colon_pos = -1
        for i in range(len(arg)):
            if arg[i] == ':':
                colon_pos = i
                break
        if colon_pos == -1 or colon_pos == len(arg) - 1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = arg[:colon_pos]
        value_str = arg[colon_pos + 1:]
        if key == "":
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key in inv:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            quantity = int(value_str)
        except ValueError as e:
            print(f"Quantity error for '{key}': ", e)
            continue
        if quantity < 0:
            print(f"Negative quantity error for '{key}': {quantity}")
            continue
        inv.update({key: quantity})

    print("Got inventory:", inv)
    print("Item list:", list(inv.keys()))
    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")

    if len(inv) > 0 and total > 0:
        most, least = "", ""
        for key in inv:
            percentage = round(inv[key] * 100 / total, 1)
            print(f"Item {key} represents {percentage}%")
            if most == "" or inv[key] > inv[most]:
                most = key
            if least == "" or inv[key] < inv[least]:
                least = key
        print(f"Item most abundant: {most} with quantity {inv[most]}")
        print(f"Item least abundant: {least} with quantity {inv[least]}")
    inv.update({"magic_item": 1})
    print("Updated inventory:", inv)


if __name__ == "__main__":
    main()
