"""Checker: when the expected answer is IMPOSSIBLE the output must say so
too; otherwise it must list all N * N squares of the board, each once,
as a letter a.. and a number 1.., every square a knight move from the
one before it."""

import sys

LETTERS = "abcdefgh"
KNIGHT = {1, 2}


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    expected = open(ans).read().split()
    got = open(output).read().split()
    if expected == ["IMPOSSIBLE"]:
        if got != ["IMPOSSIBLE"]:
            fail("expected IMPOSSIBLE")
        return
    if len(got) != n * n:
        fail("expected %d squares, got %d words" % (n * n, len(got)))
    squares = []
    for word in got:
        if len(word) != 2 or word[0] not in LETTERS[:n] or not word[1].isdigit():
            fail("bad square %r" % word)
        c, r = LETTERS.index(word[0]), int(word[1]) - 1
        if not 0 <= r < n:
            fail("bad square %r" % word)
        squares.append((c, r))
    if len(set(squares)) != n * n:
        fail("a square is visited twice")
    for (c1, r1), (c2, r2) in zip(squares, squares[1:]):
        if {abs(c1 - c2), abs(r1 - r2)} != KNIGHT:
            fail("not a knight move: %s%d to %s%d" % (LETTERS[c1], r1 + 1, LETTERS[c2], r2 + 1))


if __name__ == "__main__":
    main()
