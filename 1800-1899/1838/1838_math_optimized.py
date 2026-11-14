import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    length = int(tokens[0])
    first = int(tokens[2])
    last = int(tokens[-1])
    min_cut = 2 * first
    max_cut = 2 * last - length
    if max_cut <= min_cut:
        print(length)
        return

    supports = iter(tokens)
    next(supports)
    next(supports)
    left = int(next(supports))
    safe = 0
    for token in supports:
        right = int(token)
        if left >= max_cut:
            break
        if right > min_cut:
            start = max(left, min_cut, 2 * right - length)
            end = min(right, max_cut, 2 * left)
            if end > start:
                safe += end - start
        left = right
    print(length - safe)


if __name__ == "__main__":
    main()
