import sys

FIRST = ord("a")
LAST = ord("z")
FREE = ord("?")


def solve(pattern, limit):
    fixed = set(pattern)
    fixed.discard(FREE)
    needed = max(0, limit - len(fixed))
    holes = pattern.count(b"?")
    if holes < needed:
        return False
    negative = pattern[1::2].count(b"?")
    positive = holes - negative

    missing = [letter for letter in range(FIRST, LAST + 1) if letter not in fixed]
    low, high = [0], [0]
    for a, z in zip(missing, reversed(missing)):
        low.append(low[-1] + a - FIRST)
        high.append(high[-1] + LAST - z)
    choices = range(max(0, needed - negative), min(needed, positive) + 1)
    take = min(choices, key=lambda count: high[count] + low[needed - count])

    left, right = 0, len(missing)
    negative = needed - take
    for i, letter in enumerate(pattern):
        if letter != FREE:
            continue
        if i % 2 == 0:
            if take:
                take -= 1
                right -= 1
                pattern[i] = missing[right]
            else:
                pattern[i] = LAST
        elif negative:
            negative -= 1
            pattern[i] = missing[left]
            left += 1
        else:
            pattern[i] = FIRST
    return True


def main():
    read = sys.stdin.buffer.readline
    pattern = bytearray(read().strip())
    limit = int(read())
    output = sys.stdout.buffer
    if solve(pattern, limit):
        output.write(pattern)
        output.write(b"\n")
    else:
        output.write(b"-1\n")


if __name__ == "__main__":
    main()
