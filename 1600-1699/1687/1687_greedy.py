import sys


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    k = data[1]
    boxes, pos = [], 2
    for _ in range(k):
        size = data[pos]
        boxes.append(data[pos + 1:pos + 1 + size])
        pos += 1 + size
    wanted = set(data[pos + 1:pos + 1 + data[pos]])
    useful = [i for i in range(k) if wanted.intersection(boxes[i])]
    coverable = wanted.intersection(c for i in useful for c in boxes[i])
    # no set of boxes is worth more than all coverable coins, nor holds more
    # than all useful boxes; one box per coverable coin reaches every coin,
    # so the answer is min(useful, coverable): those boxes, then any others
    picked = []
    covered = set()
    for coin in sorted(coverable):
        if coin not in covered:
            box = next(i for i in useful if coin in boxes[i])
            picked.append(box)
            covered.update(boxes[box])
    chosen = set(picked)
    for i in useful:
        if len(picked) < len(coverable) and i not in chosen:
            picked.append(i)
    print(len(picked))
    print(" ".join(str(i + 1) for i in sorted(picked)))


main()
