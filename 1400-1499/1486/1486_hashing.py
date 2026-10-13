import sys
from array import array

LETTER_BITS = 5
LETTER_MASK = (1 << LETTER_BITS) - 1
ROW_BITS = 2 * LETTER_BITS
KEY_BITS = 2 * ROW_BITS
TABLE_SIZE = 1 << KEY_BITS
MIX_A = 1000003
MIX_B = 1000033
MIX_C = 1000037
MIX_D = 1000039


def same(grid, first, second, stride, k):
    r1, c1 = divmod(first, stride)
    r2, c2 = divmod(second, stride)
    for t in range(k):
        if grid[r1 + t][c1 : c1 + k] != grid[r2 + t][c2 : c2 + k]:
            return False
    return True


def extend(grid, first, second, stride, best):
    n, m = len(grid), len(grid[0])
    r1, c1 = divmod(first, stride)
    r2, c2 = divmod(second, stride)
    upper = min(n - r1, m - c1, n - r2, m - c2)
    k = best + 1
    if upper < k or grid[r1][c1 : c1 + k] != grid[r2][c2 : c2 + k]:
        return best
    if grid[r1 + best][c1 : c1 + k] != grid[r2 + best][c2 : c2 + k]:
        return best
    t = 0
    while t < upper:
        one, two = grid[r1 + t], grid[r2 + t]
        if one[c1 : c1 + upper] != two[c2 : c2 + upper]:
            low, high = 0, upper
            while low + 1 < high:
                mid = (low + high) // 2
                if one[c1 : c1 + mid] == two[c2 : c2 + mid]:
                    low = mid
                else:
                    high = mid
            # A mismatch leaves the square when either its row or its column is excluded.
            upper = max(t, low)
            if upper <= best:
                return best
        t += 1
    return upper


def single_pair(grid, stride):
    seen = array("i", [-1]) * (1 << LETTER_BITS)
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            key = value & LETTER_MASK
            old = seen[key]
            if old >= 0:
                return 1, (old, r * stride + c)
            seen[key] = r * stride + c
    return 0, None


def solve(grid, n, m):
    stride = m + 1
    total = (n + 1) * stride
    limit = min(n, m) - (n == m)
    if limit < 2:
        return single_pair(grid, stride)
    # Exact two-by-two labels need a direct table, without dictionary entries.
    ranks = array("I", [0]) * total
    table = array("i", [0]) * TABLE_SIZE
    active = array("I")
    best, answer = 0, None
    for r in range(n - 1):
        top, bottom = grid[r], grid[r + 1]
        offset = r * stride
        for c in range(m - 1):
            one = (top[c] & LETTER_MASK) << LETTER_BITS | (top[c + 1] & LETTER_MASK)
            two = (bottom[c] & LETTER_MASK) << LETTER_BITS | (bottom[c + 1] & LETTER_MASK)
            key = one << ROW_BITS | two
            pos = offset + c
            ranks[pos] = key + 1
            old = table[key]
            if old == 0:
                table[key] = pos + 1
            else:
                # A negative representative marks a class already added to the next scan.
                if old > 0:
                    active.append(old - 1)
                    table[key] = -old
                active.append(pos)
                if answer is None:
                    best = extend(grid, abs(old) - 1, pos, stride, 1)
                    answer = (abs(old) - 1, pos)
                    if best == limit:
                        return best, answer
    del table
    if not active:
        return single_pair(grid, stride)

    def refine(k, size, ranks, active, keep):
        count = len(active)
        length = 1
        while length < 2 * count:
            length *= 2
        mask = length - 1
        table = array("i", [0]) * length
        result = array("I", [0]) * total if keep else None
        remaining = array("I") if keep else None
        # Four overlapping corner squares determine the entire larger square exactly.
        d = k - size
        down = d * stride
        diagonal = down + d
        pair = None
        for pos in active:
            r, c = divmod(pos, stride)
            if r + k > n or c + k > m:
                continue
            a, b = ranks[pos], ranks[pos + d]
            cc, dd = ranks[pos + down], ranks[pos + diagonal]
            if not a or not b or not cc or not dd:
                continue
            slot = (a * MIX_A ^ b * MIX_B ^ cc * MIX_C ^ dd * MIX_D) & mask
            # Hash collisions probe another slot; equality always compares all four labels.
            while table[slot]:
                old = abs(table[slot]) - 1
                if (ranks[old] == a and ranks[old + d] == b
                        and ranks[old + down] == cc and ranks[old + diagonal] == dd):
                    break
                slot = (slot + 1) & mask
            old = table[slot]
            if old == 0:
                table[slot] = pos + 1
                if keep:
                    result[pos] = slot + 1
            else:
                pair = (abs(old) - 1, pos)
                if not keep:
                    return pair
                result[pos] = slot + 1
                if old > 0:
                    remaining.append(old - 1)
                    table[slot] = -old
                remaining.append(pos)
        if keep:
            return result, remaining, pair
        return pair

    size = 2
    high = limit + 1
    # Unique squares cannot be corners of any larger repeated square.
    while size * 2 <= limit:
        next_size = size * 2
        result, remaining, pair = refine(next_size, size, ranks, active, True)
        if pair is None:
            del result, remaining
            high = next_size
            break
        ranks, active = result, remaining
        size = next_size
        if size > best:
            best = extend(grid, pair[0], pair[1], stride, size - 1)
            answer = pair
        if best == limit:
            return best, answer
    low = max(best, size)
    while low + 1 < high:
        k = (low + high) // 2
        pair = refine(k, size, ranks, active, False)
        if pair is None:
            high = k
        else:
            best = extend(grid, pair[0], pair[1], stride, k - 1)
            answer = pair
            low = best
    return best, answer


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2 : 2 + n]
    k, pair = solve(grid, n, m)
    if pair is None:
        sys.stdout.write("0\n")
    else:
        r1, c1 = divmod(pair[0], m + 1)
        r2, c2 = divmod(pair[1], m + 1)
        sys.stdout.write(f"{k}\n{r1 + 1} {c1 + 1}\n{r2 + 1} {c2 + 1}\n")


if __name__ == "__main__":
    main()
