import sys


def main():
    words = iter(sys.stdin.read().split())
    length, top, k = int(next(words)), int(next(words)), int(next(words))
    n = int(next(words))
    # ways[i][r]: how many ways i registers can hold values 1..M with a sum
    # that leaves remainder r modulo K
    ways = [[0] * k for _ in range(length + 1)]
    ways[0][0] = 1
    for i in range(1, length + 1):
        prev, row = ways[i - 1], ways[i]
        for v in range(1, top + 1):
            for r in range(k):
                row[(r + v) % k] += prev[r]
    out, total = [], 0
    for pos in range(length):
        left = length - pos - 1
        # try the values in increasing order and skip whole blocks of states
        for v in range(1, top + 1):
            block = ways[left][-(total + v) % k]
            if n < block:
                out.append(v)
                total += v
                break
            n -= block
    print(" ".join(map(str, out)))


main()
