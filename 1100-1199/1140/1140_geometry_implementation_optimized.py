from os import read as read_input
from os import _exit as _finish_process
import sys as _finish_sys


INPUT_BUFFER_BYTES = 4096


def words():
    """Yield tokens while retaining only one bounded input chunk and its unfinished token."""
    pending = b""
    while True:
        block = read_input(0, INPUT_BUFFER_BYTES)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > 32 else b""
        yield from parts
    if pending:
        yield pending


def main():
    values = iter(words())
    n = int(next(values))
    total = {b"X": 0, b"Y": 0, b"Z": 0}
    for _ in range(n):
        direction = next(values)
        total[direction] += int(next(values))
    # a step along Y is a step along X and one along Z, so the walk ends at
    # a X + b Z; going back with m steps along Y costs |a - m| + |m| + |b - m|,
    # which is smallest at the median of a, 0 and b
    a = total[b"X"] + total[b"Y"]
    b = total[b"Z"] + total[b"Y"]
    m = sorted((a, 0, b))[1]
    back = [("X", m - a), ("Y", -m), ("Z", m - b)]
    back = [(d, k) for d, k in back if k]
    print(len(back))
    for d, k in back:
        print(d, k)


main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
