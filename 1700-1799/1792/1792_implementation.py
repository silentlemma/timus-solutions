import sys

DISKS = 4


def valid(word):
    # petal j lies in every disk except disk j
    total = sum(word[:DISKS])
    return all((total - word[j]) % 2 == p for j, p in enumerate(word[DISKS:]))


def main():
    word = list(map(int, sys.stdin.read().split()))
    # try the word as it is, then each single change
    candidates = [word] + [word[:k] + [1 - word[k]] + word[k + 1:] for k in range(len(word))]
    print(*next(c for c in candidates if valid(c)))


main()
