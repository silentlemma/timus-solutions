import sys

FIELDS = 3  # attack, shield and coins of a knight


def top_two(values):
    """The two largest values and the position of the first one; -1 stands
    for a missing value, so a lone knight needs nothing."""
    first, second, where = -1, -1, -1
    for index, value in enumerate(values):
        if value > first:
            first, second, where = value, first, index
        elif value > second:
            second = value
    return first, second, where


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1::FIELDS][:n]
    d = data[2::FIELDS][:n]
    g = data[FIELDS::FIELDS][:n]
    # the strongest attack and shield each rival can afford
    attack = top_two([a[i] + g[i] for i in range(n)])
    shield = top_two([d[i] + g[i] for i in range(n)])
    for i in range(n):
        # The shield must exceed every rival's best attack and the attack must
        # reach every rival's best shield, whatever the rivals do.
        rival_attack = attack[1] if attack[2] == i else attack[0]
        rival_shield = shield[1] if shield[2] == i else shield[0]
        cost = max(0, rival_attack + 1 - d[i]) + max(0, rival_shield - a[i])
        if cost <= g[i]:
            print(i + 1)
            return
    print(-1)


main()
