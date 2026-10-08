import sys
from itertools import permutations

FACES = 6
# quarter turns around the vertical and the left-right axes: the new face at
# position i is the old face at position TURNS[t][i]
TURNS = ((3, 5, 2, 1, 4, 0), (0, 1, 5, 2, 3, 4))


def rotations():
    seen, todo = {tuple(range(FACES))}, [tuple(range(FACES))]
    while todo:
        p = todo.pop()
        for turn in TURNS:
            r = tuple(p[i] for i in turn)
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return seen


def main():
    rots = rotations()
    # all 720 dice, each mapped to the smallest of its rotations
    key = {}
    for die in permutations(range(1, FACES + 1)):
        key[die] = min(tuple(die[i] for i in r) for r in rots)
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    values = list(map(int, data[1 : 1 + FACES * n]))
    groups = {}
    for d in range(n):
        k = key[tuple(values[FACES * d : FACES * (d + 1)])]
        groups.setdefault(k, []).append(d + 1)
    # dicts keep the order of first appearance
    out = [str(len(groups))]
    out += [" ".join(map(str, g)) for g in groups.values()]
    sys.stdout.write("\n".join(out) + "\n")


main()
