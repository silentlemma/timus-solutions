"""Generate deterministic deals with either one complete move order or no solution."""

import random
import sys
from collections import deque

MAX_CARDS = 100_000
SMALL_SUITS = 8
SMALL_RANKS = 8
SINGLE_RANKS = 100
MIXED_SUITS = 250
MIXED_RANKS = 400
PARTITION_CHANCE = 10
ARGUMENT_COUNT = 3


def ordered_cards(suits, ranks, rng, grouped=False):
    if grouped:
        suit_order = list(range(1, suits + 1))
        rng.shuffle(suit_order)
        return [(suit, rank) for suit in suit_order for rank in range(1, ranks + 1)]
    suit_order = list(range(1, suits + 1)) * ranks
    rng.shuffle(suit_order)
    next_rank = [0] * (suits + 1)
    cards = []
    for suit in suit_order:
        next_rank[suit] += 1
        cards.append((suit, next_rank[suit]))
    return cards


def unique_rows(cards, rng):
    # Each consecutive move is forced by a row edge or a same-suit rank edge.
    rows = []
    segment = []
    for card in cards:
        if segment and segment[-1][0] == card[0] and rng.randrange(2) == 0:
            rows.append(segment[::-1])
            segment = []
        segment.append(card)
    rows.append(segment[::-1])
    rng.shuffle(rows)
    return rows


def random_rows(cards, rng):
    rng.shuffle(cards)
    rows = []
    row = []
    for card in cards:
        if row and rng.randrange(PARTITION_CHANCE) == 0:
            rows.append(row)
            row = []
        row.append(card)
    if row:
        rows.append(row)
    return rows


def blocked_rows(suits, ranks, rng):
    blocked_suit = rng.randrange(1, suits + 1)
    cards = [
        (suit, rank)
        for suit in range(1, suits + 1)
        for rank in range(1, ranks + 1)
        if suit != blocked_suit or rank > 2
    ]
    rows = random_rows(cards, rng)
    rows.append([(blocked_suit, 1), (blocked_suit, 2)])
    rng.shuffle(rows)
    return rows


def has_unique_answer(suits, ranks, rows):
    total = suits * ranks
    edges = [[] for _ in range(total)]
    indegree = [0] * total
    for suit in range(suits):
        first = suit * ranks
        for card in range(first, first + ranks - 1):
            edges[card].append(card + 1)
            indegree[card + 1] += 1
    for row in rows:
        ids = [(suit - 1) * ranks + rank - 1 for suit, rank in row]
        for left, right in zip(ids, ids[1:]):
            edges[right].append(left)
            indegree[left] += 1
    ready = deque(card for card in range(total) if indegree[card] == 0)
    unique = True
    moved = 0
    while ready:
        unique = unique and len(ready) == 1
        card = ready.popleft()
        moved += 1
        for target in edges[card]:
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    return moved != total or unique


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        suits = rng.randrange(1, SMALL_SUITS + 1)
        ranks = rng.randrange(1, SMALL_RANKS + 1)
        rows = unique_rows(ordered_cards(suits, ranks, rng), rng)
    elif mode == "blocked":
        suits = rng.randrange(1, SMALL_SUITS + 1)
        ranks = rng.randrange(2, SMALL_RANKS + 1)
        rows = blocked_rows(suits, ranks, rng)
    elif mode == "random":
        suits = rng.randrange(2, SMALL_SUITS + 1)
        ranks = rng.randrange(2, SMALL_RANKS + 1)
        while True:
            cards = [(s, r) for s in range(1, suits + 1) for r in range(1, ranks + 1)]
            rows = random_rows(cards, rng)
            if has_unique_answer(suits, ranks, rows):
                break
    elif mode == "single":
        suits = 1
        ranks = rng.randrange(1, SINGLE_RANKS + 1)
        rows = unique_rows(ordered_cards(suits, ranks, rng), rng)
    elif mode == "chain":
        suits, ranks = MAX_CARDS, 1
        rows = [ordered_cards(suits, ranks, rng)[::-1]]
    elif mode == "rows":
        suits, ranks = 1, MAX_CARDS
        rows = [[(1, rank)] for rank in range(1, ranks + 1)]
        rng.shuffle(rows)
    elif mode in ("mixed", "bands"):
        suits, ranks = MIXED_SUITS, MIXED_RANKS
        cards = ordered_cards(suits, ranks, rng, grouped=mode == "bands")
        rows = unique_rows(cards, rng)
    elif mode == "blocked-large":
        suits, ranks = 2, MAX_CARDS // 2
        rows = blocked_rows(suits, ranks, rng)
    elif mode == "blocked-end":
        suits, ranks = 1, MAX_CARDS
        rows = [[(1, rank)] for rank in range(1, ranks - 1)]
        rows.append([(1, ranks - 1), (1, ranks)])
        rng.shuffle(rows)
    elif mode == "blocked-row":
        suits, ranks = 1, MAX_CARDS
        rows = [[(1, rank) for rank in range(1, ranks + 1)]]
    else:
        raise ValueError("unknown mode: " + mode)
    return suits, ranks, rows


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: gen.py MODE SEED")
    suits, ranks, rows = generate(sys.argv[1], int(sys.argv[2]))
    lines = ["%d %d %d" % (suits, ranks, len(rows))]
    for row in rows:
        values = [str(len(row))]
        for suit, rank in row:
            values.extend((str(suit), str(rank)))
        lines.append(" ".join(values))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
