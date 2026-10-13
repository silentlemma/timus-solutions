import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    weights = sorted(int(x) for x in data[1 : n + 1])
    record = data[n + 1]
    other = {"L": "R", "R": "L"}
    # the weights in use always form a block of the sorted list whose
    # neighbours stand on opposite pans, so the pan of the largest one wins,
    # and a change adds a new largest weight, any other step a new smallest
    changes = sum(1 for a, b in zip(record, record[1:]) if a != b)
    low = high = n - 1 - changes
    side = {low: record[0]}
    out = ["%d %s" % (weights[low], record[0])]
    for prev, cur in zip(record, record[1:]):
        if cur != prev:
            high += 1
            side[high] = other[side[high - 1]]
            out.append("%d %s" % (weights[high], side[high]))
        else:
            low -= 1
            side[low] = other[side[low + 1]]
            out.append("%d %s" % (weights[low], side[low]))
    print("\n".join(out))


main()
