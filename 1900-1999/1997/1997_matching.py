import sys
from collections import deque


def solve(a, b, records):
    enters = [time for time, direction in records if direction == 0]
    exits = [time for time, direction in records if direction == 1]
    if len(enters) != len(exits):
        return None
    count = len(enters)
    edges = [
        [j for j, out in enumerate(exits) if out > entry and (out - entry <= b or out - entry >= a)]
        for entry in enters
    ]
    left = [-1] * count
    right = [-1] * count
    total = 0
    while True:
        distances = [-1] * count
        queue = deque()
        for u in range(count):
            if left[u] == -1:
                distances[u] = 0
                queue.append(u)
        shortest = count + 1
        while queue:
            u = queue.popleft()
            if distances[u] >= shortest:
                continue
            for v in edges[u]:
                mate = right[v]
                if mate == -1:
                    shortest = distances[u] + 1
                elif distances[mate] == -1:
                    distances[mate] = distances[u] + 1
                    queue.append(mate)
        if shortest == count + 1:
            break
        cursor = [0] * count

        def augment(u):
            while cursor[u] < len(edges[u]):
                v = edges[u][cursor[u]]
                cursor[u] += 1
                mate = right[v]
                if (mate == -1 and distances[u] + 1 == shortest) or (
                    mate != -1 and distances[mate] == distances[u] + 1 and augment(mate)
                ):
                    left[u] = v
                    right[v] = u
                    return True
            distances[u] = -1
            return False

        for u in range(count):
            if left[u] == -1 and augment(u):
                total += 1
    if total != count:
        return None
    return [(entry, exits[left[u]]) for u, entry in enumerate(enters)]


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    a, b, count = next(tokens), next(tokens), next(tokens)
    records = [(next(tokens), next(tokens)) for _ in range(count)]
    answer = solve(a, b, records)
    if answer is None:
        print("Liar")
    else:
        print("No reason")
        print("\n".join(f"{start} {end}" for start, end in answer))


if __name__ == "__main__":
    main()
