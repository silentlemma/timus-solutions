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

    # tunnels are free; every bridge joins two of the remaining groups
    groups = n
    for _ in range(k):
        a, b = find(next(nums)), find(next(nums))
        if a != b:
            parent[a] = b
            groups -= 1
    print(groups - 1)


main()
