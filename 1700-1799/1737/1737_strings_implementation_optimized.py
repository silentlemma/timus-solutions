from os import _exit as _finish_process
import sys as _finish_sys
import sys

LIMIT = 100000
LETTERS = b"abc"
PERIOD = len(LETTERS)
WORD_COUNT = PERIOD * (PERIOD - 1)

n = int(sys.stdin.read())
write = sys.stdout.buffer.write
if n == 1:
    write(bytes((LETTERS[0], 10, LETTERS[1], 10, LETTERS[2], 10)))
elif WORD_COUNT * n > LIMIT:
    write(b"TOO LONG\n")
else:
    index_sum = PERIOD * (PERIOD - 1) // 2
    lines = []
    for first in range(PERIOD):
        for second in range(PERIOD):
            if first != second:
                third = index_sum - first - second
                pattern = bytes((LETTERS[first], LETTERS[second], LETTERS[third]))
                lines.append(pattern * (n // PERIOD) + pattern[: n % PERIOD])
    write(b"\n".join(lines) + b"\n")


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
