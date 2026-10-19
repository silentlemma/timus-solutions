import sys
from array import array


class ConnectivityQueue:
    def __init__(self, n, first, second):
        self.parent = [-1] * n
        self.components = n
        self.first = first
        self.second = second
        self.ranks = []
        self.flags = bytearray()
        self.children = []
        self.sizes = []
        self.front_count = 0

    def push(self, rank, front=0):
        u, v = self.first[rank], self.second[rank]
        p = self.parent
        # Union by size bounds tree height without changing paths during rollback.
        while p[u] >= 0:
            u = p[u]
        while p[v] >= 0:
            v = p[v]
        size = 0
        if u != v:
            if p[u] > p[v]:
                u, v = v, u
            size = p[v]
            p[u] += size
            p[v] = u
            self.components -= 1
        else:
            v = -1
        self.children.append(v)
        self.sizes.append(size)
        self.ranks.append(rank)
        self.flags.append(front)
        self.front_count += front

    def rollback(self):
        v = self.children.pop()
        size = self.sizes.pop()
        if v >= 0:
            p = self.parent
            p[p[v]] -= size
            p[v] = size
            self.components += 1
        self.front_count -= self.flags.pop()
        return self.ranks.pop()

    def pop(self):
        if not self.flags[-1]:
            # Rebuild equal portions of the two stacks, or reverse all remaining edges.
            # Front edges are restored last so that the oldest edge can be rolled back.
            back = []
            front = []
            while self.ranks:
                flag = self.flags[-1]
                rank = self.rollback()
                if flag:
                    front.append(rank)
                else:
                    back.append(rank)
                if not self.front_count:
                    while self.ranks:
                        back.append(self.rollback())
                    break
                if len(front) == len(back):
                    break
            if self.front_count:
                for rank in reversed(back):
                    self.push(rank)
            else:
                for rank in back:
                    self.push(rank, 1)
            for rank in reversed(front):
                self.push(rank, 1)
        return self.rollback()


def solve(n, first, second, weights, identifiers):
    queue = ConnectivityQueue(n, first, second)
    lower = 0
    width = None
    best_left = best_right = 0
    for rank, w in enumerate(weights):
        queue.push(rank)
        last = -1
        # The last connected window has the largest possible lower price.
        while queue.components == 1:
            last = lower
            queue.pop()
            lower += 1
        if last >= 0:
            diff = w - weights[last]
            if width is None or diff < width:
                width, best_left, best_right = diff, last, rank
            if width == 0:
                break
    p = [-1] * n
    answer = []
    for rank in range(best_left, best_right + 1):
        u, v = first[rank], second[rank]
        identifier = identifiers[rank]
        while p[u] >= 0:
            if p[p[u]] >= 0:
                p[u] = p[p[u]]
            u = p[u]
        while p[v] >= 0:
            if p[p[v]] >= 0:
                p[v] = p[p[v]]
            v = p[v]
        if u != v:
            if p[u] > p[v]:
                u, v = v, u
            p[u] += p[v]
            p[v] = u
            answer.append(identifier)
    return answer


def main():
    fields = iter(sys.stdin.buffer.read().split())
    vertices, count = int(next(fields)), int(next(fields))
    first, second, weights = array("i"), array("i"), array("i")
    for _ in range(count):
        first.append(int(next(fields)) - 1)
        second.append(int(next(fields)) - 1)
        weights.append(int(next(fields)))
    del fields
    order = list(range(count))
    # Stable passes preserve the original ordering of equal-price edges.
    order.sort(key=second.__getitem__)
    order.sort(key=first.__getitem__)
    order.sort(key=weights.__getitem__)
    first = array("i", (first[i] for i in order))
    second = array("i", (second[i] for i in order))
    weights = array("i", (weights[i] for i in order))
    identifiers = array("i", (i + 1 for i in order))
    del order
    chosen = solve(vertices, first, second, weights, identifiers)
    sys.stdout.write(" ".join(map(str, chosen)) + "\n")


if __name__ == "__main__":
    main()
