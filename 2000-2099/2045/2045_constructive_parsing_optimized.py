"""Use one constant run and a three-letter tail with no longer palindromes."""

from os import write as _native_write
from os import _exit as _finish_process
import sys as _finish_sys

import sys

TAIL = b"bcd"
OUTPUT_CHUNK_BYTES = 8192


def word_for(n, count, tail):
    if count < min(n, len(TAIL)):
        return b"NO"
    if n < len(TAIL):
        return b"a" * n
    prefix = count - len(TAIL)
    return b"a" * prefix + tail[: n - prefix]


def write_all(data):
    view = memoryview(data)
    try:
        while view:
            count = _native_write(1, view)
            if count <= 0:
                raise OSError("output made no progress")
            view = view[count:]
    finally:
        view.release()


def solve(n):
    write = write_all
    if n < len(TAIL):
        for count in range(1, n + 1):
            write(str(count).encode() + b" : " + word_for(n, count, b"") + b"\n")
        return
    word = bytearray((TAIL * ((n + len(TAIL) - 1) // len(TAIL)))[:n])
    rows = bytearray(b"1 : NO\n2 : NO\n")
    for count in range(3, n + 1):
        if count > 3:
            word[count - 4] = ord("a")
        rows.extend(str(count).encode())
        rows.extend(b" : ")
        rows.extend(word)
        rows.append(10)
        if len(rows) >= OUTPUT_CHUNK_BYTES:
            write(rows)
            rows.clear()
    if rows:
        write(rows)


def main():
    solve(int(sys.stdin.buffer.read()))


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # Flush the complete output before skipping interpreter teardown.
    _finish_sys.stdout.flush()
    _finish_sys.stderr.flush()
    _finish_process(0)
