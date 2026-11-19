import os
from sys import stdout

READ_CHUNK = 4096
SPACE = 32


def words():
    pending = b""
    while True:
        block = os.read(0, READ_CHUNK)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > SPACE else b""
        yield from parts
    if pending:
        yield pending


tokens = map(int, words())
count = next(tokens)
prefix = [0]
for _ in range(count):
    prefix.append(prefix[-1] + next(tokens))
first, second = next(tokens) - 1, next(tokens) - 1
if first == second:
    own = prefix[first + 1] - prefix[first]
    score = own + max(prefix[first], prefix[-1] - prefix[first + 1])
elif first < second:
    score = prefix[(first + second) // 2 + 1]
else:
    score = prefix[-1] - prefix[(first + second + 1) // 2]
print(score, prefix[-1] - score)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
