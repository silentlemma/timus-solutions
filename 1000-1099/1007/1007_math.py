import sys


def restore(s, n):
    """Undo at most one change: the sum of the positions (from 1) of the ones
    of a sent word is divisible by n + 1."""
    mod = n + 1
    w = sum(i for i, c in enumerate(s, 1) if c == "1")
    if len(s) == n:
        # a raised zero at position p adds exactly p to the weight
        p = w % mod
        return s if p == 0 else s[: p - 1] + "0" + s[p:]
    # ones_after: ones to the right of the changed place; they shift by one
    ones_after = 0
    if len(s) == n - 1:
        for i in range(len(s), -1, -1):
            if (w + ones_after) % mod == 0:
                return s[:i] + "0" + s[i:]
            if (w + ones_after + i + 1) % mod == 0:
                return s[:i] + "1" + s[i:]
            if i > 0 and s[i - 1] == "1":
                ones_after += 1
    else:
        for i in range(len(s) - 1, -1, -1):
            one = s[i] == "1"
            if (w - ones_after - one * (i + 1)) % mod == 0:
                return s[:i] + s[i + 1 :]
            ones_after += one
    return s


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    sys.stdout.write("".join(restore(s, n) + "\n" for s in data[1:]))


main()
