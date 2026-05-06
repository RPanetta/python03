#!/usr/bin/env python3

import sys


def command_quest(args: list[str]) -> None:
    n = len(sys.argv)
    print("=== Command Quest ===")
    print("Program name:", args[0])

    if n == 1:
        print("No arguments provided!")
    else:
        print("Arguments received:", n - 1)

    for i in range(1, n):
        print(f"Argument {i}: ", args[i])
    print("Total arguments:", n)


def main() -> None:
    command_quest(sys.argv)


if __name__ == "__main__":
    main()
