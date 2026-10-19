import math
import sys

SMALL_SENDER = 5
BASE = 6
BOARD_SIZE = 7
POWER_OF_TWO = 8
POWER_OF_THREE = 9
SECOND_PRIME = 3


def solve(sender, target):
    if target <= sender:
        return sender - target, [sender, target]
    if target % sender == 0:
        return 0, [sender, target]

    # One paid step must connect a multiple of sender to a divisor of target.
    for divisor in range(1, math.isqrt(target) + 1):
        if target % divisor:
            continue
        for receiver in (divisor, target // divisor):
            for before in (receiver - 1, receiver + 1):
                if before >= sender and before % sender == 0:
                    return 1, [sender, before, receiver, target]

    if sender <= SMALL_SENDER:
        before = target // sender * sender
        if target - before > before + sender - target:
            before += sender
        return 2, [sender, before, target]

    remainder = target
    for prime in (2, SECOND_PRIME):
        while remainder % prime == 0:
            remainder //= prime
    if remainder > 1:
        before = remainder - 1 if remainder % BASE == 1 else remainder + 1
        return 2, [sender, BASE, before, remainder, target]
    if target % BASE == 0:
        return 2, [sender, BASE, target]
    if target % POWER_OF_TWO == 0:
        return 2, [sender, POWER_OF_TWO, target]
    if sender == BOARD_SIZE:
        return 2, [sender, POWER_OF_THREE, target]
    return 2, [sender, SMALL_SENDER, 10, POWER_OF_THREE, target]


def main():
    sender, target = map(int, sys.stdin.buffer.read().split())
    cost, route = solve(sender, target)
    path = []
    for employee in route:
        if not path or path[-1] != employee:
            path.append(employee)
    print(cost)
    print(len(path))
    print(*path)


if __name__ == "__main__":
    main()
