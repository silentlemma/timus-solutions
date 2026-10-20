import sys

SUITS = 3
RANKS = 9
TYPES = SUITS * RANKS
TRIPLE_SIZE = 3
PAIR_SIZE = 2


def triples(counts):
    counts = counts.copy()
    for tile in range(TYPES):
        # Three equal sequences can be replaced with three triplets.
        runs = counts[tile] % TRIPLE_SIZE
        if not runs:
            continue
        if tile % RANKS > RANKS - TRIPLE_SIZE or counts[tile + 1] < runs or counts[tile + 2] < runs:
            return False
        counts[tile + 1] -= runs
        counts[tile + 2] -= runs
    return True


def winning(counts):
    pair_suit = -1
    for suit in range(SUITS):
        start = suit * RANKS
        remainder = sum(counts[start : start + RANKS]) % TRIPLE_SIZE
        if remainder == PAIR_SIZE and pair_suit == -1:
            pair_suit = suit
        elif remainder:
            return False
    if pair_suit == -1:
        return False
    start = pair_suit * RANKS
    for tile in range(start, start + RANKS):
        if counts[tile] >= PAIR_SIZE:
            counts[tile] -= PAIR_SIZE
            complete = triples(counts)
            counts[tile] += PAIR_SIZE
            if complete:
                return True
    return False


def classify(counts):
    if winning(counts):
        return "Tsumo"
    for removed in range(TYPES):
        if not counts[removed]:
            continue
        counts[removed] -= 1
        for added in range(TYPES):
            if added == removed:
                continue
            # A replacement may produce five identical tiles.
            counts[added] += 1
            ready = winning(counts)
            counts[added] -= 1
            if ready:
                return "Tenpai"
        counts[removed] += 1
    return "Noten"


def main():
    counts = [0] * TYPES
    for tile in sys.stdin.buffer.read().split():
        rank = tile[0] - ord("1")
        suit = tile[1] - ord("a")
        counts[suit * RANKS + rank] += 1
    print(classify(counts))


if __name__ == "__main__":
    main()
