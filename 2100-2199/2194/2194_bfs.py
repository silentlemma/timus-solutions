import sys
from collections import deque

FACES = 6  # a six lets the player roll again in the same turn


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    jump = [0, 0] + data[1:n - 1] + [0]
    # land[i]: where the token rests after arriving at i and following snakes
    land = list(range(n + 1))
    for i in range(2, n):
        if jump[i]:
            land[i] = land[i - jump[i]]

    # turns holds the fewest turns begun when the token is about to roll at a
    # cell, and a six keeps the turn going at weight 0 while other rolls cost 1
    infinity = n + 1
    turns = [infinity] * (n + 1)
    turns[1] = 1
    queue = deque([1])
    best = infinity
    while queue:
        cell = queue.popleft()
        current = turns[cell]
        if current >= best:
            continue
        for face in range(1, FACES + 1):
            target = land[min(cell + face, n)]
            if target == n:
                best = min(best, current)
                continue
            cost = current if face == FACES else current + 1
            if cost < turns[target]:
                turns[target] = cost
                if face == FACES:
                    queue.appendleft(target)
                else:
                    queue.append(target)
    print(best if best < infinity else -1)


main()
