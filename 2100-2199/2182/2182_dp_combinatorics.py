import sys
from math import comb

SMALL = 60  # only boxes up to the number of bits can receive extra bottles


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    boxes = list(map(int, data[2:2 + q]))
    top = (1 << n) - 1
    last = min(SMALL, top)
    # Box k gets one bottle for every bottle placed in a box j != k with
    # popcount(j) = k; boxes above 60 hold only their own one, and the small
    # boxes are filled from the top down, as popcount(j) < j for j > 1.
    count = [1] * (last + 1)
    for k in range(last, 0, -1):
        small = [j for j in range(k + 1, last + 1) if bin(j).count("1") == k]
        count[k] = 1 + comb(n, k) - (k == 1) - len(small) + sum(count[j] for j in small)
    print(" ".join(str(count[a]) if a <= last else "1" for a in boxes))


main()
