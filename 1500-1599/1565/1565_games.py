import sys
from itertools import permutations

EPS = 1e-12  # survival chances closer than this count as equal
AIR = -1  # a shot into the air
SHOOTERS = 3


def main():
    acc = [float(v) for v in sys.stdin.read().split()]

    def strongest(shooter, alive):
        """The most accurate living opponent; the earlier one on a tie."""
        rivals = [i for i in alive if i != shooter]
        return max(rivals, key=lambda i: (acc[i], -i))

    def duel(first, second):
        """Two left, first to shoot: first wins p / (p + q - p q)."""
        p, q = acc[first], acc[second]
        chances = [0.0] * SHOOTERS
        chances[first] = p / (p + q - p * q)
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
        alive = range(SHOOTERS)
        if shooter == 0:
            return after_hit(order, turn, strongest(shooter, alive))
        p = acc[shooter]
        miss = three(order, (turn + 1) % SHOOTERS)
        outcomes = {AIR: miss}
        for target in alive:
            if target != shooter:
                hit = after_hit(order, turn, target)
                outcomes[target] = [p * h + (1 - p) * m for h, m in zip(hit, miss)]
        best = max(v[shooter] for v in outcomes.values())
        # on a tie the strongest opponent is shot, then A, B, C, then the air
        for choice in [strongest(shooter, alive), 0, 1, 2, AIR]:
            if choice in outcomes and outcomes[choice][shooter] >= best - EPS:
                return outcomes[choice]

    total = [0.0] * SHOOTERS
    orders = list(permutations(range(SHOOTERS)))
    for order in orders:
        for i, v in enumerate(three(order, 0)):
            total[i] += v
    print(" ".join("%.5f" % (v * (1 / len(orders))) for v in total))


main()
