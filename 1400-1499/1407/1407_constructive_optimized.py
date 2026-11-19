import os
from sys import stdout

BASE = 10
count = int(open(0, "rb", buffering=0).read())
value, place, bit = 0, 1, 1
digits = bytearray()
for _ in range(count):
    # place / bit is odd, so this bit decides which digit preserves divisibility.
    digit = 1 if value & bit else 2
    value += digit * place
    digits.append(ord("0") + digit)
    place *= BASE
    bit <<= 1
digits.reverse()
stdout.buffer.write(digits + b"\n")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
