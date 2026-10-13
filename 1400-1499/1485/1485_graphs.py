import sys

WIN = 3
DRAW = 1


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    n = data[0]
    said = [data[1 + i * n : 1 + (i + 1) * n] for i in range(n)]

    # 2-SAT on "captain i tells the truth" (literal 2i) or lies (2i + 1),
    # and i scored against j exactly when the literal of statement (i, j) holds
    def literal(i, j):
        return 2 * i if said[i][j] == 1 else 2 * i + 1

    graph = [[] for _ in range(2 * n)]
    for i in range(n):
        for j in range(i + 1, n):
            if said[i][j] >= 0 and said[j][i] >= 0:
                # somebody scores in every match: a or b, so not a -> b
                a, b = literal(i, j), literal(j, i)
                graph[a ^ 1].append(b)
                graph[b ^ 1].append(a)

    # Tarjan's strongly connected components, without recursion
    index, low, comp = [-1] * (2 * n), [0] * (2 * n), [-1] * (2 * n)
    stack, on_stack, counter, comps = [], [False] * (2 * n), 0, 0
    for root in range(2 * n):
        if index[root] >= 0:
            continue
        work = [(root, 0)]
        while work:
            v, k = work.pop()
            if k == 0:
                index[v] = low[v] = counter
                counter += 1
                stack.append(v)
                on_stack[v] = True
            if k < len(graph[v]):
                work.append((v, k + 1))
                u = graph[v][k]
                if index[u] < 0:
                    work.append((u, 0))
                elif on_stack[u]:
                    low[v] = min(low[v], index[u])
                continue
            if low[v] == index[v]:
                while True:
                    u = stack.pop()
                    on_stack[u] = False
                    comp[u] = comps
                    if u == v:
                        break
                comps += 1
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[v])

    if any(comp[2 * i] == comp[2 * i + 1] for i in range(n)):
        print("Impossible")
        return
    # Tarjan numbers components in reverse topological order
    truthful = [comp[2 * i] < comp[2 * i + 1] for i in range(n)]

    def scored(i, j):
        if said[i][j] < 0:
            return True
        return (said[i][j] == 1) == truthful[i]

    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            a, b = scored(i, j), scored(j, i)
            if a and b:
                table[i][j] = table[j][i] = DRAW
            elif a:
                table[i][j] = WIN
            else:
                table[j][i] = WIN
    print("\n".join(" ".join(map(str, row)) for row in table))


main()
