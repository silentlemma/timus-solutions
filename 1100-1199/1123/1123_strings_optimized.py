import os
from sys import stdout

original = open(0, "rb", buffering=0).read().strip().lstrip(b"0") or b"0"
digits = bytearray(original)
size = len(digits)
for at in range(size // 2):
    digits[size - 1 - at] = digits[at]
if digits < original:
    at = (size - 1) // 2
    while digits[at] == ord("9"):
        digits[at] = digits[size - 1 - at] = ord("0")
        at -= 1
    digits[at] += 1
    digits[size - 1 - at] = digits[at]
stdout.buffer.write(digits + b"\n")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
