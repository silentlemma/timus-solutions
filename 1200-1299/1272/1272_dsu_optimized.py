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


def main():
    nums = numbers()
    n, k = next(nums), next(nums)
    m = next(nums)
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # tunnels are free; every bridge joins two of the remaining groups
    groups = n
    for _ in range(k):
        a, b = find(next(nums)), find(next(nums))
        if a != b:
            parent[a] = b
            groups -= 1
    # bridges do not change tunnel components; still consume every pair.
    for _ in range(m):
        next(nums)
        next(nums)
    print(groups - 1)


main()
