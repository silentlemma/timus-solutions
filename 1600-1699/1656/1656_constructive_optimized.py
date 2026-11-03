MIN_HEIGHT = 170
MAX_HEIGHT = 200
SIDES = 4

n = int(input())
counts = [0] * (MAX_HEIGHT - MIN_HEIGHT + 1)
for _ in range(n * n):
    counts[int(input()) - MIN_HEIGHT] += 1

heights = bytearray(n * n)
position = 0
for height in range(MAX_HEIGHT, MIN_HEIGHT - 1, -1):
    for _ in range(counts[height - MIN_HEIGHT]):
        heights[position] = height
        position += 1
middle = n // 2
offset = [0] * n
total = 0
for rank in range(n):
    offset[rank] = total
    if rank == 0:
        total += 1
    elif rank <= middle:
        total += SIDES * rank
    else:
        total += SIDES * (n - rank)

# Every outward step increases rank; each rank consumes a consecutive height range.
for row in range(n):
    for column in range(n):
        rank = abs(row - middle) + abs(column - middle)
        if column:
            print(" ", end="")
        print(heights[offset[rank]], end="")
        offset[rank] += 1
    print()
