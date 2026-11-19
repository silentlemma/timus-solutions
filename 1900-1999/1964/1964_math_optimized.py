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
population, count = next(tokens), next(tokens)
common = population
for _ in range(count):
    common -= population - next(tokens)
print(max(0, common))

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
