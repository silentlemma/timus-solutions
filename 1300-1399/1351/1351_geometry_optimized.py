import os
import sys

OUTPUT_CHUNK_LINES = 1024
INPUT_BUFFER_BYTES = 4096
WHITESPACE = 32

HEADER = 6  # the range, both borders and the count


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
    reach, rx, ry, lx, ly, n = (next(values) for _ in range(HEADER))
    out = []
    write = sys.stdout.write
    for _ in range(n):
        x, y = next(values), next(values)
        # inside the sector means left of the right border and right of the
        # left one, borders included; the sector is narrower than a half turn
        right, left = rx * y - ry * x, x * ly - y * lx
        inside = right >= 0 and left >= 0
        # a border's extension behind the gun is out; for a sector of zero
        # width, both borders along one ray, no other test rejects it
        behind = (right == 0 and rx * x + ry * y < 0) or (left == 0 and lx * x + ly * y < 0)
        out.append("YES" if inside and not behind and x * x + y * y <= reach * reach else "NO")
        if len(out) == OUTPUT_CHUNK_LINES:
            write("\n".join(out) + "\n")
            out.clear()
    if out:
        write("\n".join(out) + "\n")


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
