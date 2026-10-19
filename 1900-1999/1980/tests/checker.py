"""Check road-index walks and high-precision lower-bound infeasibility."""

from collections import deque
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
import sys

EPSILON = Decimal("1e-6")
PRECISION = 80
ROUND_GUARD = Decimal("1e-60")


def read_instance(text):
    tokens = iter(map(int, text.split()))
    n, m = next(tokens), next(tokens)
    edges = [(next(tokens) - 1, next(tokens) - 1, next(tokens), next(tokens)) for _ in range(m)]
    deadline = next(tokens)
    return n, edges, deadline


def faster_path(n, edges, deadline, extra):
    graph = [[] for _ in range(n)]
    for a, b, speed, length in edges:
        cost = Decimal(length) / (Decimal(speed) + extra)
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    distance = [Decimal("Infinity")] * n
    distance[0] = Decimal(0)
    queued = bytearray(n)
    queued[0] = 1
    pending = deque([0])
    threshold = Decimal(deadline) - ROUND_GUARD * max(1, deadline)
    while pending:
        vertex = pending.popleft()
        queued[vertex] = 0
        for neighbor, cost in graph[vertex]:
            candidate = distance[vertex] + cost
            if candidate < distance[neighbor] and candidate < threshold:
                if neighbor == n - 1:
                    return True
                distance[neighbor] = candidate
                if not queued[neighbor]:
                    queued[neighbor] = 1
                    if pending and candidate < distance[pending[0]]:
                        pending.appendleft(neighbor)
                    else:
                        pending.append(neighbor)
    return False


def verify(n, edges, deadline, text):
    try:
        tokens = text.split()
        if len(tokens) < 2:
            return False, "missing speed or road count"
        extra = Decimal(tokens[0])
        count = int(tokens[1])
        path = [int(s) - 1 for s in tokens[2:]]
        if not extra.is_finite() or extra < 0 or count != len(path) or count < 1:
            return False, "invalid speed or road count"
        with localcontext() as context:
            context.prec = PRECISION
            # Exact inversion of |reported-opt|<=epsilon*max(1,opt).
            lower = (
                max(Decimal(0), extra - EPSILON) if extra <= 1 + EPSILON else extra / (1 + EPSILON)
            )
            upper = extra + EPSILON if extra <= 1 - EPSILON else extra / (1 - EPSILON)
            vertex = 0
            time = Decimal(0)
            for index in path:
                if not 0 <= index < len(edges):
                    return False, "unknown road index"
                a, b, speed, length = edges[index]
                if vertex != a and vertex != b:
                    return False, "roads do not form a walk"
                vertex = a + b - vertex
                time += Decimal(length) / (Decimal(speed) + upper)
            if vertex != n - 1 or time > Decimal(deadline) + ROUND_GUARD * max(1, deadline):
                return False, "reported path cannot meet the deadline within speed tolerance"
            if lower > 0 and faster_path(n, edges, deadline, lower):
                return False, "speed exceeds the allowed error above the optimum"
        return True, "OK"
    except (ValueError, InvalidOperation, OverflowError):
        return False, "invalid numeric output"


if __name__ == "__main__":
    try:
        n, edges, deadline = read_instance(Path(sys.argv[1]).read_text())
        good, detail = verify(n, edges, deadline, Path(sys.argv[3]).read_text())
    except (ValueError, StopIteration, OSError, IndexError) as error:
        good, detail = False, str(error)
    print(detail)
    raise SystemExit(0 if good else 1)
