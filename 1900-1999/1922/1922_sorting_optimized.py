import os
import sys

INPUT_BUFFER_BYTES = 4096


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > 32 else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, words())
    n = next(values)
    ordered = sorted((next(values), index + 1) for index in range(n))
    sizes = []
    for size in range(1, n + 1):
        if ordered[size - 1][0] <= size and (size == n or ordered[size][0] > size + 1):
            sizes.append(size)
    indices = [str(index) for _, index in ordered]
    write = sys.stdout.write
    write(str(len(sizes)) + "\n")
    for size in sizes:
        write(str(size) + " " + " ".join(indices[:size]) + "\n")


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
