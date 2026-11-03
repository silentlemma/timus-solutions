from array import array
import sys

MOD = 10**9


def main():
    numbers = (int(word) for line in sys.stdin.buffer for word in line.split())
    n, k = next(numbers), next(numbers)
    if k > n:
        print(0)
        return
    flipped = array("H", (n + 1 - next(numbers) for _ in range(n)))
    del numbers
    ways = array("I", [1]) * n
    tree = array("I", [0]) * (n + 1)
    total = 0
    for _ in range(k - 1):
        for j in range(n + 1):
            tree[j] = 0
        total = 0
        nonzero = False
        for i, value in enumerate(flipped):
            old = ways[i]
            result, j = 0, value - 1
            while j:
                result += tree[j]
                if result >= MOD:
                    result -= MOD
                j &= j - 1
            ways[i] = result
            if result:
                nonzero = True
                total += result
                if total >= MOD:
                    total -= MOD
            # Future queries need the old layer, not the result just written.
            if old:
                j = value
                while j <= n:
                    cell = tree[j] + old
                    if cell >= MOD:
                        cell -= MOD
                    tree[j] = cell
                    j += j & -j
        if not nonzero:
            print(0)
            return
    print(total)


main()
