SIDE = 4
HALF = SIDE // 2

counts = [0] * SIDE
for row in range(SIDE):
    colours = input().split()
    first = (row // HALF) * HALF
    counts[first] += colours[:HALF].count("1")
    counts[first + 1] += colours[HALF:].count("1")
# A target quadrant costs4-count[target]+count[opposite]. Minimize both pairs.
print(SIDE - max(abs(counts[0] - counts[-1]), abs(counts[1] - counts[2])))
