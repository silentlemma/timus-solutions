import sys

CHOICES = 3  # names offered for every problem


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    names = [sorted(data[1 + CHOICES * i:1 + CHOICES * (i + 1)]) for i in range(n)]
    order = [int(w) - 1 for w in data[1 + CHOICES * n:1 + (CHOICES + 1) * n]]
    # in the given order, the least name above the previous one leaves the
    # most room for the problems still to come
    chosen = []
    last = ""
    for p in order:
        bigger = [name for name in names[p] if name > last]
        if not bigger:
            print("IMPOSSIBLE")
            return
        last = bigger[0]
        chosen.append(last)
    print("\n".join(chosen))


main()
