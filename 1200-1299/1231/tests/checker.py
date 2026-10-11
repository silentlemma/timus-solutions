"""Checker: the output must be a Turing machine table that, for the k of the
input and every n from 1 to 200, crosses out all minuses but the one the
counting rhyme leaves, within 1 000 000 steps, and halts on that minus. The
machine starts in state 1 on the leftmost of n minuses, the rest of the tape
holds '#', and it halts when no row matches its state and symbol.
"""

import sys

MAX_N = 200
MAX_STEPS = 1000000
MAX_ROWS = 10000
MAX_STATE = 30000
SIDE = 5000
WRITABLE = set("+#ABCDEFGHIJKLMNOPQRSTUVWXYZ")
MOVES = {"<": -1, "=": 0, ">": 1}


class Bad(Exception):
    pass


def read_table(text):
    lines = text.split("\n")
    first = lines[0].split()
    if len(first) != 1 or not first[0].isdigit():
        raise Bad("the first line must be the number of rows")
    p = int(first[0])
    if not 1 < p < MAX_ROWS:
        raise Bad("the table has %d rows" % p)
    rows = [line.rstrip("\r") for line in lines[1:]]
    while rows and not rows[-1].strip():
        rows.pop()
    if len(rows) != p:
        raise Bad("expected %d rows, found %d" % (p, len(rows)))
    table = {}
    for i, row in enumerate(rows):
        parts = row.split(" ")
        if len(parts) != 5 or any(len(x) != 1 for x in (parts[1], parts[3], parts[4])):
            raise Bad("row %d is not five single-space separated items" % (i + 1))
        state, read, nxt, write, move = parts
        if not (state.isdigit() and nxt.isdigit()):
            raise Bad("row %d: states must be integers" % (i + 1))
        state, nxt = int(state), int(nxt)
        if not (1 <= state <= MAX_STATE and 1 <= nxt <= MAX_STATE):
            raise Bad("row %d: state out of range" % (i + 1))
        if move not in MOVES:
            raise Bad("row %d: bad move %r" % (i + 1, move))
        if write not in WRITABLE and not (write == "-" and read == "-"):
            raise Bad("row %d: cannot write %r" % (i + 1, write))
        if (state, read) in table:
            raise Bad("two rows for state %d and symbol %r" % (state, read))
        table[(state, read)] = (nxt, write, MOVES[move])
    return table


def survivor(n, k):
    pos = 0
    for m in range(1, n + 1):
        pos = (pos + k) % m
    return pos


def run(table, n, k):
    tape = ["#"] * (2 * SIDE + 1)
    for i in range(n):
        tape[SIDE + i] = "-"
    head, state = SIDE, 1
    for _ in range(MAX_STEPS + 1):
        step = table.get((state, tape[head]))
        if step is None:
            break
        state, write, move = step
        if SIDE <= head < SIDE + n and write not in "-+":
            raise Bad("n=%d: writes %r over a minus cell" % (n, write))
        tape[head] = write
        head += move
        if not 0 <= head < len(tape):
            raise Bad("n=%d: the head leaves the tape" % n)
    else:
        raise Bad("n=%d: more than %d steps" % (n, MAX_STEPS))
    left = [i for i in range(n) if tape[SIDE + i] == "-"]
    want = survivor(n, k)
    if left != [want]:
        raise Bad("n=%d: minuses left at %s, expected only %d" % (n, left[:5], want + 1))
    if head != SIDE + want:
        raise Bad("n=%d: the head stops off the remaining minus" % n)


def main():
    inp, _, output = sys.argv[1:4]
    k = int(open(inp).read().split()[0])
    try:
        table = read_table(open(output).read())
        for n in range(1, MAX_N + 1):
            run(table, n, k)
    except Bad as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
