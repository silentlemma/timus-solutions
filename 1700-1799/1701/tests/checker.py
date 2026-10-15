"""Checker: an Impossible line must equal the expected one; otherwise
Possible and n salaries with Vasily's 0, all between 0 and 10^9, that
satisfy every statement."""

import sys

MOST = 10 ** 9


class Bad(Exception):
    pass


def check(source, expected, output):
    data = [int(w) for w in open(source).read().split()]
    n, m = data[0], data[1]
    want = open(expected).read().split("\n")[0].strip()
    lines = open(output).read().split("\n")
    first = lines[0].strip()
    if want != "Possible" or first != "Possible":
        if first != want:
            raise Bad("expected %r, got %r" % (want, first))
        return
    salary = [int(w) for w in " ".join(lines[1:]).split()]
    if len(salary) != n:
        raise Bad("%d salaries instead of %d" % (len(salary), n))
    if salary[0] != 0:
        raise Bad("Vasily earns %d" % salary[0])
    if not all(0 <= s <= MOST for s in salary):
        raise Bad("a salary is out of range")
    for k in range(m):
        i, j, d = data[2 + 3 * k:5 + 3 * k]
        if salary[i] - salary[j] != d:
            raise Bad("statement %d fails" % (k + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
