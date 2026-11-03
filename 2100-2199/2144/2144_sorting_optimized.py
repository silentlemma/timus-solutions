import sys

VALUE_BITS = 14
VALUE_MASK = (1 << VALUE_BITS) - 1


def main():
    tokens = (int(word) for line in sys.stdin.buffer for word in line.split())
    n = next(tokens)
    boxes = []
    for _ in range(n):
        count = next(tokens)
        first = previous = next(tokens)
        for _ in range(count - 1):
            value = next(tokens)
            if value < previous:
                print("NO")
                return
            previous = value
        # Each endpoint fits14bits. Both endpoints decide equal-first ties.
        boxes.append((first << VALUE_BITS) | previous)
    del tokens
    boxes.sort()
    last = 0
    for box in boxes:
        if last > box >> VALUE_BITS:
            print("NO")
            return
        last = box & VALUE_MASK
    print("YES")


main()
