from array import array
from sys import stdin

BASE = 10
DIGITS = (1, 2)
MAX_DIGITS = 30
DIVISOR_FIVE = 5


def smallest(modulus):
    if modulus % DIVISOR_FIVE == 0:
        return "Impossible"

    # Zero means unseen; the low bit stores the appended digit minus one.
    parent = array("I", [0]) * modulus
    queue = array("I")
    for digit in DIGITS:
        remainder = digit % modulus
        if parent[remainder] == 0:
            parent[remainder] = ((modulus + 1) << 1) | (digit - 1)
            queue.append(remainder)

    front = 0
    for _ in range(1, MAX_DIGITS):
        end = len(queue)
        if front == end or parent[0]:
            break
        while front < end and not parent[0]:
            previous = queue[front]
            front += 1
            code = (previous + 1) << 1
            for digit in DIGITS:
                remainder = (previous * BASE + digit) % modulus
                if parent[remainder] == 0:
                    parent[remainder] = code | (digit - 1)
                    queue.append(remainder)

    if parent[0] == 0:
        return "Impossible"
    result = []
    remainder = 0
    while remainder != modulus:
        code = parent[remainder]
        result.append("12"[code & 1])
        remainder = (code >> 1) - 1
    return "".join(reversed(result))


print(smallest(int(stdin.buffer.readline())))
