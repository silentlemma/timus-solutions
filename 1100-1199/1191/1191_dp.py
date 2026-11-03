from sys import stdin

values = list(map(int, stdin.read().split()))
gap = values[0]
needed = 1
# Reverse the floor maps: ceil(needed/k)*k is the least earlier surviving gap.
while len(values) > 2:
    interval = values.pop()
    needed = (needed + interval - 1) // interval * interval
    if needed > gap:
        print("YES")
        break
else:
    print("NO")
