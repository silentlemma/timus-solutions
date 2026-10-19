from itertools import permutations
import sys

LOCAL_LIMIT = 5


def wins(first, second):
    first, second = tuple(first), tuple(second)
    seen = set()
    while first and second:
        state = first, second
        if state in seen:
            return False
        seen.add(state)
        x, y = first[0], second[0]
        first, second = first[1:], second[1:]
        if x > y:
            first += (y, x)
        elif y > x:
            second += (x, y)
    return bool(first)


def construct(opponent):
    size = min(len(opponent), LOCAL_LIMIT)
    local = tuple(opponent[:size])
    for candidate in permutations(sorted(local)):
        if wins(candidate, local):
            return list(candidate) + opponent[size:]
    return None


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    answer = construct(data[1:])
    if answer is None:
        print("NO")
    else:
        print("YES")
        print(*answer)
