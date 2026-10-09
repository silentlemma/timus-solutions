"""Checker: a solution always exists, so the output must start with the
line "There is solution:", every following line must be a transversal
(a permutation of 1..2N+1, entry s being the column in row s), and after
all of them are applied the table must have at most 2N plus signs."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = open(inp).read().split()
    n = 2 * int(tok[0]) + 1
    table = [[c == "+" for c in row] for row in tok[1 : 1 + n]]
    lines = [line.split() for line in open(output).read().split("\n")]
    lines = [line for line in lines if line]
    if not lines or " ".join(lines[0]) != "There is solution:":
        fail('expected "There is solution:"')
    for number, line in enumerate(lines[1:], 2):
        try:
            cols = [int(x) for x in line]
        except ValueError:
            fail("line %d is not a list of integers" % number)
        if sorted(cols) != list(range(1, n + 1)):
            fail("line %d is not a transversal" % number)
        for row, col in enumerate(cols):
            table[row][col - 1] = not table[row][col - 1]
    plus = sum(map(sum, table))
    if plus > n - 1:
        fail("%d plus signs remain, more than %d" % (plus, n - 1))


main()
