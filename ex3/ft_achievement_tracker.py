#!/usr/bin/env python3

import random

achievement: list[str] = [
    'Crafting Genius', 'Strategist', 'World Savior',
    'Speed Runner', 'Survivor', 'Master Explorer',
    'Treasure Hunter', 'Unstoppable', 'First Steps',
    'Collector Supreme', 'Untouchable', 'Sharp Mind',
    'Boss Slayer'
        ]


def gen_player_achievements() -> set[str]:
    n: int = random.randint(5, 10)
    selection: list[str] = random.sample(achievement, n)
    return set(selection)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
        }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_achievements}")

    common: set[str] = set().intersection(*players.values())
    print(f"\nCommon achievements: {common}")

    print()
    for name, achievements in players.items():
        others = [p for n, p in players.items() if n != name]
        union = set().union(*others)
        only = achievements.difference(union)
        print(f"Only {name} has: {only}")

    print()
    for name, achievements in players.items():
        missing: set[str] = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
