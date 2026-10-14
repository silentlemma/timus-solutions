import sys
from collections import Counter


def main():
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    # every record is two words, the kind and "Penguin"
    seen = Counter()
    for _ in range(n):
        seen[next(words)] += 1
        next(words)
    kind = seen.most_common(1)[0][0]
    print(kind + " Penguin")


main()
