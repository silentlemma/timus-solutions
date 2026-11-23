import os
from array import array
import sys

OUTPUT_CHUNK_LINES = 1024
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
    first_count = next(values)
    first = array("h", (next(values) for _ in range(3 * first_count)))
    second_count = next(values)
    second = array("h", (next(values) for _ in range(3 * second_count)))
    result = array("h")
    j = 0
    for index in range(0, len(first), 3):
        a, b, y = first[index : index + 3]
        cur = a
        # walk through [a, b) and keep what no interval of the second covers
        while cur < b:
            while j < len(second) and second[j + 1] <= cur:
                j += 3
            if j < len(second) and second[j] <= cur:
                cur = second[j + 1]
                continue
            end = min(b, second[j]) if j < len(second) else b
            result.extend((cur, end, y))
            cur = end
    write = sys.stdout.write
    write(str(len(result) // 3))
    for start in range(0, len(result), OUTPUT_CHUNK_LINES):
        write(" " + " ".join(map(str, result[start : start + OUTPUT_CHUNK_LINES])))
    write("\n")


main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
