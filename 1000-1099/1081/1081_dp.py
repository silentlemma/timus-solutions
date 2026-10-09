import sys


def main():
    n, k = map(int, sys.stdin.read().split())
    # count[r]: strings of length r without two adjacent ones (Fibonacci)
    count = [1, 2]
    while len(count) <= n:
        count.append(count[-1] + count[-2])
    if k > count[n]:
        print(-1)
        return
    out = []
    for pos in range(n):
        rest = n - pos - 1
        # strings with 0 here come first; a 1 is only possible after a 0
        if (out and out[-1] == "1") or k <= count[rest]:
            out.append("0")
        else:
            k -= count[rest]
            out.append("1")
    print("".join(out))


main()
