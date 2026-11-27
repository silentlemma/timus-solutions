from os import _exit, write
import sys


# chunks bound token storage even when all input is on one line.
# every input integer has at most ten digits; only an unfinished token is kept.
INPUT_BUFFER = 1024


def numbers():
    tail = b""
    while chunk := sys.stdin.buffer.read(INPUT_BUFFER):
        parts = (tail + chunk).split()
        tail = parts.pop() if chunk[-1:] > b" " else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


def finish(answer):
    write(1, (str(answer) + "\n").encode())
    _exit(0)


def main():
    nums = numbers()
    n, k = next(nums), next(nums)
    next(nums)  # Bridge count; its records cannot change the answer.
    if n == 1 or k == 0:
        finish(n - 1)
    parent = [-1] * (n + 1)

    def find(x):
        while parent[x] >= 0:
            next_vertex = parent[x]
            if parent[next_vertex] >= 0:
                parent[x] = parent[next_vertex]
            x = next_vertex
        return x

    # Tunnels are free; some bridges can stay inside a tunnel component.
    # The connected full network provides enough bridges between components.
    groups = n
    for _ in range(k):
        a, b = find(next(nums)), find(next(nums))
        if a != b:
            if parent[a] > parent[b]:
                a, b = b, a
            parent[a] += parent[b]
            parent[b] = a
            groups -= 1
            if groups == 1:
                finish(0)
    # The complete network is connected; bridge endpoints cannot change this count.
    # No need to parse the unused remainder of the standalone input file.
    finish(groups - 1)


main()
