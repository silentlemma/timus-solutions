import os
from sys import stdout

CHOICES = 3
words = open(0, "rb", buffering=0).read().split()
count = int(words[0])
names = [words[1 + CHOICES * i : 1 + CHOICES * (i + 1)] for i in range(count)]
answer = bytearray()
last = b""
for token in words[1 + CHOICES * count : 1 + (CHOICES + 1) * count]:
    choice = None
    for name in names[int(token) - 1]:
        if name > last and (choice is None or name < choice):
            choice = name
    if choice is None:
        answer = bytearray(b"IMPOSSIBLE\n")
        break
    answer.extend(choice + b"\n")
    last = choice
stdout.buffer.write(answer)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
