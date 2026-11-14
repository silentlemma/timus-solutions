from array import array
import sys


MASKS = {b"A": 1, b"B": 2, b"P": 4, b"AB": 3, b"AP": 5, b"BP": 6, b"ABP": 7}
MASK_COUNT = 8
UNREACHED = 3 * MASK_COUNT
OUTPUT_CHUNK = 512


def optimal_order(kinds):
    present = sum(1 << kind for kind in kinds)
    costs = bytearray([UNREACHED]) * ((present + 1) * MASK_COUNT)
    previous = bytearray(len(costs))
    for kind in kinds:
        costs[(1 << kind) * MASK_COUNT + kind] = kind.bit_count()
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
                new_cost = cost + (kind & ~last).bit_count()
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
