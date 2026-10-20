import random
import sys


SUITS = "abc"
RANK_COUNT = 9
TILE_COUNT = len(SUITS) * RANK_COUNT
COPIES = 4
HAND_SIZE = 14
MELD_SIZE = 3
MELD_COUNT = 4
SEQUENCE_STARTS = RANK_COUNT - MELD_SIZE + 1
BOUNDARY_WIDTH = 3
MIN_CHANGES = 1
MAX_CHANGES = 4

UNIFORM = 1
WINNING = 2
ONE_CHANGE = 3
TWO_CHANGES = 4
ONE_SUIT = 5
TWO_SUITS = 6
FOUR_COPIES = 7
BOUNDARIES = 8
OVERLAPPING = 9
MIXED_CHANGES = 10


def winning_hand(rng, only_suit=None):
    while True:
        hand = []
        for _ in range(MELD_COUNT):
            suit = rng.randrange(len(SUITS)) if only_suit is None else only_suit
            base = suit * RANK_COUNT
            if rng.randrange(2):
                start = base + rng.randrange(SEQUENCE_STARTS)
                hand.extend(range(start, start + MELD_SIZE))
            else:
                hand.extend([base + rng.randrange(RANK_COUNT)] * MELD_SIZE)
        pair = rng.randrange(TILE_COUNT)
        if only_suit is not None:
            pair = only_suit * RANK_COUNT + rng.randrange(RANK_COUNT)
        hand.extend([pair] * 2)
        if all(hand.count(tile) <= COPIES for tile in set(hand)):
            return hand


def change_hand(rng, hand, changes):
    for _ in range(changes):
        position = rng.randrange(HAND_SIZE)
        previous = hand[position]
        choices = [
            tile for tile in range(TILE_COUNT) if tile != previous and hand.count(tile) < COPIES
        ]
        hand[position] = rng.choice(choices)
    return hand


def sampled_hand(rng, suits, ranks):
    pack = [suit * RANK_COUNT + rank for suit in suits for rank in ranks for _ in range(COPIES)]
    return rng.sample(pack, HAND_SIZE)


def generate(mode, rng):
    if mode == UNIFORM:
        return sampled_hand(rng, range(len(SUITS)), range(RANK_COUNT))
    if mode == WINNING:
        return winning_hand(rng)
    if mode == ONE_CHANGE:
        return change_hand(rng, winning_hand(rng), MIN_CHANGES)
    if mode == TWO_CHANGES:
        return change_hand(rng, winning_hand(rng), 2)
    if mode == ONE_SUIT:
        return sampled_hand(rng, [rng.randrange(len(SUITS))], range(RANK_COUNT))
    if mode == TWO_SUITS:
        return sampled_hand(rng, rng.sample(range(len(SUITS)), 2), range(RANK_COUNT))
    if mode == FOUR_COPIES:
        tiles = rng.sample(range(TILE_COUNT), MELD_COUNT)
        hand = [tile for tile in tiles[:-1] for _ in range(COPIES)]
        hand.extend([tiles[-1]] * 2)
        return hand
    if mode == BOUNDARIES:
        ranks = list(range(BOUNDARY_WIDTH))
        ranks.extend(range(RANK_COUNT - BOUNDARY_WIDTH, RANK_COUNT))
        return sampled_hand(rng, range(len(SUITS)), ranks)
    if mode == OVERLAPPING:
        return winning_hand(rng, rng.randrange(len(SUITS)))
    if mode == MIXED_CHANGES:
        changes = rng.randint(MIN_CHANGES, MAX_CHANGES)
        return change_hand(rng, winning_hand(rng), changes)
    raise ValueError("unknown mode")


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    hand = generate(mode, rng)
    rng.shuffle(hand)
    print(" ".join(f"{tile % RANK_COUNT + 1}{SUITS[tile // RANK_COUNT]}" for tile in hand))


if __name__ == "__main__":
    main()
