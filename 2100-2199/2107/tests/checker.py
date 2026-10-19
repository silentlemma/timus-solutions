"""Validate a completion and independently decide whether a negative answer is possible."""

import math
import sys
from functools import lru_cache
from pathlib import Path

ARGUMENT_COUNT = 3


class Bad(Exception):
    pass


def completion_count(n, k, partial):
    """Count completions, stopping at two, by grouping labelled open paths into cycles."""
    incoming = [0] * n
    for target in partial:
        if target:
            incoming[target - 1] += 1
            if incoming[target - 1] > 1:
                return 0

    seen = [False] * n
    lengths = []
    for start in range(n):
        if incoming[start]:
            continue
        current = start
        length = 0
        while current >= 0:
            seen[current] = True
            length += 1
            current = partial[current] - 1
        lengths.append(length)

    for start in range(n):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = partial[current] - 1
        if k % length:
            return 0

    sizes = tuple(sorted(set(lengths)))
    initial = tuple(lengths.count(size) for size in sizes)
    allowed = [length for length in range(1, n + 1) if k % length == 0]

    @lru_cache(None)
    def count(state):
        if not any(state):
            return 1
        anchor = len(state) - 1
        while state[anchor] == 0:
            anchor -= 1
        available = list(state)
        available[anchor] -= 1
        remaining_counts = available.copy()
        total = 0

        def groups(index, remaining, chosen, ways):
            if remaining == 0:
                yield tuple(remaining_counts), 2 if chosen >= 2 else ways
                return
            if index < 0:
                return
            size = sizes[index]
            maximum = min(available[index], remaining // size)
            for amount in range(maximum + 1):
                remaining_counts[index] = available[index] - amount
                choices = math.comb(available[index], amount)
                weight = min(2, ways * choices)
                yield from groups(index - 1, remaining - amount * size, chosen + amount, weight)
            remaining_counts[index] = available[index]

        # Anchor one labelled path, so each cycle partition is counted once.
        for length in allowed:
            if length < sizes[anchor]:
                continue
            for remaining, ways in groups(anchor, length - sizes[anchor], 0, 1):
                total += ways * count(remaining)
                if total >= 2:
                    return 2
        return total

    return count(initial)


def check(source, expected, output):
    data = [int(token) for token in Path(source).read_text(encoding="utf-8").split()]
    n, k = data[:2]
    partial = data[2:]
    got = Path(output).read_text(encoding="utf-8").split()
    if not got:
        raise Bad("missing Yes or No")
    if got[0] == "No":
        if len(got) != 1:
            raise Bad("unexpected values after No")
        if completion_count(n, k, partial):
            raise Bad("a valid completion exists")
        return
    if got[0] != "Yes" or len(got) != n + 1:
        raise Bad("expected Yes and exactly n values, or No")
    try:
        answer = [int(token) for token in got[1:]]
    except ValueError:
        raise Bad("the completion must contain integers") from None
    if sorted(answer) != list(range(1, n + 1)):
        raise Bad("the completion is not a permutation")
    if any(fixed and fixed != target for fixed, target in zip(partial, answer)):
        raise Bad("a specified value was changed")
    seen = [False] * n
    for start in range(n):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = answer[current] - 1
        if k % length:
            raise Bad("a cycle length does not divide k")


def main():
    try:
        check(*sys.argv[1 : ARGUMENT_COUNT + 1])
    except (Bad, ValueError, OSError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
