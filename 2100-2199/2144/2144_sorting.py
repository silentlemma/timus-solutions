import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pos = 1
    boxes = []
    ok = True
    for _ in range(n):
        k = int(data[pos])
        sizes = list(map(int, data[pos + 1:pos + 1 + k]))
        pos += 1 + k
        if any(a > b for a, b in zip(sizes, sizes[1:])):
            ok = False
        boxes.append((sizes[0], sizes[-1]))
    # Sorting by the first size, and then by the last, gives a valid order if any exists.
    boxes.sort()
    if any(left[1] > right[0] for left, right in zip(boxes, boxes[1:])):
        ok = False
    print("YES" if ok else "NO")


main()
