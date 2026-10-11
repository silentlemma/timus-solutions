import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    weight, n = data[0], data[1]
    cards = data[2 : 2 + n]
    mask = (1 << (weight + 1)) - 1
    # bit s of once[i] / twice[i]: at least one / two sets of the first i
    # cards weigh s
    once, twice = [1], [0]
    for c in cards:
        a, b = once[-1], twice[-1]
        once.append((a | a << c) & mask)
        twice.append((b | b << c | a & a << c) & mask)
    if twice[n] >> weight & 1:
        print(-1)
        return
    if not once[n] >> weight & 1:
        print(0)
        return
    # the only set: card i is in it exactly when the rest cannot be made
    # from the cards before it
    missing, s = [], weight
    for i in range(n, 0, -1):
        if once[i - 1] >> s & 1:
            missing.append(i)
        else:
            s -= cards[i - 1]
    print(" ".join(map(str, reversed(missing))))


main()
