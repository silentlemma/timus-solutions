from sys import stdin


PIGEON_WIDTH = 5
half = int(stdin.buffer.readline()) // 2
row = stdin.buffer.readline()
left = row.count(b"<")
# Each pair of opposite target patterns differs from half by the same amount.
halves = abs(2 * row.count(b"<", 0, half * PIGEON_WIDTH) - left)
alternating = abs(2 * row[:: 2 * PIGEON_WIDTH].count(b"<") - left)
print(half - max(halves, alternating))
