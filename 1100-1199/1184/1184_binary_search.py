import sys

CENTS = 100


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    # lengths have exactly two decimals, so in centimetres they are exact
    cables = [int(t.replace(".", "")) for t in data[2 : 2 + n]]
    # more pieces come out of shorter ones, so the longest length that still
    # gives k pieces is found by binary search; 0 means even 1 cm is too long
    low, high = 0, max(cables)
    while low < high:
        mid = (low + high + 1) // 2
        if sum(c // mid for c in cables) >= k:
            low = mid
        else:
            high = mid - 1
    print("%d.%02d" % divmod(low, CENTS))


main()
