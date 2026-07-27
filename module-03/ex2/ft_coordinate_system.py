#!/usr/bin/python3

import math


def get_player_pos() -> tuple[float, float, float]:
    enter_coord = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        coord = input(enter_coord).split(",")
        if len(coord) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(coord[0])
            y = float(coord[1])
            z = float(coord[2])
        except ValueError as e:
            for value in coord:
                try:
                    float(value)
                except ValueError:
                    print(f"Error on parameter '{value.strip()}': {e}")
                    break
            continue
        else:
            break
    return (x, y, z)


def ft_coordinate_system() -> None:
    print("\nGet a first set of coordinates")
    c1 = get_player_pos()
    print("Got a first tuple:", c1)
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    to_center = math.sqrt((c1[0])**2 + (c1[1])**2 + (c1[2])**2)
    print("Distance to center:", round(to_center, 4))
    print("\nGet a second set of coordinates")
    c2 = get_player_pos()
    print("Distance between the 2 sets of coordinates:", round(math.sqrt(
        (c2[0]-c1[0])**2 + (c2[1]-c1[1])**2 + (c2[2]-c1[2])**2), 4)
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()
