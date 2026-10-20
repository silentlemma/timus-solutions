import sys
from collections import deque


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    count = next(tokens)
    lower = next(tokens)
    upper = next(tokens)
    values = list(tokens)

    unreachable = count + 1
    best = [unreachable] * (count + 1)
    best[0] = 0
    upper_left = lower_left = 0
    upper_product = lower_product = 1
    lower_bound = lower - 1
    candidates = deque()
    next_cut = 0

    for index, value in enumerate(values):
        if value > upper:
            upper_left = index + 1
            upper_product = 1
        else:
            # Divide first so that the stored product never exceeds the bound.
            limit = upper // value
            while upper_product > limit:
                upper_product //= values[upper_left]
                upper_left += 1
            upper_product *= value

        if value > lower_bound:
            lower_left = index + 1
            lower_product = 1
        else:
            limit = lower_bound // value
            while lower_product > limit:
                lower_product //= values[lower_left]
                lower_left += 1
            lower_product *= value

        # Valid previous cuts form [upper_left, lower_left).
        while next_cut < lower_left:
            if best[next_cut] != unreachable:
                while candidates and best[candidates[-1]] >= best[next_cut]:
                    candidates.pop()
                candidates.append(next_cut)
            next_cut += 1
        while candidates and candidates[0] < upper_left:
            candidates.popleft()
        if candidates:
            best[index + 1] = best[candidates[0]] + 1

    print(-1 if best[count] == unreachable else best[count])


if __name__ == "__main__":
    main()
