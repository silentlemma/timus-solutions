import sys

BASE = 10


def construct(old, flags, offset):
    n = len(old)
    stride = n + 1
    identifiers = [-1] * (2 * n * stride)
    keys = [2 * n]
    identifiers[keys[0]] = 0
    rows = []
    for key in keys:
        normal, previous = divmod(key // 2, stride)
        row = []
        for digit in range(BASE):
            next_normal = old[normal][digit]
            if digit:
                next_previous = old[normal][digit - 1]
            else:
                next_previous = n if previous == n else old[previous][BASE - 1]
            if digit >= offset:
                accepted = flags[old[normal][digit - offset]]
            elif previous != n:
                accepted = flags[old[previous][digit + BASE - offset]]
            else:
                accepted = 0
            target = 2 * (next_normal * stride + next_previous) + accepted
            if identifiers[target] < 0:
                identifiers[target] = len(keys)
                keys.append(target)
            row.append(identifiers[target])
        rows.append(row)
    return rows, [key & 1 for key in keys]


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    offset, n = next(tokens), next(tokens)
    flags = [next(tokens) for _ in range(n)]
    old = [[next(tokens) - 1 for _ in range(BASE)] for _ in range(n)]
    rows, flags = construct(old, flags, offset)
    output = ["Success", str(len(rows)), " ".join(map(str, flags))]
    output.extend(" ".join(str(target + 1) for target in row) for row in rows)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
