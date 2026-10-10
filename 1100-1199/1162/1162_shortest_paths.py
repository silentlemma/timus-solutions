import sys

sys.set_int_max_str_digits(0)

# after the two currencies, a point gives a rate and a commission each way
TERMS = 4


def scaled(text, places):
    whole, _, fraction = text.partition('.')
    return int(whole + fraction + '0' * (places - len(fraction)))


def main():
    tok = iter(sys.stdin.read().split())
    n, m, s = int(next(tok)), int(next(tok)), int(next(tok))
    text = next(tok)
    places = max(2, len(text.partition('.')[2]))
    v = scaled(text, places)
    unit = 10 ** (places - 2)
    edges = []
    for _ in range(m):
        a, b = int(next(tok)), int(next(tok))
        rab, cab, rba, cba = (scaled(next(tok), 2) for _ in range(TERMS))
        edges += [(a, b, rab, cab), (b, a, rba, cba)]
    # All amounts share an exact denominator, multiplied by 100 each pass.
    # A change on pass n means a reachable gaining cycle.
    best = [-1] * (n + 1)
    best[s] = v
    for _ in range(n):
        after = [amount * 100 if amount >= 0 else -1 for amount in best]
        changed = False
        for a, b, rate, fee in edges:
            cost = fee * unit
            if best[a] >= cost:
                got = (best[a] - cost) * rate
                if got > after[b]:
                    after[b] = got
                    changed = True
        best = after
        unit *= 100
        v *= 100
        if best[s] > v or not changed:
            break
    print("YES" if best[s] > v or changed else "NO")


main()
