import sys


def main():
    data = iter(map(int, sys.stdin.read().split()))
    p, t, n, m = next(data), next(data), next(data), next(data)
    pairs = [next(data) for _ in range(2 * m)]
    half = t // 2
    full = (1 << n) - 1
    # after[x]: the dishes that may still be brought over a plate of dish x
    after = [full] * n
    for i, j in zip(pairs[0::2], pairs[1::2]):
        after[i - 1] &= ~(1 << (j - 1))
    # the count of time-tables depends only on the set of dishes that may be
    # brought; plates above a plate of x shrink that set to its part in after[x]
    seen, stack = {full}, [full]
    while stack:
        allowed = stack.pop()
        for x in range(n):
            if allowed >> x & 1:
                inner = allowed & after[x]
                if inner not in seen:
                    seen.add(inner)
                    stack.append(inner)
    # ways[s][q]: time-tables of q dishes with the set s allowed
    ways = {}
    for allowed in sorted(seen, key=lambda s: bin(s).count("1")):
        dishes = [x for x in range(n) if allowed >> x & 1]
        inner_sets = [allowed & after[x] for x in dishes]
        f = [1] + [0] * half
        tree = [0] * half  # tree[q]: one plate with q dishes over it
        for q in range(1, half + 1):
            tree[q - 1] = sum((ways[s] if s != allowed else f)[q - 1] for s in inner_sets) % p
            # the first plate holds a dishes over it, the rest follow it
            f[q] = sum(tree[a] * f[q - 1 - a] for a in range(q)) % p
        ways[allowed] = f
    print(ways[full][half] % p)


main()
