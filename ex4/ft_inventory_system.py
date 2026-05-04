#!/usr/bin/env python3

import sys


def parse_args(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for argument in args:
        if ":" not in argument:
            print(f"Error - invalid parameter {argument}")
            continue
        key, val_str = argument.split(":", 1)

        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        try:
            inventory[key] = int(val_str)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")

    return inventory


def display_analysis(inventory: dict[str, int]) -> None:
    if not inventory:
        return
    items: list[str] = list(inventory.keys())
    total_qty: int = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant: str = items[0]
    least_abundant: str = items[0]

    for item in inventory:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant}"
          f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant}"
          f"with quantity {inventory[least_abundant]}")


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = parse_args(sys.argv[1:])

    if not inventory:
        print("At the beginning of the game,"
              "your inventory is usually empty ;)")
        return

    display_analysis(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
