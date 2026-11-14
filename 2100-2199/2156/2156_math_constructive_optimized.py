from sys import stdin, stdout

BLOCK_SIZE = 1 << 14
OUTPUT_BATCH = 1024


def numbers():
    pending = b""
    while block := stdin.buffer.read(BLOCK_SIZE):
        # Keep the last token until the next block, which may complete it.
        tokens = (pending + block).split()
        pending = tokens.pop() if tokens and not block[-1:].isspace() else b""
        yield from map(int, tokens)
    if pending:
        yield int(pending)


def write_group(falls, group, count):
    stdout.write(f"{count}\n")
    batch = []
    for edge, flag in enumerate(falls, 1):
        if flag == group:
            batch.append(str(edge))
            if len(batch) == OUTPUT_BATCH:
                stdout.write(" ".join(batch) + " ")
                batch.clear()
    stdout.write(" ".join(batch) + "\n")


def main():
    values = numbers()
    n, first = next(values), next(values)
    falls = bytearray(n)
    previous = first
    for edge, current in enumerate(values):
        falls[edge] = previous > current
        previous = current
    falls[-1] = previous > first
    count = sum(falls)
    if not count:
        falls[0] = count = 1
    stdout.write("YES\n")
    write_group(falls, 1, count)
    write_group(falls, 0, n - count)


if __name__ == "__main__":
    main()
