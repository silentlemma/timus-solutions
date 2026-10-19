"""Certify the full shifted decimal language using a finite arithmetic product."""

from collections import deque
from pathlib import Path
import sys

BASE = 10
STATE_LIMIT = 25600


def certify(old, old_flags, new, flags, offset):
    n, size = len(old), len(new)
    zero_seen = bytearray(size)
    zero = 0
    while not zero_seen[zero]:
        zero_seen[zero] = 1
        for digit in range(offset):
            if flags[new[zero][digit]]:
                return False, "a number below the offset is accepted"
        zero = new[zero][0]
    seen = bytearray(2 * n * size)
    seen[0] = 1
    queue = deque([0])
    visited = 0
    while queue:
        pair, difference = divmod(queue.popleft(), 2)
        new_state, old_state = divmod(pair, n)
        visited += 1
        for digit in range(BASE):
            final_digit = digit + offset - BASE * difference
            if 0 <= final_digit < BASE:
                if old_flags[old[old_state][digit]] != flags[new[new_state][final_digit]]:
                    return False, "shifted languages differ"
        if difference == 0:
            for digit in range(BASE):
                next_old = old[old_state][digit]
                target = 2 * (new[new_state][digit] * n + next_old)
                if not seen[target]:
                    seen[target] = 1
                    queue.append(target)
                if digit + 1 < BASE:
                    target = 2 * (new[new_state][digit + 1] * n + next_old) + 1
                    if not seen[target]:
                        seen[target] = 1
                        queue.append(target)
        else:
            target = 2 * (new[new_state][0] * n + old[old_state][BASE - 1]) + 1
            if not seen[target]:
                seen[target] = 1
                queue.append(target)
    return True, {"product_states": visited, "candidate_states": size}


def judge(old, old_flags, offset, output):
    tokens = output.split()
    if not tokens or tokens[0] != "Success":
        return False, "a valid bounded automaton always exists"
    try:
        data = list(map(int, tokens[1:]))
    except ValueError:
        return False, "noninteger automaton field"
    if not data or not 1 <= data[0] <= STATE_LIMIT:
        return False, "invalid state count"
    size = data[0]
    if len(data) != 1 + size + BASE * size:
        return False, "wrong number of automaton fields"
    flags = data[1 : 1 + size]
    if flags[0] or any(value not in (0, 1) for value in flags):
        return False, "invalid terminal flags or accepting initial state"
    targets = data[1 + size :]
    if any(not 1 <= value <= size for value in targets):
        return False, "transition outside state range"
    rows = [[value - 1 for value in targets[i : i + BASE]] for i in range(0, len(targets), BASE)]
    return certify(old, old_flags, rows, flags, offset)


def main():
    data = list(map(int, Path(sys.argv[1]).read_text().split()))
    offset, size = data[:2]
    flags = data[2 : 2 + size]
    values = data[2 + size :]
    old = [[value - 1 for value in values[i : i + BASE]] for i in range(0, len(values), BASE)]
    passed, detail = judge(old, flags, offset, Path(sys.argv[3]).read_text())
    print("ok" if passed else detail)
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
