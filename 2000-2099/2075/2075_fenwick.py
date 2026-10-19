import sys

ENDLESS = 1 << 62


def main():
    data = sys.stdin.buffer.read().split(b"\n")
    n = int(data[0])
    events = [line.split() for line in data[1:n + 1]]
    names = sorted({e[1] for e in events if e[1] not in (b"Oleg", b"fire")})
    index = {name: i for i, name in enumerate(names)}
    m = len(names)
    # layers in order of names (the densest at the bottom), with a Fenwick tree of heights
    tree = [0] * (m + 1)
    height = [0] * m
    top = 1
    while top * 2 <= m:
        top *= 2

    def add(i, delta):
        height[i] += delta
        i += 1
        while i <= m:
            tree[i] += delta
            i += i & -i

    def layer_at(h):
        # the layer that contains level h, and how much of it lies above h
        pos, step = 0, top
        while step:
            if pos + step <= m and tree[pos + step] <= h:
                pos += step
                h -= tree[pos]
            step >>= 1
        return pos, height[pos] - h

    total = straw = clock = 0
    drinking = False
    sips = []  # [from, to, layer], neighbours of one liqueur merged

    def drink(amount):
        nonlocal total, clock
        while amount > 0 and total > straw:
            layer, above = layer_at(straw)
            take = min(above, amount)
            add(layer, -take)
            total -= take
            amount -= take
            if sips and sips[-1][2] == layer and sips[-1][1] == clock:
                sips[-1][1] = clock + take
            else:
                sips.append([clock, clock + take, layer])
            clock += take

    for e in events:
        t = int(e[0])
        if drinking:
            drink(t - clock)
            # running dry before this moment stops him; running dry exactly now does not
            # matter: a pour lets him go on, and Oleg or fire set the state anyway
            drinking = clock == t
        clock = t
        if e[1] == b"Oleg":
            straw = int(e[2])
            drinking = True
        elif e[1] == b"fire":
            drinking = False
        else:
            h = int(e[2])
            add(index[e[1]], h)
            total += h
    if drinking:
        drink(ENDLESS)
    out = ["%d-%d %s" % (a, b, names[k].decode()) for a, b, k in sips]
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
