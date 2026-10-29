import sys


def main():
    # the input is parsed line by line; there are at most 100 vertices, so the
    # adjacency lists and the sides fit in bytearrays
    tokens = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(tokens)
    adj = [bytearray() for _ in range(n + 1)]
    for neighbours in adj[1:]:
        for vertex in tokens:
            if vertex == 0:
                break
            neighbours.append(vertex)
    # colour a BFS tree of every component by depth parity: each member has a
    # tree neighbour, its parent or a child, in the other team
    side = bytearray(n + 1)
    for root in range(1, n + 1):
        if side[root]:
            continue
        side[root] = 1
        # a plain list walked in order serves as the queue
        queue = [root]
        for vertex in queue:
            other_side = 1 + side[vertex] % 2
            for neighbour in adj[vertex]:
                if not side[neighbour]:
                    side[neighbour] = other_side
                    queue.append(neighbour)
    team = [str(v) for v in range(1, n + 1) if side[v] == 1]
    print(str(len(team)) + "\n" + " ".join(team))


main()
