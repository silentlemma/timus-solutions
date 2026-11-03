import sys

SIDE_AREA = 9
ENTRANCE_SIDES = 4
EMPTY = ord(".")

data = sys.stdin.buffer.read().split()
n = int(data[0])
open_rows = [sum((c == EMPTY) << j for j, c in enumerate(row)) for row in data[1 : n + 1]]
seen = [0] * n
front = [0] * n
seen[0] = front[0] = 1
seen[-1] = front[-1] = 1 << (n - 1)
active = 1 | (1 << (n - 1))
# Rows carry disjoint newly reached cells; each cell is enqueued only once.
while active:
    bit = active & -active
    active -= bit
    r = bit.bit_length() - 1
    cells = front[r]
    front[r] = 0
    for q in range(max(0, r - 1), min(n, r + 2)):
        fresh = ((cells << 1) | (cells >> 1)) if q == r else cells
        fresh &= open_rows[q] & ~seen[q]
        if fresh:
            seen[q] |= fresh
            front[q] |= fresh
            active |= 1 << q
sides = 0
for r in range(n):
    sides += (seen[r] & ~(open_rows[r] << 1)).bit_count()
    sides += (seen[r] & ~(open_rows[r] >> 1)).bit_count()
    sides += (seen[r] & ~(open_rows[r - 1] if r else 0)).bit_count()
    sides += (seen[r] & ~(open_rows[r + 1] if r + 1 < n else 0)).bit_count()
print((sides - ENTRANCE_SIDES) * SIDE_AREA)
