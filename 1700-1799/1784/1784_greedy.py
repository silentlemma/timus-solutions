import sys

RANKS = 13


def main():
    cards = sys.stdin.read().split()
    suits = [[c[-1] for c in cards[i:i + RANKS]] for i in range(0, len(cards), RANKS)]
    count, depth = len(suits), RANKS
    moves = 0
    for level in range(depth - 1):
        # once the cards above level j sit in one-suit runs, the run ending at
        # level j of pile i must go onto the card one rank lower in its suit,
        # which lies at level j + 1 of pile target[i]
        holder = {suits[k][level + 1]: k for k in range(count)}
        target = [holder[suits[i][level]] for i in range(count)]
        # every pile with a change of suit here needs one move, and each cycle
        # of such piles needs one more, to a new pile and back
        seen = [False] * count
        for i in range(count):
            if target[i] == i or seen[i]:
                continue
            moves += 1
            k = i
            while not seen[k]:
                seen[k] = True
                moves += 1
                k = target[k]
    print(moves)


main()
