"""Deterministic maximal coordinate families with exact geometric answers."""

import argparse
import sys

MAX_POINTS = 50000
SCALE = 1000


def points(mode):
    if mode == "integer":
        return [(100000, -100000)] * MAX_POINTS
    if mode == "corner":
        return [(-99500, 99500)] * MAX_POINTS
    if mode == "negative":
        return [(-1, -99999)] * MAX_POINTS
    if mode == "unique":
        return [(index // SCALE, index % SCALE) for index in range(MAX_POINTS)]
    if mode == "unique_far":
        return [
            (SCALE // 2 + index // SCALE, index % SCALE) for index in range(MAX_POINTS)
        ]
    if mode == "priority":
        return [(0, 0)] * 24999 + [(500, 500)] * 25000 + [(-1, 1)]
    if mode == "tie":
        return [(-1, -1)] * 25000 + [(499, 499)] * 25000
    return [(index % SCALE, index % SCALE) for index in range(MAX_POINTS)]


def decimal(value):
    return (
        ("-" if value < 0 else "")
        + str(abs(value) // SCALE)
        + f".{abs(value) % SCALE:03}"
    )


def generate(mode):
    data = points(mode)
    return (
        str(len(data))
        + "\n"
        + "".join(decimal(x) + " " + decimal(y) + "\n" for x, y in data)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=[
            "integer",
            "corner",
            "negative",
            "unique",
            "unique_far",
            "priority",
            "tie",
            "grid",
        ],
    )
    sys.stdout.write(generate(parser.parse_args().mode))
