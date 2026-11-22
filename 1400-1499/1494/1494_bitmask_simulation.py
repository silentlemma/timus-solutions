from os import _exit, write
from sys import stdin

BLOCK_SIZE = 4096
WHITESPACE = ord(" ")
WORD_BITS = 32
WORD_MASK = (1 << WORD_BITS) - 1
WORD_SHIFT = 5


def numbers(source):
    pending = b""
    while block := source.read(BLOCK_SIZE):
        fields = (pending + block).split()
        pending = fields.pop() if block[-1] > WHITESPACE else b""
        yield from map(int, fields)
    if pending:
        yield int(pending)


def possible(balls):
    # Each entry packs a nonempty word's index and its 32 pending balls.
    # Entries stay in increasing word order, so the last word has the top.
    pocket = []
    highest = 0
    for ball in balls:
        if ball > highest:
            first, end = highest, ball - 1
            while first < end:
                index = first >> WORD_SHIFT
                stop = min(end, (index + 1) << WORD_SHIFT)
                mask = ((1 << (stop - first)) - 1) << (first & (WORD_BITS - 1))
                if pocket and pocket[-1] >> WORD_BITS == index:
                    pocket[-1] |= mask
                else:
                    pocket.append((index << WORD_BITS) | mask)
                first = stop
            highest = ball
        else:
            if not pocket:
                return False
            packet = pocket[-1]
            mask = packet & WORD_MASK
            top = ((packet >> WORD_BITS) << WORD_SHIFT) + mask.bit_length()
            if top != ball:
                return False
            mask ^= 1 << ((ball - 1) & (WORD_BITS - 1))
            if mask:
                pocket[-1] = (packet & ~WORD_MASK) | mask
            else:
                pocket.pop()
    return True


def main():
    values = numbers(stdin.buffer)
    next(values)
    answer = b"Not a proof\n" if possible(values) else b"Cheater\n"
    write(1, answer)
    _exit(0)


main()
