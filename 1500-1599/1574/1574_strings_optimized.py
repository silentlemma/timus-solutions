import os
import sys

BLOCK_SIZE = 4096
OPEN = ord("(")
CLOSE = ord(")")


def main():
    balance = lowest = count = 0
    for block in iter(lambda: sys.stdin.buffer.read(BLOCK_SIZE), b""):
        for bracket in block:
            if bracket == OPEN:
                balance += 1
            elif bracket == CLOSE:
                balance -= 1
            else:
                continue
            if balance < lowest:
                lowest, count = balance, 1
            elif balance == lowest:
                count += 1
    print(count if balance == 0 else 0)
    sys.stdout.flush()
    os._exit(0)


main()
