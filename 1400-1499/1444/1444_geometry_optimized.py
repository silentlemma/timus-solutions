import sys

MAX_COORD = 1000
MAX_DENOMINATOR = 4 * MAX_COORD
SCALE = MAX_DENOMINATOR * MAX_DENOMINATOR
HALF_TURN = 2 * SCALE
FULL_TURN = 4 * SCALE
DISTANCE_BITS = 12
ID_BITS = 15
KEY_SHIFT = DISTANCE_BITS + ID_BITS
ID_MASK = (1 << ID_BITS) - 1

read = sys.stdin.buffer.readline
n = int(read())
ox, oy = map(int, read().split())
keys = []
for identity in range(2, n + 1):
    x, y = map(int, read().split())
    dx, dy = x - ox, y - oy
    distance = abs(dx) + abs(dy)
    if dy > 0 or (dy == 0 and dx > 0):
        rank = (distance - dx) * SCALE // distance
    else:
        rank = HALF_TURN + (distance + dx) * SCALE // distance
    keys.append((rank << KEY_SHIFT) | (distance << ID_BITS) | identity)
keys.sort()
start = 0
previous = keys[-1] >> KEY_SHIFT
for index, key in enumerate(keys):
    current = key >> KEY_SHIFT
    gap = current - previous
    if gap < 0:
        gap += FULL_TURN
    if gap >= HALF_TURN:
        start = index
    previous = current
out = [str(n), "1"]
for index in range(start, len(keys)):
    out.append(str(keys[index] & ID_MASK))
for index in range(start):
    out.append(str(keys[index] & ID_MASK))
sys.stdout.write("\n".join(out) + "\n")
