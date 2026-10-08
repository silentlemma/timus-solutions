def main():
    n = int(input())
    # ways[s]: sets of distinct step sizes, each used at most once, summing
    # to s; sizes are added one by one, going over s downwards
    ways = [1] + [0] * n
    for size in range(1, n + 1):
        for s in range(n, size - 1, -1):
            ways[s] += ways[s - size]
    # a staircase needs at least two steps: drop the single step of n cubes
    print(ways[n] - 1)


main()
