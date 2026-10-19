import sys
from collections import deque


def solve(locations, claims):
    n = len(locations)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if locations[i] != locations[j] and claims[i] & claims[j]:
                graph[i].append(j)
                graph[j].append(i)
    color = [-1] * n
    answer = []
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        sides = [[], []]
        pending = deque([start])
        while pending:
            vertex = pending.popleft()
            sides[color[vertex]].append(vertex)
            for target in graph[vertex]:
                if color[target] == -1:
                    color[target] = color[vertex] ^ 1
                    pending.append(target)
        answer.extend(sides[0] if len(sides[0]) <= len(sides[1]) else sides[1])
    return answer or [0]


def run(tokens):
    n = int(next(tokens))
    locations = []
    claims = []
    for i in range(n):
        locations.append(next(tokens))
        mask = 1 << i
        for _ in range(int(next(tokens))):
            mask |= 1 << (int(next(tokens)) - 1)
        claims.append(mask)
    answer = solve(locations, claims)
    return str(len(answer)) + "\n" + " ".join(str(v + 1) for v in answer) + "\n"


if __name__ == "__main__":
    sys.stdout.write(run(iter(sys.stdin.buffer.read().split())))
