import sys

LIMIT = 2 * 10 ** 6  # the largest possible sum of two notes
DEPTH = 10 ** 4  # augmenting paths visit at most 250 odd notes


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    notes = data[1:n + 1]
    prime = bytearray([1]) * (LIMIT + 1)
    prime[0] = prime[1] = 0
    i = 2
    while i * i <= LIMIT:
        if prime[i]:
            prime[i * i::i] = bytes(len(range(i * i, LIMIT + 1, i)))
        i += 1
    ones = notes.count(1)
    odd = [c for c in notes if c % 2 and c != 1]
    even = [c for c in notes if c % 2 == 0]
    # A prime sum is 2 = 1 + 1 or an odd prime, the sum of an odd and an even
    # note. So the surplus of odd notes must be paired as ones among themselves.
    surplus = ones + len(odd) - len(even)
    if surplus < 0 or surplus > ones:
        print("NO")
        return
    one_pairs = surplus // 2
    odd += [1] * (ones - 2 * one_pairs)
    near = [[v for v, e in enumerate(even) if prime[o + e]] for o in odd]
    partner = [-1] * len(even)

    def augment(u, visited):
        for v in near[u]:
            if not visited[v]:
                visited[v] = True
                if partner[v] < 0 or augment(partner[v], visited):
                    partner[v] = u
                    return True
        return False

    sys.setrecursionlimit(DEPTH)
    for u in range(len(odd)):
        if not augment(u, [False] * len(even)):
            print("NO")
            return
    out = ["YES"] + ["1 1"] * one_pairs
    out += ["%d %d" % (odd[partner[v]], even[v]) for v in range(len(even))]
    print("\n".join(out))


main()
