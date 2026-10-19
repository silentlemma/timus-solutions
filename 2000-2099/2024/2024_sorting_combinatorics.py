import sys

ALPHABET = 26
FIRST = ord("a")


def solve(text, limit):
    counts = [0] * ALPHABET
    for letter in text:
        counts[ord(letter) - FIRST] += 1
    counts.sort(reverse=True)
    size = sum(counts[:limit])
    boundary = counts[limit - 1]
    if boundary == 0:
        return size, 1
    greater = sum(count > boundary for count in counts)
    tied = counts.count(boundary)
    chosen = min(limit - greater, tied - (limit - greater))
    ways = 1
    for index in range(1, chosen + 1):
        ways = ways * (tied - index + 1) // index
    return size, ways


def main():
    text, limit = sys.stdin.read().split()
    print(*solve(text, int(limit)))


if __name__ == "__main__":
    main()
