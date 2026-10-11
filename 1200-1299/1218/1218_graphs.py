import sys

PARAMS = 3
MAJORITY = 2


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    names, stats = [], []
    for i in range(n):
        row = data[1 + (PARAMS + 1) * i : 1 + (PARAMS + 1) * (i + 1)]
        names.append(row[0])
        stats.append(list(map(int, row[1:])))
    # reach[i]: the Jedi that i beats, directly or through a chain of wins
    reach = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and sum(a > b for a, b in zip(stats[i], stats[j])) >= MAJORITY:
                reach[i] |= 1 << j
    for k in range(n):
        bit = 1 << k
        for i in range(n):
            if reach[i] & bit:
                reach[i] |= reach[k]
    everyone = (1 << n) - 1
    # a Jedi can win when every other one can be beaten along such a chain
    print("\n".join(names[i] for i in range(n) if reach[i] | 1 << i == everyone))


main()
