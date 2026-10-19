"""Usage: seed mode. All modes have n=1000, scores between 0 and 6.
Modes: first_wins_max_margin, second_wins_max_margin, all_zero_tie,
all_six_tie, equal_total_different_multisets, equal_multiset_permuted,
one_point_first_win, one_point_second_win, random_full_range.
"""

import random
import sys

COUNT = 1000
MAX_SCORE = 6
HALF_SCORE = MAX_SCORE // 2


def generate(seed, mode):
    n = COUNT
    rng = random.Random(seed)
    if mode == "first_wins_max_margin":
        first, second = [MAX_SCORE] * n, [0] * n
    elif mode == "second_wins_max_margin":
        first, second = [0] * n, [MAX_SCORE] * n
    elif mode == "all_zero_tie":
        first = second = [0] * n
    elif mode == "all_six_tie":
        first = second = [MAX_SCORE] * n
    elif mode == "equal_total_different_multisets":
        first, second = [0] * (n // 2) + [MAX_SCORE] * (n // 2), [HALF_SCORE] * n
    elif mode == "equal_multiset_permuted":
        first = [rng.randrange(MAX_SCORE + 1) for _ in range(n)]
        second = first.copy()
        rng.shuffle(second)
    elif mode in ("one_point_first_win", "one_point_second_win"):
        first, second = [MAX_SCORE] * (n - 1) + [1], [MAX_SCORE] * (n - 1) + [0]
        if mode == "one_point_second_win":
            first, second = second, first
    elif mode == "random_full_range":
        first, second = [[rng.randrange(MAX_SCORE + 1) for _ in range(n)] for _ in range(2)]
    else:
        raise ValueError("unknown mode")
    return str(n) + "\n" + " ".join(map(str, first)) + "\n" + " ".join(map(str, second)) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
