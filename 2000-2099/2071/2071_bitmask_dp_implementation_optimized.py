import os
from array import array
import sys


MASKS = {b"A": 1, b"B": 2, b"P": 4, b"AB": 3, b"AP": 5, b"BP": 6, b"ABP": 7}
MASK_COUNT = 8
UNREACHED = 3 * MASK_COUNT
OUTPUT_CHUNK = 512


def optimal_order(kinds):
    present = sum(1 << kind for kind in kinds)
    counts = tuple(value.bit_count() for value in range(MASK_COUNT))
    costs = [UNREACHED] * ((present + 1) * MASK_COUNT)
    previous = [0] * len(costs)
    for kind in kinds:
        costs[(1 << kind) * MASK_COUNT + kind] = counts[kind]
    for used in range(1, present):
        for last in kinds:
            cost = costs[used * MASK_COUNT + last]
            if cost == UNREACHED:
                continue
            for kind in kinds:
                bit = 1 << kind
                if used & bit:
                    continue
                index = (used | bit) * MASK_COUNT + kind
                new_cost = cost + counts[kind & ~last]
                if new_cost < costs[index]:
                    costs[index] = new_cost
                    previous[index] = last
    last = min(kinds, key=lambda kind: costs[present * MASK_COUNT + kind])
    answer = costs[present * MASK_COUNT + last]
    order = []
    while last:
        order.append(last)
        present, last = present ^ (1 << last), previous[present * MASK_COUNT + last]
    return answer, reversed(order)


def main():
    source = sys.stdin.buffer
    count = int(source.readline())
    # Read one order at a time and keep only packed glass indices.
    glasses = [array("I") for _ in range(MASK_COUNT)]
    for index in range(1, count + 1):
        glasses[MASKS[source.readline().strip()]].append(index)
    answer, order = optimal_order([kind for kind, indices in enumerate(glasses) if indices])

    write = sys.stdout.write
    write(f"{answer}\n")
    separator = ""
    for kind in order:
        indices = glasses[kind]
        # Bound temporary strings while still joining and writing in batches.
        for start in range(0, len(indices), OUTPUT_CHUNK):
            write(separator + " ".join(map(str, indices[start : start + OUTPUT_CHUNK])))
            separator = " "
    write("\n")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
