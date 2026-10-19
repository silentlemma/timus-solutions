"""Generate maximum binary boards: seed mode.

Modes: all_black, all_white, alternating, defect, corners, impossible,
alternating_noise, block_sparse, block_dense, star_one_defect,
star_sparse_noise, many_stripes_noise, embedded_star_noise,
embedded_stripes_noise, embedded_block_noise, diagonal_zeros, triangular,
random_half, random_half_large_k, embedded_star_clean.
Noise families use one seeded stream with deterministic family offsets.
"""

import random
import sys

SIZE = 1000
HALF = SIZE // 2
QUARTER = SIZE // 4
PERIOD = 20
NOISE = 0.002
RARE_NOISE = 0.001
ALTERNATING_NOISE = 0.02
STAR_MARGIN = SIZE // PERIOD
STRIPE_MARGIN = SIZE // 5
BLOCK_MARGIN = SIZE // 10
DEFECT = SIZE * 7 // 10
PACKED_MODES = (
    "alternating_noise",
    "block_sparse",
    "block_dense",
    "star_one_defect",
    "star_sparse_noise",
    "many_stripes_noise",
)
EXTRA_MODES = (
    "embedded_star_noise",
    "embedded_stripes_noise",
    "embedded_block_noise",
    "diagonal_zeros",
    "triangular",
    "random_half",
    "random_half_large_k",
    "embedded_star_clean",
)


def skip_stream(rng, mode, modes, counts):
    for previous in modes:
        if previous == mode:
            return
        for _ in range(counts[previous]):
            rng.random()
    raise ValueError("Unknown mode")


def build(seed, mode):
    rng = random.Random(seed)
    if mode in ("all_black", "all_white", "impossible"):
        n = SIZE - 1 if mode == "impossible" else SIZE
        k = SIZE if mode == "impossible" else HALF if mode == "all_black" else 1
        return [("0" if mode == "all_white" else "1") * SIZE] * n, k
    if mode in ("alternating", "defect"):
        grid = ["1" * SIZE if r % 2 else "01" * HALF for r in range(SIZE)]
        if mode == "defect":
            row = grid[HALF]
            grid[HALF] = row[:HALF] + "1" + row[HALF + 1 :]
        return grid, QUARTER if mode == "alternating" else 2
    if mode == "corners":
        grid = ["1" * SIZE] * SIZE
        grid[0], grid[-1] = "0" + "1" * (SIZE - 1), "1" * (SIZE - 1) + "0"
        return grid, 1
    if mode in PACKED_MODES:
        free = SIZE - SIZE // PERIOD
        draws = {
            "alternating_noise": HALF * HALF,
            "block_sparse": HALF * HALF,
            "block_dense": HALF * HALF,
            "star_one_defect": 0,
            "star_sparse_noise": (SIZE - 1) ** 2,
            "many_stripes_noise": free * free,
        }
        skip_stream(rng, mode, PACKED_MODES, draws)
        k = 2 if mode == "alternating_noise" else HALF if mode.startswith("block_") else 1
        if mode == "many_stripes_noise":
            k = SIZE // PERIOD
        grid = []
        for r in range(SIZE):
            line = []
            for c in range(SIZE):
                if mode == "alternating_noise":
                    black = r % 2 or c % 2 or rng.random() < ALTERNATING_NOISE
                elif mode.startswith("block_"):
                    probability = RARE_NOISE if mode == "block_sparse" else 0.5
                    black = r < HALF or c < HALF or rng.random() < probability
                elif mode == "star_one_defect":
                    black = r == HALF or c == HALF or r == DEFECT and c == DEFECT
                elif mode == "star_sparse_noise":
                    black = r == HALF or c == HALF or rng.random() < NOISE
                else:
                    black = r % PERIOD == 0 or c % PERIOD == 0 or rng.random() < NOISE
                line.append("1" if black else "0")
            grid.append("".join(line))
        return grid, k
    if mode not in EXTRA_MODES:
        raise ValueError("Unknown mode")
    star_span = SIZE - 2 * STAR_MARGIN
    stripe_span = SIZE - 2 * STRIPE_MARGIN
    block_span = SIZE - 2 * BLOCK_MARGIN
    draws = {
        "embedded_star_noise": SIZE * SIZE - (2 * star_span - 1),
        "embedded_stripes_noise": SIZE * SIZE - stripe_span * stripe_span * 3 // 4,
        "embedded_block_noise": SIZE * SIZE - (block_span**2 - (block_span - QUARTER) ** 2),
        "diagonal_zeros": 0,
        "triangular": 0,
        "random_half": SIZE * SIZE,
        "random_half_large_k": SIZE * SIZE,
        "embedded_star_clean": 0,
    }
    skip_stream(rng, mode, EXTRA_MODES, draws)
    k = 2 if mode == "embedded_stripes_noise" else QUARTER if mode == "embedded_block_noise" else 1
    if mode == "random_half_large_k":
        k = HALF
    grid = []
    for r in range(SIZE):
        line = []
        for c in range(SIZE):
            if mode.startswith("embedded_star"):
                black = (
                    r == HALF
                    and STAR_MARGIN <= c < SIZE - STAR_MARGIN
                    or c == HALF
                    and STAR_MARGIN <= r < SIZE - STAR_MARGIN
                )
                if mode.endswith("noise"):
                    black = black or rng.random() < NOISE
            elif mode == "embedded_stripes_noise":
                black = (
                    STRIPE_MARGIN <= r < SIZE - STRIPE_MARGIN
                    and STRIPE_MARGIN <= c < SIZE - STRIPE_MARGIN
                    and (r % 2 or c % 2)
                )
                black = black or rng.random() < NOISE
            elif mode == "embedded_block_noise":
                black = (
                    BLOCK_MARGIN <= r < SIZE - BLOCK_MARGIN
                    and BLOCK_MARGIN <= c < SIZE - BLOCK_MARGIN
                    and (r < BLOCK_MARGIN + QUARTER or c < BLOCK_MARGIN + QUARTER)
                )
                black = black or rng.random() < NOISE
            elif mode == "diagonal_zeros":
                black = r != c
            elif mode == "triangular":
                black = r < c
            else:
                black = rng.random() < 0.5
            line.append("1" if black else "0")
        grid.append("".join(line))
    return grid, k


def main():
    grid, k = build(int(sys.argv[1]), sys.argv[2])
    print(len(grid), len(grid[0]), k)
    print(*grid, sep="\n")


if __name__ == "__main__":
    main()
