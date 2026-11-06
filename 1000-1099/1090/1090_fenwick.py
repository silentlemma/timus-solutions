from sys import stdin

read = stdin.buffer
size, row_count = map(int, read.readline().split())
recruits = (int(token) for line in read for token in line.split())
best_count = -1
best_row = 1
for row in range(1, row_count + 1):
    tree = [0] * (size + 1)
    jumps = 0
    for position in range(size):
        height = next(recruits)
        jumps += position
        prefix = height - 1
        while prefix:
            jumps -= tree[prefix]
            prefix &= prefix - 1
        while height <= size:
            tree[height] += 1
            height += height & -height
    if jumps > best_count:
        best_count = jumps
        best_row = row
print(best_row)
