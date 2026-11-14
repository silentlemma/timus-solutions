import sys


def main():
    values = map(int, sys.stdin.buffer.read().split())
    size = next(values)
    parent = [0, 0, *values]
    height = [0] * (size + 1)
    deepest = list(range(size + 1))
    diameter = 0
    endpoint = 1

    # Each child's height is final when it reaches its parent.
    for vertex in range(size, 1, -1):
        above = parent[vertex]
        arm = height[vertex] + 1
        across = arm + height[above]
        if across > diameter:
            diameter = across
            # Start on the longer arm so the middle stays below the fork.
            endpoint = deepest[vertex] if arm >= height[above] else deepest[above]
        if arm > height[above]:
            height[above] = arm
            deepest[above] = deepest[vertex]

    for _ in range(diameter // 2):
        endpoint = parent[endpoint]
    if diameter % 2:
        print(*sorted((endpoint, parent[endpoint])))
    else:
        print(endpoint)


if __name__ == "__main__":
    main()
