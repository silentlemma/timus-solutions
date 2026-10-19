"""Generate maximum bipartite graphs with an explicit matching certificate.

Modes: complete, complete_permuted, deficient_dense, half_block,
long_augment, long_augment_permuted, mixed, empty, triangular, deficient_chain.
All modes have 1000 vertices in each part. Vertex and input edge orders vary.
"""

import random
import sys

SIZE = 1000


def build(seed, mode):
    n = SIZE
    full = (1 << n) - 1
    if mode in ("complete", "complete_permuted"):
        rows, matching = [full] * n, list(range(n))
    elif mode == "deficient_dense":
        rows, matching = [(1 << (n - 1)) - 1] * n, list(range(n - 1)) + [-1]
    elif mode == "half_block":
        half = n // 2
        rows, matching = [(1 << half) - 1] * n, list(range(half)) + [-1] * half
    elif mode in ("long_augment", "long_augment_permuted"):
        rows = [(1 << u) | (1 << (u + 1)) for u in range(n - 1)] + [1]
        matching = list(range(1, n)) + [0]
    elif mode == "mixed":
        center = 399
        rows = [(1 << center) - 1] + [1 << center] * center
        rows += [1 << u for u in range(center + 1, n - 1)] + [0]
        matching = [0, center] + [-1] * (center - 1)
        matching += list(range(center + 1, n - 1)) + [-1]
    elif mode == "empty":
        rows, matching = [0] * n, [-1] * n
    elif mode == "triangular":
        rows = [full ^ ((1 << u) - 1) for u in range(n)]
        matching = list(range(n))
    elif mode == "deficient_chain":
        rows = [1] + [(1 << (u - 1)) | (1 << u) for u in range(1, n - 1)]
        rows += [1 << (n - 2)]
        matching = list(range(n - 1)) + [-1]
    else:
        raise ValueError("Unknown mode")
    assert len(rows) == len(matching) == n
    permuted = mode.endswith("_permuted") or mode in (
        "deficient_dense",
        "half_block",
        "mixed",
        "deficient_chain",
    )
    if permuted:
        rng = random.Random(seed)
        left_labels, right_labels = list(range(n)), list(range(n))
        rng.shuffle(left_labels)
        rng.shuffle(right_labels)
        transformed, mapped_matching = [0] * n, [-1] * n
        for u, mask in enumerate(rows):
            while mask:
                bit = mask & -mask
                mask -= bit
                transformed[left_labels[u]] |= 1 << right_labels[bit.bit_length() - 1]
            if matching[u] >= 0:
                mapped_matching[left_labels[u]] = right_labels[matching[u]]
        rows, matching = transformed, mapped_matching
    return rows, matching


def main():
    seed, mode = int(sys.argv[1]), sys.argv[2]
    rows, _ = build(seed, mode)
    print(SIZE, SIZE, sum(row.bit_count() for row in rows))
    rng = random.Random(seed)
    order = list(range(SIZE))
    rng.shuffle(order)
    for u in order:
        mask, neighbors = rows[u], []
        while mask:
            bit = mask & -mask
            mask -= bit
            neighbors.append(bit.bit_length())
        rng.shuffle(neighbors)
        sys.stdout.write("".join(f"{u + 1} {v}\n" for v in neighbors))


if __name__ == "__main__":
    main()
