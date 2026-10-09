import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    # equation v over GF(2) as an integer bit mask: the chosen technicians turn
    # valve v an odd number of times; bit n is the right-hand side
    eq = [1 << n] * n
    i = 1
    for t in range(n):
        while data[i] != -1:
            eq[data[i] - 1] |= 1 << t
            i += 1
        i += 1
    # Gauss-Jordan elimination: column c ends with a single 1, in its pivot row
    pivot_of = [-1] * n
    rank = 0
    for c in range(n):
        bit = 1 << c
        r = next((r for r in range(rank, n) if eq[r] & bit), -1)
        if r < 0:
            continue
        eq[r], eq[rank] = eq[rank], eq[r]
        row = eq[rank]
        eq = [e ^ row if i != rank and e & bit else e for i, e in enumerate(eq)]
        pivot_of[c] = rank
        rank += 1
    if any(eq[r] >> n & 1 for r in range(rank, n)):
        print("No solution")
        return
    # independent technicians make the solution unique, so it is also the shortest
    chosen = [c + 1 for c in range(n) if pivot_of[c] >= 0 and eq[pivot_of[c]] >> n & 1]
    print(" ".join(map(str, chosen)))


main()
