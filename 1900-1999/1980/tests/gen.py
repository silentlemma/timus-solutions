"""Usage: gen.py SEED MODE; modes: chain_max, chain_zero, chain_zero_large, chain_mixed, chain_large_deadline, parallel, heap_stale, switch_low, switch_high, irrelevant, tiny_root, uniform_bfs."""

import random

MODES = (
    "chain_max",
    "chain_zero",
    "chain_zero_large",
    "chain_mixed",
    "chain_large_deadline",
    "parallel",
    "heap_stale",
    "switch_low",
    "switch_high",
    "irrelevant",
    "tiny_root",
    "uniform_bfs",
)


def generate(seed, mode):
    rng = random.Random(seed)
    n = 10000
    if mode.startswith("chain_"):
        speed, length, deadline = 1, 1000, 1
        if mode == "chain_zero":
            speed, length, deadline = 3, 1, 3333
        if mode == "chain_zero_large":
            speed, length, deadline = 300, 1000, 33330
        if mode == "chain_large_deadline":
            deadline = 10**6
        edges = []
        groups = {}
        for i in range(n - 1):
            s, l = (
                (rng.randint(1, 300), rng.randint(1, 1000))
                if mode == "chain_mixed"
                else (speed, length)
            )
            edges.append((i, i + 1, s, l))
            groups[s] = groups.get(s, 0) + l
        info = {"kind": "unique_chain", "speed_length_sums": groups}
    elif mode == "parallel":
        n = 2
        deadline = 1
        edges = [(0, 1, rng.randint(1, 300), rng.randint(501, 1000)) for _ in range(10000)]
        info = {"kind": "parallel"}
    elif mode == "heap_stale":
        n = 1500
        deadline = 1
        edges = [(i, i + 1, 300, 1) for i in range(n - 2)]
        for _ in range(10000 - len(edges) - 1):
            a = rng.randrange(n - 2)
            b = rng.randint(a + 1, min(n - 2, a + 1000))
            length = rng.randint(b - a, 1000)
            edges.append((a, b, 300, length))
        edges.append((n - 2, n - 1, 1, 1000))
        info = {
            "kind": "potential_prefix_and_bridge",
            "speed_length_sums": {300: n - 2, 1: 1000},
            "potential_prefix_end": n - 2,
        }
    elif mode in ("switch_low", "switch_high"):
        deadline = 1 if mode == "switch_low" else 20
        middle = (n - 2) // 2
        left = [0] + list(range(1, middle + 1)) + [n - 1]
        right = [0] + list(range(middle + 1, n - 1)) + [n - 1]
        edges = [(a, b, 1, 1) for a, b in zip(left, left[1:])]
        edges += [(a, b, 300, 2) for a, b in zip(right, right[1:])]
        info = {
            "kind": "two_uniform_routes",
            "routes": [(len(left) - 1, 1), (2 * (len(right) - 1), 300)],
        }
    elif mode == "irrelevant":
        deadline = 1
        edges = [(0, n - 1, 300, 1000)] + [(i, i + 1, 1, 1000) for i in range(1, n - 2)]
        while len(edges) < 10000:
            a, b = sorted(rng.sample(range(1, n - 1), 2))
            edges.append((a, b, rng.randint(1, 300), rng.randint(1, 1000)))
        info = {"kind": "single_usable_road", "speed_length_sums": {300: 1000}}
    elif mode == "tiny_root":
        deadline = 10**6
        raw = [(1, 1000)] * 999 + [(1, 999), (299, 1), (300, 299)]
        n = len(raw) + 1
        edges = [(i, i + 1, s, l) for i, (s, l) in enumerate(raw)]
        info = {"kind": "unique_chain", "speed_length_sums": {1: 999999, 299: 1, 300: 299}}
    elif mode == "uniform_bfs":
        n = 2000
        deadline = 1
        edges = [(i, i + 1, 1, 1) for i in range(n - 1)]
        while len(edges) < 10000:
            a, b = sorted(rng.sample(range(n), 2))
            edges.append((a, b, 1, 1))
        info = {"kind": "unit_length_BFS"}
    else:
        raise ValueError(mode)
    rng.shuffle(edges)
    assert 2 <= n <= 10000 and 1 <= len(edges) <= 10000
    assert all(0 <= a < b < n and 1 <= s <= 300 and 1 <= l <= 1000 for a, b, s, l in edges)
    return n, edges, deadline, info


if __name__ == "__main__":
    import sys

    n, edges, deadline, _ = generate(int(sys.argv[1]), sys.argv[2])
    print(n, len(edges))
    for a, b, s, l in edges:
        print(a + 1, b + 1, s, l)
    print(deadline)
