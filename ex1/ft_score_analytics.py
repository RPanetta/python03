#!/usr/bin/env python3

import sys


def main() -> None:
    args = sys.argv[1:]
    scores = []
    print("=== Player Score Analytics ===")
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print("No scores provided. "
              f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
        return

    total = sum(scores)
    average = total / len(scores)
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
