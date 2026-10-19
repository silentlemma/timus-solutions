"""Checker: the first line is an order of all n cards, and putting every used
card back below the given number of cards keeps the next card to use on top.
The stack is a list of blocks, so each step costs about the square root of n."""

import sys

BLOCK = 512


class Bad(Exception):
    pass


class Stack:
    def __init__(self, cards):
        self.blocks = [cards[i:i + BLOCK] for i in range(0, len(cards), BLOCK)]

    def pop_top(self):
        card = self.blocks[0].pop(0)
        if not self.blocks[0]:
            self.blocks.pop(0)
        return card

    def insert(self, rank, card):
        for i, block in enumerate(self.blocks):
            if rank <= len(block):
                block.insert(rank, card)
                if len(block) > 2 * BLOCK:
                    self.blocks[i:i + 1] = [block[:BLOCK], block[BLOCK:]]
                return
            rank -= len(block)
        self.blocks.append([card])

    def top(self):
        return self.blocks[0][0]


def check(source, expected, output):
    data = open(source).read().split()
    n, k = int(data[0]), int(data[1])
    uses = [int(v) for v in data[2:2 + k]]
    got = open(output).read().split()
    if len(got) != n + k or not all(w.isdigit() for w in got):
        raise Bad("expected %d cards and %d positions" % (n, k))
    cards = [int(w) for w in got[:n]]
    if sorted(cards) != list(range(1, n + 1)):
        raise Bad("the first line is not an order of the cards")
    stack = Stack(cards)
    for i, card in enumerate(uses):
        if stack.top() != card:
            raise Bad("use %d: card %d is not on top" % (i + 1, card))
        stack.pop_top()
        rank = int(got[n + i])
        if rank > n - 1:
            raise Bad("use %d: only %d other cards" % (i + 1, n - 1))
        stack.insert(rank, card)


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
