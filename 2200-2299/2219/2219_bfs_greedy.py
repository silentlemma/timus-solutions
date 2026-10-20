import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, k = next(data), next(data), next(data)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = next(data) - 1, next(data) - 1
        graph[u].append(v)
        graph[v].append(u)
    cups = sorted(data, reverse=True)

    states = 2 * n
    distance = [-1] * states
    distance[0] = 0
    queue = [0]
    for state in queue:
        parity = (state & 1) ^ 1
        length = distance[state] + 1
        for v in graph[state // 2]:
            neighbor = 2 * v + parity
            if distance[neighbor] == -1:
                distance[neighbor] = length
                queue.append(neighbor)

    suffix = [[-1] * (k + 1) for _ in range(2)]
    for i in range(k - 1, -1, -1):
        suffix[0][i] = suffix[0][i + 1]
        suffix[1][i] = suffix[1][i + 1]
        suffix[cups[i] & 1][i] = cups[i]

    needed = [-1] * states
    needed[0] = 0
    next_distance = [2, 1]
    smallest = [-1, -1]
    total = 0
    for count, cup in enumerate(cups, 1):
        total += cup
        smallest[cup & 1] = cup
        parity = total & 1
        best = [-1, -1]
        best[parity] = total
        # Changing the prefix parity needs only one exchange across its boundary.
        for removed in range(2):
            added = suffix[removed ^ 1][count]
            if smallest[removed] != -1 and added != -1:
                best[parity ^ 1] = max(best[parity ^ 1], total - smallest[removed] + added)
        for p in range(2):
            length = next_distance[p]
            while length < states and length <= best[p]:
                needed[length] = count
                length += 2
            next_distance[p] = length

    answers = []
    for v in range(n):
        answer = -1
        for parity in range(2):
            length = distance[2 * v + parity]
            if length != -1:
                count = needed[length]
                if count != -1 and (answer == -1 or count < answer):
                    answer = count
        answers.append(str(answer))
    sys.stdout.write(" ".join(answers) + "\n")


if __name__ == "__main__":
    main()
