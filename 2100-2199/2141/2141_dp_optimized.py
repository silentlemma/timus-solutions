import sys

BLOCK_SIZE = 65536
SPACE = ord(" ")


def integers():
    pending = b""
    while True:
        block = sys.stdin.buffer.read(BLOCK_SIZE)
        if not block:
            if pending:
                yield int(pending)
            return
        data = pending + block
        cut = len(data)
        # A token may cross a block boundary, including just after its minus.
        while cut and data[cut - 1] > SPACE:
            cut -= 1
        pending = data[cut:]
        yield from map(int, data[:cut].split())


values = integers()
n = next(values)
plus, minus = next(values), 0
best = plus if plus > 0 else 0
for _ in range(n - 1):
    value = next(values)
    next_plus = value + (minus if minus > 0 else 0)
    minus = plus - value
    plus = next_plus
    if plus > best:
        best = plus
    if minus > best:
        best = minus
print(best)
