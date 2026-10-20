"""Boxes from a seed: mode 1 a few small random boxes, mode 2 the maximum
size cut from one sorted row and shuffled, mode 3 the same with two
neighbouring sizes swapped, mode 4 the maximum size with many equal
sizes."""

import random
import sys

MAX_N = 100
MAX_K = 100
MAX_A = 10 ** 4
SMALL_N = 6
SMALL_K = 3
SMALL_A = 6


def cut(row, lengths, rng):
    boxes = []
    start = 0
    for length in lengths:
        boxes.append(row[start:start + length])
        start += length
    rng.shuffle(boxes)
    return boxes


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        boxes = []
        for _ in range(n):
            box = [rng.randint(1, SMALL_A) for _ in range(rng.randint(1, SMALL_K))]
            if rng.randint(0, 1):
                box.sort()
            boxes.append(box)
    else:
        n = MAX_N
        top = SMALL_A if mode == 4 else MAX_A
        lengths = [rng.randint(1, MAX_K) for _ in range(n)]
        row = sorted(rng.randint(1, top) for _ in range(sum(lengths)))
        boxes = cut(row, lengths, rng)
        if mode == 3:
            candidates = [b for b in boxes if len(b) > 1 and b[0] < b[-1]]
            box = rng.choice(candidates)
            i = next(j for j in range(len(box) - 1) if box[j] < box[j + 1])
            box[i], box[i + 1] = box[i + 1], box[i]
    lines = [str(len(boxes))]
    lines += [" ".join(map(str, [len(b)] + b)) for b in boxes]
    print("\n".join(lines))


main()
