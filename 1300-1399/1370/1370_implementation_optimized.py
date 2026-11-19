import os
import sys

READ_CHUNK = 65536
SPACE = 32
ZERO = 48


def integers():
    pending = b""
    while True:
        block = os.read(0, READ_CHUNK)
        if not block:
            break
        data = pending + block
        words = data.split()
        if data[-1] > SPACE:
            pending = words.pop()
        else:
            pending = b""
        for word in words:
            yield int(word)
    if pending:
        yield int(pending)


WINDOW = 10
tokens = integers()
count, clicks = next(tokens), next(tokens)
start = clicks % count
visible = bytearray(WINDOW)
for index in range(count):
    digit = next(tokens)
    offset = (index - start) % count
    if offset < WINDOW:
        visible[offset] = digit + ZERO
print(visible.decode("ascii"))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
