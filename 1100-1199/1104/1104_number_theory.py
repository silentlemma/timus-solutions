import sys

MAX_BASE = 36


def main():
    digits = [int(ch, MAX_BASE) for ch in sys.stdin.read().split()[0]]
    # base k is 1 modulo k - 1, so the number is congruent to its digit sum
    total = sum(digits)
    for k in range(max(max(digits), 1) + 1, MAX_BASE + 1):
        if total % (k - 1) == 0:
            print(k)
            return
    print("No solution.")


main()
