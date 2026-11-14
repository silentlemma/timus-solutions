import sys

SHOWN = 10
MAX_FREQUENCY = 10**6
RANK_BYTES = 3


def main():
    read = sys.stdin.buffer.readline
    count = int(read())
    entries = []
    for _ in range(count):
        word, frequency = read().split()
        rank = MAX_FREQUENCY - int(frequency)
        entries.append(rank.to_bytes(RANK_BYTES, "big") + word)

    query_count = int(read())
    queries = [read().strip() for _ in range(query_count)]
    suggestions = {query: [] for query in queries}
    lengths = sorted({len(query) for query in suggestions})
    entries.sort()
    remaining = len(suggestions)
    for entry in entries:
        word = entry[RANK_BYTES:]
        for length in lengths:
            if length > len(word):
                break
            prefix = word[:length]
            box = suggestions.get(prefix)
            if box is not None and len(box) < SHOWN:
                box.append(word)
                if len(box) == SHOWN:
                    remaining -= 1
        if remaining == 0:
            break

    del entries
    blocks = {
        query: b"\n".join(box) + (b"\n" if box else b"") for query, box in suggestions.items()
    }
    write = sys.stdout.buffer.write
    for i, query in enumerate(queries):
        if i:
            write(b"\n")
        write(blocks[query])


if __name__ == "__main__":
    main()
