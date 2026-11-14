from array import array
from itertools import accumulate
from sys import stdin

BLOCK_SIZE = 1 << 15


def numbers():
    pending = b""
    while block := stdin.buffer.read(BLOCK_SIZE):
        fields = (pending + block).split()
        pending = fields.pop() if fields and not block[-1:].isspace() else b""
        yield from map(int, fields)
    if pending:
        yield int(pending)


def main():
    values = numbers()
    floors, _ = next(values), next(values)
    if floors == 1:
        print(-1)
        return
    # Index each gap by the floor above it, starting at index zero.
    difference = array("i", [0]) * floors
    for left, right in zip(values, values):
        difference[left - 1] += 1
        difference[right - 1] -= 1
    # The final entry is beyond the last gap.
    difference.pop()
    print(min(accumulate(difference)))


if __name__ == "__main__":
    main()
