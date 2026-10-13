import sys

COMMANDS = 4
BLOCK = 4  # commands applied at once
DEDUP_EVERY = 4  # blocks between removals of repeated cells


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    cells = n * m
    # go[k][c]: the cell reached from cell c by command k, cells numbered by rows
    go = []
    pos = 2
    for _ in range(COMMANDS):
        pairs = data[pos : pos + 2 * cells]
        pos += 2 * cells
        go.append([(int(r) - 1) * m + int(c) - 1 for r, c in zip(pairs[::2], pairs[1::2])])
    s = int(data[pos])
    commands = [int(k) - 1 for k in data[pos + 1 : pos + 1 + s]]
    # two commands in a row as one table, and four as one table built from
    # two pairs when that block first occurs: a quarter of the steps
    pair = [[[b[c] for c in a] for b in go] for a in go]
    quads = {}
    cur = list(range(cells))  # the cells the player may stand on
    whole = s - s % BLOCK
    for i in range(0, whole, BLOCK):
        a, b, c, d = commands[i : i + BLOCK]
        code = ((a * COMMANDS + b) * COMMANDS + c) * COMMANDS + d
        to = quads.get(code)
        if to is None:
            second = pair[c][d]
            to = quads[code] = [second[x] for x in pair[a][b]]
        cur = [to[x] for x in cur]
        if i // BLOCK % DEDUP_EVERY == 0:
            cur = list(set(cur))
    for k in commands[whole:]:
        to = go[k]
        cur = [to[c] for c in cur]
    cur = sorted(set(cur))
    out = ["%d" % len(cur)]
    out += ["%d %d" % (c // m + 1, c % m + 1) for c in cur]
    sys.stdout.write("\n".join(out) + "\n")


main()
