import sys

MOD = 10**9
OPEN, CLOSE = 1, 2  # plugs are brackets: the two ends of one path


def partner(q, k):
    # the bracket matching q[k]: rightwards for an opening one, leftwards otherwise
    step = 1 if q[k] == OPEN else -1
    depth, j = 0, k
    while True:
        if q[j] == q[k]:
            depth += 1
        elif q[j]:
            depth -= 1
        if depth == 0:
            return j
        j += step


def row_moves(width, start, last):
    # run one row of cells over a plug state and return the states it can
    # leave below; p[c] is the left plug of cell c, p[c + 1] its upper plug
    states = {(0,) + start: 1}
    for c in range(width):
        nxt = {}
        for p, ways in states.items():
            left, up = p[c], p[c + 1]

            def put(down, right, q=p, ways=ways):
                q = list(q)
                q[c], q[c + 1] = down, right
                key = tuple(q)
                nxt[key] = nxt.get(key, 0) + ways

            if not left and not up:
                if c + 1 < width and not last:
                    put(OPEN, CLOSE)  # a new path turning right and down
            elif left and up:
                q = list(p)
                if left == OPEN and up == CLOSE:
                    # closing the cycle: only at the very last cell, with nothing else open
                    if last and c == width - 1 and not any(p[:c] + p[c + 2 :]):
                        put(0, 0)
                    continue
                if left == OPEN and up == OPEN:
                    q[partner(q, c + 1)] = OPEN
                elif left == CLOSE and up == CLOSE:
                    q[partner(q, c)] = CLOSE
                put(0, 0, tuple(q))
            else:
                plug = left or up
                if not last:
                    put(plug, 0)
                if c + 1 < width:
                    put(0, plug)
        states = nxt
    return {p[:width]: w for p, w in states.items() if p[width] == 0}


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) % MOD for j in range(n)] for i in range(n)]


def main():
    width, height = (int(x) for x in sys.stdin.read().split())
    # every plug state that a row can leave behind, reached from the empty one
    empty = (0,) * width
    index = {empty: 0}
    order = [empty]
    for s in order:
        for t in row_moves(width, s, False):
            if t not in index:
                index[t] = len(order)
                order.append(t)
    size = len(order)
    step = [[0] * size for _ in range(size)]
    for s in order:
        for t, w in row_moves(width, s, False).items():
            step[index[s]][index[t]] = w % MOD
    # the first height - 1 rows by fast powering, then the last row that closes the cycle
    power = [[int(i == j) for j in range(size)] for i in range(size)]
    e = height - 1
    while e:
        if e & 1:
            power = multiply(power, step)
        step = multiply(step, step)
        e >>= 1
    total = 0
    for s in order:
        closed = row_moves(width, s, True).get(empty, 0)
        total += power[0][index[s]] * closed
    print(2 * total % MOD)  # every cycle can be walked in two directions


main()
