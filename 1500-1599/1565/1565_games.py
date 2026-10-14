import sys
from itertools import permutations

RATIO_DIGITS = 16
OUTPUT_SCALE = 10 ** 5
ROUND_EPS = 1e-8  # absorb floating-point noise at output rounding midpoints
SHOOTERS = 3


def main():
    tokens = sys.stdin.read().split()
    acc = [float(v) for v in tokens]
    digits = max(len(v.partition(".")[2]) for v in tokens)
    values = [v.replace(".", "") + "0" * (digits - len(v.partition(".")[2]))
              for v in tokens]
    values = [v.lstrip("0") or "0" for v in values]
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    exact = [int(v) for v in values]
    stronger = 1 if exact[1] > exact[2] else 2
    weaker = 3 - stronger
    scale = 10 ** digits
    high, low = exact[stronger], exact[weaker]
    product = (scale - high) * (scale - low)
    attack = [low == 0 or product >= high * scale,
              low == 0 or product * (scale - high) >= high * scale * scale]

    def ratio(first, second):
        a, b = values[first], values[second]
        x, y = a[:RATIO_DIGITS], b[:RATIO_DIGITS]
        return (float(x) / float(y)) * 10.0 ** ((len(a) - len(x)) - (len(b) - len(y)))

    def duel(first, second):
        """Two left, first to shoot: first wins p / (p + q - p q)."""
        p, q = acc[first], acc[second]
        chances = [0.0] * SHOOTERS
        if exact[first] >= exact[second]:
            chances[first] = 1 / (1 + ratio(second, first) * (1 - p))
        else:
            r = ratio(first, second)
            chances[first] = r / (1 + r * (1 - q))
        chances[second] = 1 - chances[first]
        return chances

    def after_hit(order, turn, killed):
        """The duel left after a hit, with the next living shooter first."""
        survivors = [i for i in order if i != killed]
        for step in range(1, SHOOTERS):
            first = order[(turn + step) % SHOOTERS]
            if first != killed:
                return duel(first, survivors[0] if survivors[1] == first else survivors[1])

    def three(order, turn):
        """Chances when all three live and order[turn] shoots. A never misses,
        so the shooting stops at A's turn at the latest."""
        shooter = order[turn]
        if shooter == 0:
            return after_hit(order, turn, stronger)
        p = acc[shooter]
        miss = three(order, (turn + 1) % SHOOTERS)
        # the weaker shooter attacks A iff (1-h)^k (1-l) >= h; ties attack
        next_is_stronger = order[(turn + 1) % SHOOTERS] != 0
        if shooter == weaker and not attack[next_is_stronger]:
            return miss
        hit = after_hit(order, turn, 0)
        return [p * h + (1 - p) * m for h, m in zip(hit, miss)]

    total = [0.0] * SHOOTERS
    orders = list(permutations(range(SHOOTERS)))
    for order in orders:
        for i, v in enumerate(three(order, 0)):
            total[i] += v
    rounded = [int(v * (1 / len(orders)) * OUTPUT_SCALE + 0.5 + ROUND_EPS) for v in total]
    print(" ".join(f"{v // OUTPUT_SCALE}.{v % OUTPUT_SCALE:05d}" for v in rounded))


main()
