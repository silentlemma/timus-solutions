"""Check actual card moves, and independently search for a move sequence for NO."""

import sys
from collections import deque
from pathlib import Path

HEADER_FIELDS = 3
CARD_FIELDS = 2
ARGUMENT_COUNT = 4


class Bad(Exception):
    pass


def read_input(source):
    data = list(map(int, Path(source).read_text(encoding="utf-8").split()))
    suits, ranks, row_count = data[:HEADER_FIELDS]
    rows = []
    owners = [0] * (suits * ranks)
    offset = HEADER_FIELDS
    for row_index in range(row_count):
        size = data[offset]
        offset += 1
        row = []
        for _ in range(size):
            suit, rank = data[offset : offset + CARD_FIELDS]
            offset += CARD_FIELDS
            card = (suit - 1) * ranks + rank - 1
            row.append(card)
            owners[card] = row_index
        rows.append(row)
    return suits, ranks, rows, owners


def can_finish(suits, ranks, rows, owners):
    next_rank = [0] * suits
    remaining = list(map(len, rows))
    ready = deque()
    for row_index, row in enumerate(rows):
        if row[-1] % ranks == 0:
            ready.append(row_index)
    moved = 0
    while ready:
        row_index = ready.popleft()
        if remaining[row_index] == 0:
            continue
        card = rows[row_index][remaining[row_index] - 1]
        suit, rank = divmod(card, ranks)
        if next_rank[suit] != rank:
            continue
        next_rank[suit] += 1
        remaining[row_index] -= 1
        moved += 1
        if remaining[row_index]:
            exposed = rows[row_index][remaining[row_index] - 1]
            other_suit, other_rank = divmod(exposed, ranks)
            if next_rank[other_suit] == other_rank:
                ready.append(row_index)
        if next_rank[suit] < ranks:
            successor = card + 1
            other_row = owners[successor]
            if remaining[other_row] and rows[other_row][remaining[other_row] - 1] == successor:
                ready.append(other_row)
    return moved == suits * ranks


def check(source, expected, output):
    suits, ranks, rows, owners = read_input(source)
    tokens = Path(output).read_text(encoding="utf-8").split()
    if not tokens or tokens[0] not in ("YES", "NO"):
        raise Bad("expected YES or NO")
    if tokens[0] == "NO":
        if len(tokens) != 1:
            raise Bad("extra output after NO")
        if can_finish(suits, ranks, rows, owners):
            raise Bad("the cards can all be moved")
        return
    total = suits * ranks
    if len(tokens) != 1 + CARD_FIELDS * total:
        raise Bad("expected exactly %d moves" % total)
    next_rank = [1] * suits
    for move in range(total):
        offset = 1 + CARD_FIELDS * move
        try:
            suit, rank = map(int, tokens[offset : offset + CARD_FIELDS])
        except ValueError:
            raise Bad("move %d: expected two integers" % (move + 1)) from None
        if not (1 <= suit <= suits and 1 <= rank <= ranks):
            raise Bad("move %d: card is out of range" % (move + 1))
        if next_rank[suit - 1] != rank:
            raise Bad("move %d: the previous rank has not been moved" % (move + 1))
        card = (suit - 1) * ranks + rank - 1
        row = rows[owners[card]]
        if not row or row[-1] != card:
            raise Bad("move %d: card is not at the right end of its row" % (move + 1))
        row.pop()
        next_rank[suit - 1] += 1


def main():
    try:
        if len(sys.argv) != ARGUMENT_COUNT:
            raise Bad("usage: checker.py input expected output")
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
