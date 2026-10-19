import sys

CASE_BIT = 32
UPPER_FIRST = ord("A")
UPPER_LAST = ord("Z")


def solve(n, word):
    answer = [-1] * n
    upper = lower = 0
    pending = []
    for code in word:
        is_upper = UPPER_FIRST <= code <= UPPER_LAST
        index = upper if is_upper else lower
        if is_upper:
            upper += 1
        else:
            lower += 1
        if pending and pending[-1][0] ^ code == CASE_BIT:
            _, previous = pending.pop()
            if is_upper:
                answer[index] = previous
            else:
                answer[previous] = index
        else:
            pending.append((code, index))
    return None if pending else answer


def run(tokens):
    n = int(next(tokens))
    answer = solve(n, next(tokens))
    return "Impossible\n" if answer is None else " ".join(str(v + 1) for v in answer) + "\n"


if __name__ == "__main__":
    sys.stdout.write(run(iter(sys.stdin.buffer.read().split())))
