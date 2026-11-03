import sys


def main():
    stream = sys.stdin.buffer
    header = stream.readline()
    while not header.strip():
        header = stream.readline()
    n, m = map(int, header.split())
    values = (int(line) for line in stream if line.strip())

    def summary(count):
        first = last = largest = next(values)
        for _ in range(count - 1):
            last = next(values)
            if last > largest:
                largest = last
        return first, last, largest

    first_v, last_v, max_v = summary(n)
    first_h, last_h, max_h = summary(m)
    # Input gives one street per line. No whole-file tokens or street lists.
    # Qualifying streets cross: both directions and both endpoints must work.
    print(min(max_v, max_h, max(first_v, first_h), max(last_v, last_h)))


main()
