"""Usage: gen.py SEED MODE; every_second,heavy,reset_blocks,finish_event,late,exact_sum,long_series,deep_resets,random_mixed,sparse_drop,mixed_weights."""

import random
import sys

SIZE = 100000
MAXIMUM_WEIGHT = 10000
MAXIMUM_TIME = 1000000000


def generate(seed, mode):
    if mode == "every_second":
        return [1] * SIZE, list(range(1, SIZE + 1)), 1
    if mode == "heavy":
        return [MAXIMUM_WEIGHT] * SIZE, list(range(1, SIZE + 1)), 1
    if mode == "reset_blocks":
        return [MAXIMUM_WEIGHT] * SIZE, [10 * (i + 1) for i in range(SIZE)], MAXIMUM_TIME
    if mode == "finish_event":
        return [1] * SIZE, [SIZE], MAXIMUM_TIME
    if mode == "late":
        return [MAXIMUM_WEIGHT] * SIZE, [MAXIMUM_TIME], MAXIMUM_TIME
    if mode == "exact_sum":
        return [1] * SIZE, [SIZE], SIZE // 2 - 1
    if mode == "long_series":
        return [1] * SIZE, [3 * (i + 1) for i in range(SIZE)], 1
    if mode == "deep_resets":
        return (
            [MAXIMUM_WEIGHT] * SIZE,
            [(SIZE - 1) * (i + 1) for i in range(MAXIMUM_WEIGHT)],
            MAXIMUM_TIME,
        )
    if mode == "sparse_drop":
        return [MAXIMUM_WEIGHT] * SIZE, [2 * (i + 1) for i in range(SIZE)], 1
    if mode == "mixed_weights":
        return [1 if i % 2 == 0 else MAXIMUM_WEIGHT for i in range(SIZE)], [SIZE], MAXIMUM_WEIGHT
    rng = random.Random(seed)
    weights = [rng.randint(1, MAXIMUM_WEIGHT) for _ in range(SIZE)]
    events, time = [], 0
    for _ in range(SIZE):
        time += rng.randint(1, 30)
        events.append(time)
    return weights, events, SIZE


if __name__ == "__main__":
    weights, events, threshold = generate(int(sys.argv[1]), sys.argv[2])
    print(len(weights), len(events), threshold)
    print("\n".join(map(str, weights)))
    print("\n".join(map(str, events)))
