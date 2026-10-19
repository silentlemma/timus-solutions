import sys

DIGITS = [
    "._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
    "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|",
]
COLUMNS = [0, 4, 10, 14]  # where the four digits start
WIDTH = 3
SECONDS = 60  # MM:SS runs from 00:00 to 59:59
TOP = SECONDS * SECONDS


def fits(shown, digit):
    # every lit segment must belong to the digit
    return all(c == "." or c == d for c, d in zip(shown, DIGITS[digit]))


def main():
    lines = sys.stdin.read().split()
    n = int(lines[0])
    out = []
    previous = TOP
    for r in range(n):
        rows = lines[1 + WIDTH * r:1 + WIDTH * (r + 1)]
        cells = ["".join(row[c:c + WIDTH] for row in rows) for c in COLUMNS]
        ok = [[fits(cell, d) for d in range(10)] for cell in cells]
        # the largest time that fits and stays below the previous one leaves the
        # most room for the rest, so it never spoils a solution
        value = previous - 1
        while True:
            m, s = divmod(value, SECONDS)
            if all(ok[k][d] for k, d in enumerate((m // 10, m % 10, s // 10, s % 10))):
                break
            value -= 1
        out.append("%02d:%02d" % (m, s))
        previous = value
    print("\n".join(out))


main()
