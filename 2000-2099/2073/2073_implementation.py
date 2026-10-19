import sys

NAME_WIDTH = 30
DATE_WIDTH = 8
LETTERS = "ABCDEFGHIJKLM"


def main():
    lines = [line.strip() for line in sys.stdin.read().split("\n")]
    pos = 0

    def next_line():
        nonlocal pos
        pos += 1
        return lines[pos - 1]

    border = "+%s+%s+%s+" % ("-" * NAME_WIDTH, "-" * DATE_WIDTH, "-" * len(LETTERS))
    out = [border, "|%s|%s|%s|" % ("Contest name".ljust(NAME_WIDTH), "Date".ljust(DATE_WIDTH),
                                   LETTERS), border]
    for _ in range(int(next_line())):
        name, date = next_line(), next_line()
        p, s = map(int, next_line().split())
        # '.' for a given problem, 'x' once submitted, 'o' once accepted
        marks = ["."] * p + [" "] * (len(LETTERS) - p)
        for _ in range(s):
            submit = next_line()
            i = LETTERS.index(submit[0])
            if submit[2:] == "Accepted":
                marks[i] = "o"
            elif marks[i] != "o":
                marks[i] = "x"
        out.append("|%s|%s|%s|" % (name.ljust(NAME_WIDTH), date, "".join(marks)))
        out.append(border)
    print("\n".join(out))


main()
