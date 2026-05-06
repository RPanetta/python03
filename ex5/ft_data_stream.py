#!/usr/bin/env python3

from typing import Generator
import random


def gen_event(
    players: list[str],
    actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield name, action


def consume_event(
    new_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(new_list) > 0:
        new_tuple: tuple[str, str] = random.choice(new_list)
        new_list.remove(new_tuple)
        yield new_tuple


def main() -> None:
    print("=== Game Data Stream Processor ===")
    players: list[str] = ['bob', 'alice', 'dylan', 'charlie']
    actions: list[str] = ['run', 'eat', 'sleep', 'grab', 'move', 'climb',
                          'swim', 'release']

    tuple_generator: Generator[
        tuple[str, str], None, None] = gen_event(players, actions)

    for i in range(0, 1000):
        name, action = next(tuple_generator)
        print(f"Event {i}: Player {name} did action {action}")

    new_list: list[tuple[str, str]] = []
    for _ in range(10):
        new_tuple: tuple[str, str] = next(tuple_generator)
        new_list.append(new_tuple)

    print(f"Built list of 10 events: {new_list}")

    for event in consume_event(new_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {new_list}")


if __name__ == "__main__":
    main()
