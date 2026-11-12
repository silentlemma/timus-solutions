from functools import cache
from sys import stdin


@cache
def fold(text):
    best = text
    size = len(text)
    for split in range(1, size):
        candidate = fold(text[:split]) + fold(text[split:])
        if len(candidate) < len(best):
            best = candidate

    for period in range(1, size // 2 + 1):
        repeats, remainder = divmod(size, period)
        unit = text[:period]
        if remainder == 0 and unit * repeats == text:
            candidate = f"{repeats}({fold(unit)})"
            if len(candidate) < len(best):
                best = candidate
    return best


print(fold(stdin.read().strip()))
