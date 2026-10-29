import sys
from math import isqrt

DISCRIMINANT_FACTOR = 8
OUTPUT_SIZE = 1 << 10
# the input is parsed line by line, and the answers are collected as bytes
# and written in 1 KB pieces
words = (word for line in sys.stdin.buffer for word in line.split())
count = int(next(words))
answer = bytearray()
write = sys.stdout.buffer.write
for _ in range(count):
    # the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
    # perfect square
    value = DISCRIMINANT_FACTOR * (int(next(words)) - 1) + 1
    root = isqrt(value)
    answer.extend(b"1 " if root * root == value else b"0 ")
    if len(answer) == OUTPUT_SIZE:
        write(answer)
        answer.clear()
if answer:
    answer[-1] = 10
    write(answer)
else:
    write(b"\n")
