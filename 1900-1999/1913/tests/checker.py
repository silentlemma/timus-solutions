"""Check two finite relay positions using only permitted directed transmissions."""

import math
from pathlib import Path
import sys

SUCCESS = ["Now", "we", "have", "enough", "power"]
TERMINALS = 3
RELAYS = 2
LOCAL_TOLERANCE = 1e-7


def check(input_text, expected_text, output_text):
    tokens = output_text.split()
    if tokens == ["Death"]:
        return None if expected_text.split() == ["Death"] else "a placement exists"
    if len(tokens) != len(SUCCESS) + 2 * RELAYS or tokens[: len(SUCCESS)] != SUCCESS:
        return "expected Death or the success phrase and two coordinate pairs"
    try:
        coordinates = list(map(float, tokens[len(SUCCESS) :]))
    except ValueError:
        return "invalid coordinate"
    if not all(math.isfinite(value) for value in coordinates):
        return "non-finite coordinate"
    values = list(map(int, input_text.split()))
    radius = values[0]
    points = list(zip(values[1::2], values[2::2]))
    points.extend(zip(coordinates[::2], coordinates[1::2]))
    edges = [[] for _ in points]
    relay_indices = range(TERMINALS, TERMINALS + RELAYS)

    def near(first, second):
        return math.dist(points[first], points[second]) <= radius + LOCAL_TOLERANCE

    for source in range(1, TERMINALS):
        edges[source] = [relay for relay in relay_indices if near(source, relay)]
    for relay in relay_indices:
        edges[relay] = [
            target
            for target in [0, *relay_indices]
            if target != relay and near(relay, target)
        ]
    for source in range(1, TERMINALS):
        seen = {source}
        stack = [source]
        while stack:
            for target in edges[stack.pop()]:
                if target not in seen:
                    seen.add(target)
                    stack.append(target)
        if 0 not in seen:
            return "a source cannot reach the receiver through the two relays"
    if expected_text.split() == ["Death"]:
        return "a witness contradicts the stored impossibility answer"
    return None


def main():
    input_path, expected_path, output_path = map(Path, sys.argv[1:])
    error = check(
        input_path.read_text(), expected_path.read_text(), output_path.read_text()
    )
    if error is not None:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
