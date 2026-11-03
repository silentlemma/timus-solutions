import sys

FLOORS = 1000
EGGS = FLOORS.bit_length()


def main():
    best = [[0] * (FLOORS + 1) for _ in range(EGGS + 1)]
    best[1] = list(range(FLOORS + 1))
    # With enough eggs, ordinary binary search needs at most ten drops.
    # The direct DP tries every first floor and pays for its worse outcome.
    for eggs in range(2, EGGS + 1):
        previous, row = best[eggs - 1], best[eggs]
        for floors in range(1, FLOORS + 1):
            row[floors] = 1 + min(
                max(previous[first - 1], row[floors - first]) for first in range(1, floors + 1)
            )
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    answer = []
    for eggs in tokens:
        floors = next(tokens)
        if eggs == floors == 0:
            break
        answer.append(str(best[min(eggs, EGGS)][floors]))
    print("\n".join(answer))


main()
