import sys

SHOWN = 10  # suggestions per query


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    words = [(-int(data[2 + 2 * i]), data[1 + 2 * i]) for i in range(n)]
    m = int(data[1 + 2 * n])
    queries = data[2 + 2 * n : 2 + 2 * n + m]
    # the best words come first, so every queried prefix simply keeps the
    # first ten words that start with it
    found = {q: [] for q in queries}
    words.sort()
    for _, word in words:
        for end in range(1, len(word) + 1):
            box = found.get(word[:end])
            if box is not None and len(box) < SHOWN:
                box.append(word)
    out = b"\n".join(b"".join(w + b"\n" for w in found[q]) for q in queries)
    sys.stdout.buffer.write(out)


main()
