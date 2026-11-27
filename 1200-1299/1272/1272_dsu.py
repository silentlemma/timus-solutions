import sys


def main():
    nums = map(int, sys.stdin.buffer.read().split())
    n, k = next(nums), next(nums)
    next(nums)  # the bridges themselves do not matter
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    # Tunnels are free; some bridges can stay inside a tunnel component.
    # The connected full network provides enough bridges between components.
    groups = n
    for _ in range(k):
        a, b = find(next(nums)), find(next(nums))
        if a != b:
            parent[a] = b
            groups -= 1
    print(groups - 1)


main()
