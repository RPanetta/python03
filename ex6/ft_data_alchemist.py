#!/usr/bin/env python3

import random


def data_alchemist(players: list[str]) -> None:
    print(f"Initial list of players: {players}")

    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized: list[str] = [name
                                   for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    scores: dict[str, int] = {name: random.randint(1, 1000)
                              for name in all_capitalized}
    print(f"\nScore dict: {scores}")

    average: float = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high_scores: dict[str, int] = {name: score for name,
                                   score in scores.items() if score > average}
    print(f"High scores: {high_scores}")


def main() -> None:
    print("=== Game Data Alchemist ===")
    players: list[str] = [
        'Alice', 'bob', 'Charlie',
        'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']

    data_alchemist(players)


if __name__ == "__main__":
    main()
