from array import array
import sys

CENTS = 100


def main():
    read = sys.stdin.buffer.readline
    n, k = map(int, read().split())
    cables = array("I", (int(read().replace(b".", b"")) for _ in range(n)))
    longest = max(cables)
    low, high = longest // k, min(longest, sum(cables) // k)
    # The longest cable alone proves low feasible; total length bounds high.
    while low < high:
        mid = (low + high + 1) // 2
        pieces = 0
        for length in cables:
            pieces += length // mid
            if pieces >= k:
                break
        if pieces >= k:
            low = mid
        else:
            high = mid - 1
    print("%d.%02d" % divmod(low, CENTS))


main()
