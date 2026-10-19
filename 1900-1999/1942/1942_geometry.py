from array import array
import math
import sys

SCALE = 1000
FRACTION_DIGITS = 3


def scaled(token):
    negative = token[:1] == b"-"
    if token[:1] in (b"-", b"+"):
        token = token[1:]
    _, _, fraction = token.partition(b".")
    value = int((fraction + b"000")[:FRACTION_DIGITS])
    return -value if negative else value


def best_group(points):
    counts = array("i", [0]) * (SCALE * SCALE)
    best_count = 0
    best_norm = 0
    for x, y in points:
        rx, ry = x % SCALE, y % SCALE
        code = rx * SCALE + ry
        counts[code] += 1
        count = counts[code]
        dx, dy = min(rx, SCALE - rx), min(ry, SCALE - ry)
        norm = dx * dx + dy * dy
        if count > best_count or (count == best_count and norm < best_norm):
            best_count, best_norm = count, norm
    return best_count, best_norm


if __name__ == "__main__":
    words = iter(sys.stdin.buffer.read().split())
    size = int(next(words).lstrip(b"+0") or b"0")
    points = ((scaled(next(words)), scaled(next(words))) for _ in range(size))
    count, norm = best_group(points)
    print(f"{count} {math.sqrt(norm) / SCALE:.9f}")
