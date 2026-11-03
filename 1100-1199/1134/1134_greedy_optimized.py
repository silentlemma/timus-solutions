n, _ = map(int, input().split())
counts = bytearray(n + 1)
valid = True
for value in map(int, input().split()):
    if counts[value] == 2:
        valid = False
        break
    counts[value] += 1

# Card zero is unavailable; afterwards only the previous value can use card x.
occupied = True
if valid:
    for needed in counts:
        needed += occupied - 1
        if needed > 1:
            valid = False
            break
        occupied = needed > 0
# Reserving a right card after processing n would require nonexistent card n+1.
print("YES" if valid and not occupied else "NO")
