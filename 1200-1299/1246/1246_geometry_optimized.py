import os
import sys

READ_CHUNK = 65536
SPACE = 32


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


tokens = integers()
count = next(tokens)
first_x, first_y = previous_x, previous_y = next(tokens), next(tokens)
twice_area = 0
for _ in range(1, count):
    x, y = next(tokens), next(tokens)
    twice_area += previous_x * y - x * previous_y
    previous_x, previous_y = x, y
twice_area += previous_x * first_y - first_x * previous_y
print("ccw" if twice_area > 0 else "cw")

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
