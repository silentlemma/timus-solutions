import os
import sys

INPUT_BUFFER_BYTES = 4096
WHITESPACE = 32


def words():
    """Yield whitespace-separated tokens with bounded temporary storage."""
    pending = b""
    while True:
        block = os.read(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > WHITESPACE else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = map(int, words())
    a, b = next(values), next(values)
    previous = next(values)
    pieces, way = 1, 0
    # stretch this piece while it stays monotone; its way up or down is
    # fixed by its first step that is not flat
    for _ in range(b - a):
        value = next(values)
        step = (value > previous) - (value < previous)
        if step and way and step != way:
            pieces += 1
            way = 0
        else:
            way = way or step
        previous = value
    print(pieces)


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
