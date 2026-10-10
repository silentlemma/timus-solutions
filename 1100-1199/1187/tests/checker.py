"""Checker: every line must match the table rebuilt here from the input,
except the percents, which only have to be right-aligned in 6 characters,
round the exact percent down or up (exact ones stay as they are), be 100%
in the totals, be '-' exactly where the total is zero, and add up to 100
along each row and down each column without the totals."""

import sys

WIDTH = 6
FULL = 100


def fail(reason):
    print(reason)
    sys.exit(1)


def parse_input(text):
    lines = text.replace("\r", "").split("\n")
    survey, at, questions = lines[0], 1, []
    while lines[at] != "#":
        if lines[at].startswith(" "):
            questions[-1][2].append((lines[at][1], lines[at]))
        else:
            questions.append((lines[at][:3], lines[at], []))
        at += 1
    at += 1
    results = []
    while lines[at] != "#":
        results.append(lines[at])
        at += 1
    at += 1
    tables = []
    while at < len(lines) and lines[at] != "#":
        tables.append((lines[at][:3], lines[at][4:7], lines[at][8:]))
        at += 1
    return survey, questions, results, tables


def read_percents(line, wanted, where):
    # the percent cells of a line, None for '-'
    if len(line) != WIDTH * (wanted + 1) or line[:WIDTH].strip():
        fail("%s: bad layout" % where)
    out = []
    for k in range(wanted):
        cell = line[WIDTH * (k + 1) : WIDTH * (k + 2)]
        text = cell.strip()
        if cell != text.rjust(WIDTH):
            fail("%s: cell not aligned" % where)
        if text == "-":
            out.append(None)
        elif text.endswith("%") and text[:-1].isdigit() and str(int(text[:-1])) == text[:-1]:
            out.append(int(text[:-1]))
        else:
            fail("%s: bad percent %r" % (where, text))
    return out


def check_vector(got, values, total, where):
    # percents of the parts of total: '-' if total is zero, else each one a
    # rounding of the exact value, together 100
    if total == 0:
        if any(p is not None for p in got):
            fail("%s: percents where the total is zero" % where)
        return
    for p, v in zip(got, values):
        if p is None:
            fail("%s: a missing percent" % where)
        low = FULL * v // total
        if not (p == low or (p == low + 1 and FULL * v % total)):
            fail("%s: %d%% is not a rounding of %d/%d" % (where, p, v, total))
    if sum(got) != FULL:
        fail("%s: percents add up to %d" % (where, sum(got)))


def main():
    inp, _, output = sys.argv[1:4]
    survey, questions, results, tables = parse_input(open(inp).read())
    place = {q[0]: k for k, q in enumerate(questions)}
    got = open(output).read().replace("\r", "").split("\n")
    while got and got[-1] == "":
        got.pop()
    at = 0

    def expect(text, what):
        nonlocal at
        if at >= len(got) or got[at] != text:
            fail("line %d: expected %s %r" % (at + 1, what, text))
        at += 1

    for t, (c1, c2, name) in enumerate(tables):
        if t:
            expect("", "a blank line")
        first, second = questions[place[c1]], questions[place[c2]]
        rows, cols = [a[0] for a in first[2]], [a[0] for a in second[2]]
        count = [[0] * len(cols) for _ in rows]
        for line in results:
            count[rows.index(line[place[c1]])][cols.index(line[place[c2]])] += 1
        expect("%s - %s" % (survey, name), "the title")
        for q in (first, second):
            expect(q[1], "the question")
            for a in q[2]:
                expect(a[1], "the answer")
        expect("", "a blank line")
        heads = ["%s:%s" % (c2, c) for c in cols] + ["TOTAL"]
        expect(" " * WIDTH + "".join(h.rjust(WIDTH) for h in heads), "the headings")
        table = [r + [sum(r)] for r in count]
        table.append([sum(c) for c in zip(*table)])
        labels = ["%s:%s" % (c1, r) for r in rows] + ["TOTAL"]
        n = len(cols) + 1
        by_row, by_col = [], []
        for k, label in enumerate(labels):
            expect(label.rjust(WIDTH) + "".join(str(v).rjust(WIDTH) for v in table[k]), "values")
            for store in (by_row, by_col):
                if at >= len(got):
                    fail("the output ends early")
                store.append(read_percents(got[at], n, "line %d" % (at + 1)))
                at += 1
        for k, r in enumerate(table):
            where = "table %d, row %s" % (t + 1, labels[k])
            check_vector(by_row[k][:-1], r[:-1], r[-1], where)
            if by_row[k][-1] != (FULL if r[-1] else None):
                fail("%s: the total should be 100%% or -" % where)
        for j in range(n):
            column = [table[i][j] for i in range(len(table))]
            mine = [by_col[i][j] for i in range(len(table))]
            where = "table %d, column %d" % (t + 1, j + 1)
            check_vector(mine[:-1], column[:-1], column[-1], where)
            if mine[-1] != (FULL if column[-1] else None):
                fail("%s: the total should be 100%% or -" % where)
    if at != len(got):
        fail("extra output")


if __name__ == "__main__":
    main()
