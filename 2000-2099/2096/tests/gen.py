"""Deterministic plan trees, questions, and arithmetic progression changes.

Modes: small, medium, limits, chain, siblings, changes, strides, empty,
rollback, and sweeps. The largest modes reach every aggregate input limit.
"""

import random
import sys

MAX_DAYS = 100_000
MAX_FRIENDS = 100_000
MAX_QUESTIONS = 100_000
MAX_CHANGES = 100_000
MAX_VISITS = 5_000_000
MAX_ACTIVITY = 1_000_000_000
SMALL_SIZE = 24
SMALL_ITEMS = 6
MEDIUM_DAYS = 1_000
MEDIUM_FRIENDS = 500
MEDIUM_COUNT = 30
STRIDE_FRIENDS = 100
BRANCH_LEAVES = 100
VISITS_PER_CHANGE = MAX_VISITS // MAX_CHANGES
FULL_SPAN_CHANGES = MAX_VISITS // MAX_DAYS
STRIDES = (1, 2, 7, 97, 1_999)


class Writer:
    def __init__(self, n, m, rng):
        assert 1 <= n <= MAX_DAYS and 1 <= m <= MAX_FRIENDS
        self.n = n
        self.m = m
        self.index = 0
        self.questions = 0
        self.changes = 0
        self.visits = 0
        print(n, m)
        print(*(rng.randint(1, MAX_ACTIVITY) for _ in range(n)))

    def block(self, queries, parent, changes):
        self.index += 1
        assert 0 <= parent < self.index
        assert len(queries) <= MAX_QUESTIONS
        assert len(changes) <= self.n
        self.questions += len(queries)
        self.changes += len(changes)
        print(len(queries))
        for target, day in queries:
            assert 0 <= target < self.index and 1 <= day <= self.n
            print(target, day)
        print(parent, len(changes))
        for day, count, period, activity in changes:
            assert 1 <= day <= self.n and 1 <= count <= self.n
            assert 1 <= period <= self.n and 1 <= activity <= MAX_ACTIVITY
            assert day + (count - 1) * period <= self.n
            self.visits += count
            print(day, count, period, activity)

    def finish(self):
        assert self.index == self.m
        assert self.questions <= MAX_QUESTIONS
        assert self.changes <= MAX_CHANGES
        assert self.visits <= MAX_VISITS


def change(rng, n, count=None, period=None):
    if period is None:
        period = rng.randint(1, n)
    if count is None:
        day = rng.randint(1, n)
        count = rng.randint(1, (n - day) // period + 1)
    else:
        day = rng.randint(1, n - (count - 1) * period)
    activity = rng.choice((1, MAX_ACTIVITY, rng.randint(1, MAX_ACTIVITY)))
    return day, count, period, activity


def random_tree(rng, medium):
    n = MEDIUM_DAYS if medium else rng.randint(1, SMALL_SIZE)
    m = MEDIUM_FRIENDS if medium else rng.randint(1, SMALL_SIZE)
    writer = Writer(n, m, rng)
    item_limit = 10 if medium else SMALL_ITEMS
    for index in range(1, m + 1):
        queries = [
            (rng.randrange(index), rng.randint(1, n)) for _ in range(rng.randint(0, item_limit))
        ]
        changes = []
        for _ in range(rng.randint(0, min(n, item_limit))):
            if medium:
                count = rng.randint(1, MEDIUM_COUNT)
                period = rng.randint(1, n // count)
                changes.append(change(rng, n, count, period))
            else:
                changes.append(change(rng, n))
        writer.block(queries, rng.randrange(index), changes)
    writer.finish()


def maximum_tree(rng, mode):
    n = MAX_DAYS
    m = MAX_FRIENDS
    if mode == "chain":
        n = 10
    writer = Writer(n, m, rng)
    branch_point = m - BRANCH_LEAVES
    for index in range(1, m + 1):
        parent = index - 1
        if mode == "siblings":
            parent = 0
        elif mode == "rollback" and index > branch_point:
            parent = branch_point
        elif mode == "empty":
            parent = rng.randrange(index)
        queries = [] if mode == "empty" else [(index - 1, rng.randint(1, n))]
        count = 1 if mode == "chain" else VISITS_PER_CHANGE
        period = rng.randint(1, n // count)
        writer.block(queries, parent, [change(rng, n, count, period)])
    writer.finish()


def many_changes(rng):
    n = MAX_DAYS
    writer = Writer(n, 2, rng)
    changes = [
        change(rng, n, VISITS_PER_CHANGE, rng.randint(1, n // VISITS_PER_CHANGE))
        for _ in range(MAX_CHANGES)
    ]
    writer.block([], 0, changes)
    queries = [(1, day) for day in range(1, MAX_QUESTIONS + 1)]
    writer.block(queries, 1, [])
    writer.finish()


def strided_tree(rng):
    n = MAX_DAYS
    writer = Writer(n, STRIDE_FRIENDS, rng)
    count = MAX_CHANGES // STRIDE_FRIENDS
    for index in range(1, STRIDE_FRIENDS + 1):
        queries = [(rng.randrange(index), rng.randint(1, n)) for _ in range(count)]
        changes = [change(rng, n, VISITS_PER_CHANGE, rng.choice(STRIDES)) for _ in range(count)]
        writer.block(queries, index // 2, changes)
    writer.finish()


def full_sweeps(rng):
    writer = Writer(MAX_DAYS, FULL_SPAN_CHANGES + 1, rng)
    for index in range(1, FULL_SPAN_CHANGES + 1):
        changes = [(1, MAX_DAYS, 1, rng.randint(1, MAX_ACTIVITY))]
        writer.block([], index - 1, changes)
    queries = [
        (rng.randrange(FULL_SPAN_CHANGES + 1), rng.randint(1, MAX_DAYS))
        for _ in range(MAX_QUESTIONS)
    ]
    writer.block(queries, FULL_SPAN_CHANGES, [])
    writer.finish()


def main():
    mode, seed = sys.argv[1], int(sys.argv[2])
    rng = random.Random(seed)
    if mode in ("small", "medium"):
        random_tree(rng, mode == "medium")
    elif mode in ("limits", "chain", "siblings", "empty", "rollback"):
        maximum_tree(rng, mode)
    elif mode == "changes":
        many_changes(rng)
    elif mode == "strides":
        strided_tree(rng)
    elif mode == "sweeps":
        full_sweeps(rng)
    else:
        raise SystemExit("unknown mode")


if __name__ == "__main__":
    main()
