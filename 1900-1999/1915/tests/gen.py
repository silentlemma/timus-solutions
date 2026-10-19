"""seed mode:1 small random,2 push/pop,3 periodic output,4 copy storm,
5 empty copies,6 alternating,7 wrapping blocks,8 shrinking-cap replacement,
9 nonbinary period,10 no output,11 extreme values,12 late push,13 tiny cap,
14 random million. Modes2..14 use exactly one million valid operations.
"""

import random
import sys

MAX_OPERATIONS = 1000000
MAX_COIN = 1000000000
SMALL_LENGTH = 200
SMALL_HEIGHT = 2000
PUSH_POP = 2
PERIODIC = 3
COPY_STORM = 4
EMPTY_COPIES = 5
ALTERNATING = 6
WRAPPING = 7
SHRINKING = 8
NONBINARY = 9
NO_OUTPUT = 10
EXTREME = 11
LATE_PUSH = 12
TINY_CAP = 13
RANDOM_MAX = 14
PERIOD_LENGTH = 8
LONG_PERIOD = 1000
DOUBLINGS = 20


def make_case(seed, mode):
    rng = random.Random(seed)
    count = SMALL_LENGTH if mode == 1 else MAX_OPERATIONS
    if mode in (1, RANDOM_MAX):
        operations = []
        height = 0
        for _ in range(count):
            choices = [1, 0, -1] if height else [1, 0]
            operation = rng.choice(choices)
            if operation > 0:
                operation = rng.randint(1, MAX_COIN)
                height += 1
            elif operation == -1:
                height -= 1
            else:
                bound = SMALL_HEIGHT if mode == 1 else MAX_OPERATIONS
                if height > bound:
                    operation = -1
                    height -= 1
                else:
                    height *= 2
            operations.append(operation)
        return operations
    if mode == PUSH_POP:
        return list(range(1, count // 2 + 1)) + [-1] * (count // 2)
    if mode in (PERIODIC, NONBINARY):
        period = PERIOD_LENGTH if mode == PERIODIC else LONG_PERIOD
        prefix = list(range(MAX_COIN - period + 1, MAX_COIN + 1)) + [0] * DOUBLINGS
        return prefix + [-1] * (count - len(prefix))
    if mode == COPY_STORM:
        return [MAX_COIN] + [0] * (count - 2) + [-1]
    if mode == EMPTY_COPIES:
        return [0] * (count - 2) + [MAX_COIN, -1]
    if mode == ALTERNATING:
        return [MAX_COIN, -1] * (count // 2)
    if mode == WRAPPING:
        block = [1, 2, 0, -1, 3, 0] + [-1] * PERIOD_LENGTH
        copies, padding = divmod(count, len(block))
        return block * copies + [0] * padding
    if mode == SHRINKING:
        prefix = [1, 2, 3, 4] + [0] * DOUBLINGS
        pairs, padding = divmod(count - len(prefix), 2)
        return prefix + [-1, MAX_COIN] * pairs + [0] * padding
    if mode == NO_OUTPUT:
        return [MAX_COIN] * count
    if mode == EXTREME:
        return [MAX_COIN, 1] * (count // 4) + [-1] * (count // 2)
    if mode == LATE_PUSH:
        return [1] + [0] * (count - 3) + [MAX_COIN, -1]
    if mode == TINY_CAP:
        return [rng.randint(1, MAX_COIN) for _ in range(count - 1)] + [-1]
    raise ValueError("unknown generator mode")


def main():
    operations = make_case(int(sys.argv[1]), int(sys.argv[2]))
    print(len(operations))
    sys.stdout.write("\n".join(map(str, operations)) + "\n")


if __name__ == "__main__":
    main()
