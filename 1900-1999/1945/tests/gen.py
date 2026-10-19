"""Deterministic 50000-visitor inputs; both inputs and answers exceed stored-file limits."""

import argparse
import sys

MAX_VISITORS = 50000
MAX_ARMS = 1000000000
MANY_TWOS_FACTOR = 16384


def values(mode):
    if mode == "prefix":
        return list(range(1, MAX_VISITORS + 1))
    if mode == "near_limit":
        return list(range(MAX_ARMS - MAX_VISITORS + 1, MAX_ARMS + 1))
    if mode == "many_twos":
        return [MANY_TWOS_FACTOR * index for index in range(1, MAX_VISITORS + 1)]
    return list(range(MAX_VISITORS, 0, -1))


def generate(mode, groups):
    data = values(mode)
    return f"{len(data)} {groups}\n" + "\n".join(map(str, data)) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode", choices=["prefix", "near_limit", "many_twos", "reverse"]
    )
    parser.add_argument("groups", type=int, choices=range(2, 6))
    args = parser.parse_args()
    sys.stdout.write(generate(args.mode, args.groups))
