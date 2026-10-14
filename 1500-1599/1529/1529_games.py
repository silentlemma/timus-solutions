import sys
from array import array
from itertools import compress, product
from operator import itemgetter

LANE = "H"  # values fit in 16 bits: a value never exceeds the number of options
BYTE = 8
FLIP = bytes([1, 0]) + bytes(254)  # turns 0 into 1 and 1 into 0


def legal_cuts(d, factor):
    """Cuts c (from 1) of an edge of length d >= 2 that leave a nonempty
    piece coprime with d. The end cuts leave d - 1, always coprime, and as
    gcd(d - c, d) = gcd(c, d), a middle cut fails only when both c - 1 and c
    share a factor with d."""
    shared = bytearray(d)  # shared[x]: x has a common factor with d
    rest = d
    while rest > 1:
        p = factor[rest]
        shared[0::p] = b"\x01" * len(range(0, d, p))
        while rest % p == 0:
            rest //= p
    mask = int.from_bytes(shared, "little")
    failing = (mask & (mask >> BYTE)).to_bytes(d, "little")  # byte c - 1 for cut c
    return list(compress(range(1, d + 1), failing.translate(FLIP)))


def orderings(box):
    """The distinct orderings of the edges of a box."""
    if not box:
        yield ()
        return
    for i, first in enumerate(box):
        if i == 0 or first != box[i - 1]:
            for rest in orderings(box[:i] + box[i + 1 :]):
                yield (first,) + rest


def option_values(rows, dims, cuts):
    """The XOR over all parts for every tuple of cuts, as rows of lanes.
    rows holds the values of the parts by piece lengths, one array along
    the last axis for each prefix, prefixes in order. A cut c of an edge d
    joins the pieces c - 1 and d - c: on the last axis that is lane c - 1 of
    the row and of the reversed row, on the others two whole rows."""
    packed = [
        int.from_bytes(r.tobytes(), "little") ^ int.from_bytes(r[::-1].tobytes(), "little")
        for r in rows
    ]
    sizes = list(dims[:-1])
    for axis in reversed(range(len(sizes))):
        inner = 1
        for s in sizes[axis + 1 :]:
            inner *= s
        d = sizes[axis]
        out = []
        for start in range(0, len(packed), d * inner):
            for c in cuts[axis]:
                low, high = start + (c - 1) * inner, start + (d - c) * inner
                out.extend(packed[low + j] ^ packed[high + j] for j in range(inner))
        packed = out
        sizes[axis] = len(cuts[axis])
    width = dims[-1] * array(LANE).itemsize
    lanes = [c - 1 for c in cuts[-1]]
    pick = itemgetter(*lanes) if len(lanes) > 1 else (lambda row: (row[lanes[0]],))
    for value in packed:
        row = array(LANE)
        row.frombytes(value.to_bytes(width, "little"))
        yield pick(row)


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    edges = [int(x) for x in data[1 : 1 + k]]
    if k == 1:
        # pieces of a segment of length d total d - 1, so by induction its
        # value is d mod 2, and from an odd length every cut wins
        if edges[0] % 2:
            print(1)
            print(1)
        else:
            print(2)
        return
    if 1 in edges:
        # any cut empties a box with an edge of 1, so Alice cuts and wins
        print(1)
        print(" ".join(["1"] * k))
        return
    # every ordering of a box's edges is stored with the same value, indexed
    # by a mixed radix over the sorted edges of the whole box
    bound = sorted(edges)
    radix = [1] * k
    for i in range(k - 2, -1, -1):
        radix[i] = radix[i + 1] * (bound[i + 1] + 1)
    grundy = array(LANE, bytes(array(LANE).itemsize * radix[0] * (bound[0] + 1)))
    longest = max(bound)
    factor = list(range(longest + 1))  # the smallest prime factor
    for p in range(2, longest + 1):
        if p * p > longest:
            break
        if factor[p] == p:
            for q in range(p * p, longest + 1, p):
                if factor[q] == q:
                    factor[q] = p
    cuts_of = {d: legal_cuts(d, factor) for d in range(2, longest + 1)}
    boxes = [b for b in product(*(range(1, e + 1) for e in bound)) if list(b) == sorted(b)]
    boxes.sort(key=sum)
    for box in boxes:
        if box[0] == 1:
            g = 1
        elif not all(cuts_of[d] for d in box):
            g = 0  # no legal cut
        else:
            rows = []
            for prefix in product(*(range(d) for d in box[:-1])):
                base = sum(x * r for x, r in zip(prefix, radix))
                rows.append(grundy[base : base + box[-1]])
            seen = set()
            for row in option_values(rows, box, [cuts_of[d] for d in box]):
                seen.update(row)
            g = 0
            while g in seen:
                g += 1
        # only orderings within the bounds are ever looked up
        for perm in orderings(box):
            if all(x <= e for x, e in zip(perm, bound)):
                grundy[sum(x * r for x, r in zip(perm, radix))] = g
    if grundy[sum(x * r for x, r in zip(bound, radix))] == 0:
        print(2)
        return

    # the first winning cut in lexicographic order, in the input's order
    def value(x):
        return grundy[sum(v * r for v, r in zip(sorted(x), radix))]

    rows = [
        array(LANE, [value(p + (x,)) for x in range(edges[-1])])
        for p in product(*(range(d) for d in edges[:-1]))
    ]
    cuts = [cuts_of[d] for d in edges]
    values = [v for row in option_values(rows, edges, cuts) for v in row]
    for move, v in zip(product(*cuts), values):
        if v == 0:
            print(1)
            print(" ".join(map(str, move)))
            return


main()
