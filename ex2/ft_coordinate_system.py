#!/usr/bin/env python3

import math


def get_player_pos():
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        coords = raw.split(',')
        if len(coords) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(coords[0])
        except ValueError as err:
            print(f"Error on parameter '{coords[0]}': {err}")
            continue

        try:
            y = float(coords[1])
        except ValueError as err:
            print(f"Error on parameter '{coords[1]}': {err}")
            continue

        try:
            z = float(coords[2])
            return (x, y, z)
        except ValueError as err:
            print(f"Error on parameter '{coords[2]}': {err}")
            continue


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    dist_ab = math.sqrt((pos2[0]-pos1[0])**2 +
                        (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_ab, 4)}")


if __name__ == "__main__":
    main()
