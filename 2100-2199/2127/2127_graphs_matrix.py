import sys

MOD = 998244353
CYCLE_PERIOD = 4


def determinant(matrix):
    size = len(matrix)
    answer = 1
    for column in range(size):
        pivot = column
        while pivot < size and matrix[pivot][column] == 0:
            pivot += 1
        if pivot == size:
            return 0
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            answer = -answer
        row = matrix[column]
        value = row[column]
        answer = answer * value % MOD
        inverse = pow(value, MOD - 2, MOD)
        for below in range(column + 1, size):
            target = matrix[below]
            if target[column] == 0:
                continue
            factor = target[column] * inverse % MOD
            for right in range(column + 1, size):
                target[right] = (target[right] - factor * row[right]) % MOD
    return answer


def solve():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    m = next(data)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(data) - 1
        v = next(data) - 1
        graph[u].append(v)
        graph[v].append(u)
    del data

    degree = [len(neighbors) for neighbors in graph]
    active = bytearray([1]) * n
    leaves = [v for v in range(n) if degree[v] <= 1]
    answer = 1
    while leaves:
        u = leaves.pop()
        if not active[u]:
            continue
        if degree[u] == 0:
            return 0
        for v in graph[u]:
            if active[v]:
                break
        # A leaf forces its edge into every contributing permutation.
        active[u] = active[v] = 0
        answer = -answer
        for w in graph[v]:
            if active[w]:
                degree[w] -= 1
                if degree[w] <= 1:
                    leaves.append(w)

    branches = [v for v in range(n) if active[v] and degree[v] > 2]
    branch_count = len(branches)
    index = [-1] * n
    for i, v in enumerate(branches):
        index[v] = i
    capacity = 2 * branch_count
    matrix = [[0] * capacity for _ in range(capacity)]
    size = branch_count
    seen = bytearray(n)
    for u in branches:
        start = index[u]
        for neighbor in graph[u]:
            if not active[neighbor] or seen[neighbor]:
                continue
            if index[neighbor] >= 0:
                if u < neighbor:
                    end = index[neighbor]
                    matrix[start][end] += 1
                    matrix[end][start] += 1
                continue
            previous, current = u, neighbor
            internal = 0
            while degree[current] == 2:
                seen[current] = 1
                internal += 1
                for following in graph[current]:
                    if active[following] and following != previous:
                        break
                previous, current = current, following
            end = index[current]
            sign = -1 if (internal // 2) % 2 else 1
            answer *= sign
            # Eliminate pairs inside a path, retaining one vertex if needed.
            if internal % 2 == 0:
                matrix[start][end] += sign
                matrix[end][start] += sign
            else:
                if size == capacity:
                    return 0
                matrix[start][size] += sign
                matrix[size][start] += sign
                matrix[end][size] += 1
                matrix[size][end] += 1
                size += 1

    for root in range(n):
        if not active[root] or index[root] >= 0 or seen[root]:
            continue
        previous, current = -1, root
        length = 0
        while not seen[current]:
            seen[current] = 1
            length += 1
            for following in graph[current]:
                if active[following] and following != previous:
                    break
            previous, current = current, following
        if length % 2:
            answer = answer * 2 % MOD
        elif length % CYCLE_PERIOD == 0:
            return 0
        else:
            answer = -CYCLE_PERIOD * answer % MOD

    matrix = [[value % MOD for value in row[:size]] for row in matrix[:size]]
    return answer * determinant(matrix) % MOD


if __name__ == "__main__":
    print(solve())
