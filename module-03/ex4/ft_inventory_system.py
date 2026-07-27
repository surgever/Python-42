#!/usr/bin/env python3

import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def ft_inventory_system() -> None:
    inv = {}
    argc = len(sys.argv)
    if argc == 1:
        print("Error - provide inventory parameters")
        print(bcolors.OKGREEN + "Warning: empty. Continue?" + bcolors.ENDC)
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
    if len(inv) > 0:
        if total > 0:
            for key in inv:
                percentage = round(inv[key] * 100 / total, 1)
                print(f"Item {key} represents {percentage}%")
        most_abundant = ""
        least_abundant = ""
        for key in inv:
            if most_abundant == "" or inv[key] > inv[most_abundant]:
                most_abundant = key
            if least_abundant == "" or inv[key] < inv[least_abundant]:
                least_abundant = key
        print(f"Item most abundant: {most_abundant}"
              f" with quantity {inv[most_abundant]}")
        print(f"Item least abundant: {least_abundant}"
              f" with quantity {inv[least_abundant]}")
    inv.update({"magic_item": 1})
    print("Updated inventory:", inv)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
