"""Checker: at most 100 lines, CALL X with 1 <= X <= 99 on every line but
the last, which is the only BELL&RET. A call to the same or an earlier
cell never returns, so every call must point forward; then the bells
made from cell i are bells(X) + bells(i + 1), the stack never holds more
than the nesting of calls, and the program must ring exactly K times."""

import sys

CELLS = 100


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    k = int(open(inp).read().split()[0])
    lines = [line.split() for line in open(output).read().splitlines() if line.strip()]
    if not lines or len(lines) > CELLS:
        fail("expected 1 to 100 commands")
    if lines[-1] != ["BELL&RET"]:
        fail("the last command must be BELL&RET")
    last = len(lines) - 1
    targets = []
    for cell, words in enumerate(lines[:-1]):
        if len(words) != 2 or words[0] != "CALL" or not words[1].isdigit():
            fail("cell %d: expected CALL X" % cell)
        x = int(words[1])
        if not 1 <= x <= CELLS - 1 or not cell < x <= last:
            fail("cell %d: CALL %d does not point forward into the program" % (cell, x))
        targets.append(x)
    bells, depth = [0] * (last + 1), [0] * (last + 1)
    bells[last] = 1
    for cell in range(last - 1, -1, -1):
        x = targets[cell]
        bells[cell] = bells[x] + bells[cell + 1]
        depth[cell] = max(depth[x] + 1, depth[cell + 1])
    if depth[0] > CELLS:
        fail("the stack would hold %d return addresses" % depth[0])
    if bells[0] != k:
        fail("%d bells instead of %d" % (bells[0], k))


if __name__ == "__main__":
    main()
