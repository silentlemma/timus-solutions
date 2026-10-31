import sys

# chunks bound token storage even when all input is on one line.
# every input integer has at most ten digits; only an unfinished token is kept.
INPUT_BUFFER = 8192


def numbers():
    tail = b""
    while chunk := sys.stdin.buffer.read(INPUT_BUFFER):
        parts = (tail + chunk).split()
        tail = parts.pop() if chunk[-1:] > b" " else b""
        yield from map(int, parts)
    if tail:
        yield int(tail)


HUB_BITS = 10
LENGTH_BITS = 2 * HUB_BITS
HUB_MASK = (1 << HUB_BITS) - 1


def main():
    nums = numbers()
    n, m = next(nums), next(nums)
    edges = []
    # n <= 1000 needs ten bits per hub; the higher bits hold the cable length.
    for _ in range(m):
        a, b, length = next(nums), next(nums), next(nums)
        edges.append((length << LENGTH_BITS) | (a << HUB_BITS) | b)
    edges.sort()
    parent = list(range(n + 1))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    plan = []
    longest = 0
    for e in edges:
        a, b = (e >> HUB_BITS) & HUB_MASK, e & HUB_MASK
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            longest = e >> LENGTH_BITS
            plan.append(f"{a} {b}")
            if len(plan) == n - 1:
                break
    print(longest, len(plan), *plan, sep="\n")


main()
