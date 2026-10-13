import sys

CANS = 3


def main():
    cap = list(map(int, sys.stdin.read().split()))
    size = [c + 1 for c in cap]

    # a state (x, y, z) as one number; every move leaves some can empty or full
    def code(v):
        return (v[0] * size[1] + v[1]) * size[2] + v[2]

    seen = bytearray(size[0] * size[1] * size[2])
    start = (0, 0, 0)
    seen[code(start)] = 1
    queue = [start]
    volumes = set()
    for v in queue:
        x, y, z = v
        volumes.update((x, y, z, x + y, x + z, y + z, x + y + z))
        nexts = []
        for i in range(CANS):
            if v[i] < cap[i]:  # fill can i from the pump up to the brim
                w = list(v)
                w[i] = cap[i]
                nexts.append(w)
            for j in range(CANS):
                if i != j and v[i] and v[j] < cap[j]:  # pour i into j
                    move = min(v[i], cap[j] - v[j])
                    w = list(v)
                    w[i] -= move
                    w[j] += move
                    nexts.append(w)
        for w in nexts:
            k = code(w)
            if not seen[k]:
                seen[k] = 1
                queue.append(tuple(w))
    volumes.discard(0)
    print(len(volumes))


main()
