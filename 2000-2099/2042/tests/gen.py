"""Maximum bounded-palindrome workloads with distinct update/query patterns."""

import random
import string
import sys

MAX_N = 100000
MAX_M = 100000
MAX_K = 50
MODES = (
    "uniform_queries",
    "alternating_queries",
    "periodic_queries",
    "random_queries",
    "short_queries",
    "mixed_short_updates",
    "mixed_long_updates",
    "point_updates",
    "edge_updates",
    "k_one",
    "k_two",
    "short_string",
    "updates_only",
    "singleton",
)


def generate(seed, mode):
    rng = random.Random(seed)
    n = 31 if mode == "short_string" else 1 if mode == "singleton" else MAX_N
    k = (
        1
        if mode == "k_one"
        else 2
        if mode == "k_two"
        else 49
        if mode in ("periodic_queries", "edge_updates")
        else MAX_K
    )
    if mode == "uniform_queries":
        word = "a" * n
    elif mode in ("alternating_queries", "point_updates"):
        word = ("ab" * ((n + 1) // 2))[:n]
    elif mode in ("random_queries", "mixed_long_updates", "k_one", "k_two"):
        word = "".join(rng.choices(string.ascii_lowercase, k=n))
    else:
        word = ("abacaba" * ((n + 6) // 7))[:n]
    yield f"{word} {k}"
    yield str(MAX_M)
    for step in range(MAX_M):
        if mode == "mixed_short_updates":
            if step % 2 == 0:
                left = rng.randrange(n)
                right = min(n - 1, left + rng.randrange(1, 2 * k))
                if step % 16 == 0:
                    left, right = 0, n - 1
                yield f"1 {left + 1} {right + 1} {rng.choice('abcde')}"
            else:
                left = rng.randrange(n // 3)
                right = rng.randrange(2 * n // 3, n)
                yield f"2 {left + 1} {right + 1}"
            continue
        left, right = sorted((rng.randrange(n), rng.randrange(n)))
        if mode.endswith("queries"):
            if mode == "short_queries" or step % 3 == 1:
                right = min(n - 1, left + rng.randrange(2 * k))
            elif step % 3 == 0:
                left, right = 0, n - 1
            yield f"2 {left + 1} {right + 1}"
            continue
        update = step % 2 == 0 or mode == "updates_only"
        if mode == "point_updates":
            if update:
                right = left
        elif mode == "edge_updates":
            width = rng.randint(1, min(n, 2 * k))
            left, right = (0, width - 1) if step % 4 < 2 else (n - width, n - 1)
        elif mode == "updates_only":
            if step % 8 == 0:
                left, right = 0, n - 1
            else:
                right = min(n - 1, left + rng.randrange(2 * k))
        elif step % 16 == 0:
            left, right = 0, n - 1
        if update:
            yield f"1 {left + 1} {right + 1} {rng.choice('abcde')}"
        else:
            yield f"2 {left + 1} {right + 1}"


if __name__ == "__main__":
    chosen = sys.argv[2]
    if chosen not in MODES:
        raise SystemExit("unknown workload")
    sys.stdout.write("\n".join(generate(int(sys.argv[1]), chosen)) + "\n")
