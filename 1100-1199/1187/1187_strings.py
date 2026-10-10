import sys

WIDTH = 6
# question codes are three characters long
CODE = 3
FULL = 100


def shares(values, total):
    # percents of total that round each value down or up and add up to 100:
    # round all down, then raise the ones with the largest remainders
    if total == 0:
        return None
    low = [FULL * v // total for v in values]
    rest = [FULL * v % total for v in values]
    for k in sorted(range(len(values)), key=lambda k: -rest[k])[: FULL - sum(low)]:
        low[k] += 1
    return low


def cells(items):
    return "".join(str(x).rjust(WIDTH) for x in items)


def percents(column):
    return ["-" if p is None else "%d%%" % p for p in column]


def main():
    lines = sys.stdin.read().replace("\r", "").split("\n")
    survey = lines[0]
    at = 1
    # each question: its code, its own line and its answers as (code, line)
    questions = []
    while lines[at] != "#":
        if lines[at].startswith(" "):
            questions[-1][2].append((lines[at][1], lines[at]))
        else:
            questions.append((lines[at][:CODE], lines[at], []))
        at += 1
    at += 1
    results = []
    while lines[at] != "#":
        results.append(lines[at])
        at += 1
    at += 1
    place = {q[0]: k for k, q in enumerate(questions)}
    out = []
    while at < len(lines) and lines[at] != "#":
        first, second = (
            questions[place[lines[at][:CODE]]],
            questions[place[lines[at][CODE + 1 : 2 * CODE + 1]]],
        )
        name = lines[at][2 * CODE + 2 :]
        at += 1
        rows, cols = [a[0] for a in first[2]], [a[0] for a in second[2]]
        count = [[0] * len(cols) for _ in rows]
        for line in results:
            count[rows.index(line[place[first[0]]])][cols.index(line[place[second[0]]])] += 1
        row_total = [sum(r) for r in count]
        col_total = [sum(c) for c in zip(*count)]
        total = sum(row_total)
        # percents along each row and down each column, the totals included
        # as one more column and one more row
        table = [r + [s] for r, s in zip(count, row_total)] + [col_total + [total]]
        lines_n, cols_n = len(table), len(cols) + 1
        by_row = []
        for r in table:
            part = shares(r[:-1], r[-1])
            by_row.append([None] * cols_n if part is None else part + [FULL])
        by_col = [[None] * cols_n for _ in range(lines_n)]
        for j in range(cols_n):
            part = shares([table[i][j] for i in range(lines_n - 1)], table[-1][j])
            if part is not None:
                for i in range(lines_n):
                    by_col[i][j] = part[i] if i < lines_n - 1 else FULL
        if out:
            out.append("")
        out.append("%s - %s" % (survey, name))
        for q in (first, second):
            out.append(q[1])
            out += [a[1] for a in q[2]]
        out.append("")
        heads = ["%s:%s" % (second[0], c) for c in cols] + ["TOTAL"]
        out.append(" " * WIDTH + cells(heads))
        labels = ["%s:%s" % (first[0], r) for r in rows] + ["TOTAL"]
        for k, label in enumerate(labels):
            out.append(label.rjust(WIDTH) + cells(table[k]))
            out.append(" " * WIDTH + cells(percents(by_row[k])))
            out.append(" " * WIDTH + cells(percents(by_col[k])))
    print("\n".join(out))


main()
