import sys

ALPHABET = 26


def main():
    data = sys.stdin.read().split()
    n, word = int(data[0]), data[1]
    size = len(word)
    # placing the remaining letter whose next occurrence is farthest moves at
    # least k places when k letters remain, so a universal word needs
    # n + (n - 1) + ... + 1 letters
    if size < n * (n + 1) // 2:
        print("NO")
        return
    fail = size + 1
    # after[c][p]: the place just after the first c at or after place p
    after = [[fail] * (size + 2) for _ in range(ALPHABET)]
    for c in range(ALPHABET):
        row = after[c]
        for p in range(size - 1, -1, -1):
            row[p] = p + 1 if ord(word[p]) - ord("a") == c else row[p + 1]
    # reach[mask]: how far the greedy embedding gets for the worst order of
    # the letters in mask; submasks come first in increasing order, and one
    # failing mask makes the whole set fail, so the table stops there
    reach = [0]
    for mask in range(1, 1 << n):
        best = 0
        rest = mask
        while rest:
            bit = rest & -rest
            rest ^= bit
            pos = after[bit.bit_length() - 1][reach[mask ^ bit]]
            if pos > best:
                best = pos
        if best == fail:
            print("NO")
            return
        reach.append(best)
    print("YES")


main()
