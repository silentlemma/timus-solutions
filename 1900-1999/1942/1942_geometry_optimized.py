import math
import sys

SCALE = 1000
FRACTION_DIGITS = 3


def residue(token):
    fraction = token.partition(b".")[2]
    value = int((fraction + b"000")[:FRACTION_DIGITS])
    return (-value if token.startswith(b"-") else value) % SCALE


def main():
    lines = sys.stdin.buffer
    size = int(lines.readline().strip().lstrip(b"+0") or b"0")
    keys = []
    for _ in range(size):
        x, y = lines.readline().split()
        keys.append(residue(x) * SCALE + residue(y))
    keys.sort()
    best_count = best_norm = first = 0
    while first < size:
        key = keys[first]
        end = first + 1
        while end < size and keys[end] == key:
            end += 1
        count = end - first
        if count >= best_count:
            x, y = divmod(key, SCALE)
            dx, dy = min(x, SCALE - x), min(y, SCALE - y)
            norm = dx * dx + dy * dy
            if count > best_count or norm < best_norm:
                best_count, best_norm = count, norm
        first = end
    print(f"{best_count} {math.sqrt(best_norm) / SCALE:.9f}")


if __name__ == "__main__":
    main()
