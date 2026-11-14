import sys


PERCENT_SCALE = 100
OUTPUT_BATCH = 1024


def plateaus(size, kept, percentage):
    start, end, weight = 0, size - kept, 1
    while start < size:
        yield end - start, weight
        # The rank points into the previous prefix through position floor(100 * end / p).
        start, end = end, min(size, (PERCENT_SCALE * end) // percentage + 1)
        weight += 1


def main():
    size, kept, percentage = map(int, sys.stdin.buffer.read().split())
    write = sys.stdout.write
    if percentage == PERCENT_SCALE:
        # All kept weights are successive records.
        write(f"{size + kept * (kept + 1) // 2}\n")
        write("1 " * (size - kept))
        for start in range(2, kept + 2, OUTPUT_BATCH):
            write(" ".join(map(str, range(start, min(kept + 2, start + OUTPUT_BATCH)))))
            write(" " if start + OUTPUT_BATCH < kept + 2 else "\n")
        return
    write(f"{sum(count * weight for count, weight in plateaus(size, kept, percentage))}\n")
    separator = ""
    for count, weight in plateaus(size, kept, percentage):
        token = str(weight)
        write(separator + token + (" " + token) * (count - 1))
        separator = " "
    write("\n")


if __name__ == "__main__":
    main()
