import sys

INFINITY = 1 << 60


def solve(cost, plants):
    n = len(cost)
    best = [INFINITY] * n
    used = [False] * n
    for vertex in plants:
        best[vertex] = 0
    answer = 0
    for _ in range(n):
        vertex = min((best[v], v) for v in range(n) if not used[v])[1]
        answer += best[vertex]
        used[vertex] = True
        for neighbor, price in enumerate(cost[vertex]):
            if not used[neighbor] and price < best[neighbor]:
                best[neighbor] = price
    return answer


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = next(tokens), next(tokens)
    plants = [next(tokens) - 1 for _ in range(k)]
    cost = [[next(tokens) for _ in range(n)] for _ in range(n)]
    print(solve(cost, plants))


if __name__ == "__main__":
    main()
