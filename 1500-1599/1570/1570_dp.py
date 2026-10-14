import sys
from array import array

SCALE = 1000  # satiety has at most three digits after the point
DIGITS = 3
MOST_DISHES = 128  # more than the number of different dishes


def thousandths(text):
    whole, _, part = text.partition(".")
    return int(whole) * SCALE + int((part + "0" * DIGITS)[:DIGITS])


def main():
    words = iter(sys.stdin.read().split())
    n, m = int(next(words)), int(next(words))
    menu = [(next(words), int(next(words)), thousandths(next(words))) for _ in range(n)]
    top = m * SCALE
    # best[s]: the least cost, then the most different dishes, of an order with
    # satiety s, where s = top stands for top or more; one number holds both,
    # cost * MOST_DISHES - dishes, so that smaller is better
    none = float("inf")
    best = [none] * (top + 1)
    best[0] = 0
    # per dish: whether the best order at s takes it, and in the orders
    # that take it, the satiety before the last plate and if that plate was the
    # first one, which leaves the orders without the dish
    took, back, first = [], [], []
    for _, price, fill in menu:
        step = price * MOST_DISHES
        mine = [none] * (top + 1)
        before = array("i", [0]) * (top + 1)
        opened = bytearray(top + 1)
        for s in range(top + 1):
            if best[s] + step - 1 < mine[min(top, s + fill)]:
                t = min(top, s + fill)
                mine[t], before[t], opened[t] = best[s] + step - 1, s, 1
        # more plates of the same dish, from lower satiety up
        for s in range(top):
            t = min(top, s + fill)
            if mine[s] + step < mine[t]:
                mine[t], before[t], opened[t] = mine[s] + step, s, 0
        taken = bytearray(top + 1)
        for s in range(top + 1):
            if mine[s] < best[s]:
                best[s], taken[s] = mine[s], 1
        took.append(taken)
        back.append(before)
        first.append(opened)
    # walk back from the full order, dish by dish from the last one
    plates = [0] * n
    s = top
    for i in range(n - 1, -1, -1):
        if took[i][s]:
            while True:
                plates[i] += 1
                s, done = back[i][s], first[i][s]
                if done:
                    break
    cost = sum(menu[i][1] * plates[i] for i in range(n))
    lines = [str(cost)] + ["%s %d" % (menu[i][0], plates[i]) for i in range(n) if plates[i]]
    print("\n".join(lines))


main()
