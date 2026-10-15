import sys

SHARES = 3  # a bill is split three ways


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    n, m = data[0], data[1]
    total = 0
    for i in range(m):
        total += data[2 + i]
        # Vanya's share total / 3 exceeds n exactly when total > 3n
        if total > SHARES * n:
            print("Free after %d times." % (i + 1))
            return
    print("Team.GOV!")


main()
