import sys

# a cost is pegs * PEG + inches cut: fewer pegs first, then less cutting
PEG = 10**6


def clear(shelf, lo, hi, width):
    # cheapest way to get a shelf out of the open strip (lo, hi) of the
    # tome, keeping its plank inside the niche [0, width]
    left, length, a, b = shelf
    if left + length <= lo or left >= hi:
        return 0
    best = 2 * PEG + length
    for start, end in ((0, lo), (hi, width)):
        # pegs stay: a plank of length t in [start, end] over both pegs with
        # its middle between them exists for b - a <= t <= this bound
        if start <= a and b <= end:
            longest = min(length, 2 * (b - start), end - start, 2 * (end - a))
            if longest >= b - a:
                best = min(best, length - longest)
        # one peg moves anywhere, so only the kept peg and the room matter
        if end > start and (start <= a <= end or start <= b <= end):
            best = min(best, PEG + max(0, length - (end - start)))
    return best


def carry(shelf, x, tome, width):
    # cost of making a shelf hold the tome over [x, x + tome], or None
    left, length, a, b = shelf
    if length < tome:
        return None
    # pegs stay: limits on the new left end, doubled to stay in integers
    low = max(0, 2 * (b - length), 2 * a - length, 2 * (x + tome - length))
    high = min(2 * a, 2 * x, 2 * b - length, 2 * (width - length))
    if low <= high:
        return 0
    # one peg moves: the plank only has to reach over the tome and the
    # peg that stays
    if any(max(x + tome, p) - min(x, p) <= length for p in (a, b)):
        return PEG
    return None


def main():
    data = iter(map(int, sys.stdin.read().split()))
    width, height = next(data), next(data)
    tome_w, tome_h = next(data), next(data)
    n = next(data)
    shelves = []
    for _ in range(n):
        y, left, length = next(data), next(data), next(data)
        x1, x2 = next(data), next(data)
        shelves.append((y, (left, length, left + x1, left + x2)))
    shelves.sort()
    spots = width - tome_w + 1
    # prefix[k][x]: total cost of clearing the strip at x from the k lowest
    # shelves
    prefix = [[0] * spots]
    for _, shelf in shelves:
        row = prefix[-1]
        prefix.append([row[x] + clear(shelf, x, x + tome_w, width) for x in range(spots)])
    best = None
    for i, (y, shelf) in enumerate(shelves):
        if y + tome_h > height:
            continue
        # the shelves strictly between the tome bottom and top are in the way
        top = i + 1
        while top < n and shelves[top][0] < y + tome_h:
            top += 1
        for x in range(spots):
            base = carry(shelf, x, tome_w, width)
            if base is not None:
                total = base + prefix[top][x] - prefix[i + 1][x]
                if best is None or total < best:
                    best = total
    print(best // PEG, best % PEG)


main()
