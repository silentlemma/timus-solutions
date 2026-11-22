import os
from sys import stdin, stdout

KEYS = (b"abc", b"def", b"ghi", b"jkl", b"mno", b"pqr", b"stu", b"vwx", b"yz", b".,!", b" ")
BYTE_VALUES = 256
weights = bytearray(BYTE_VALUES)
for key in KEYS:
    for presses, letter in enumerate(key, 1):
        weights[letter] = presses
text = stdin.buffer.readline()
print(sum(text.translate(bytes(weights))))
stdout.flush()
os._exit(0)
