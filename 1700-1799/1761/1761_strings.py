import sys

# below this many bits the string is short enough to search directly
SMALL_BITS = 6
# the palindrome is made of the numbers 2^(k-1) + 5, 2^(k-1) + 6 and the
# start of 2^(k-1) + 7, three numbers of k bits less two
NUMBERS = 3
TAIL = 3
ALL_ONES = b"111"


def longest(n):
    s = "".join(bin(i)[2:] for i in range(1, n + 1))
    best = 0
    for centre in range(2 * len(s) - 1):
        lo, hi = centre // 2, (centre + 1) // 2
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        best = max(best, hi - lo - 1)
    return best


def main():
    # the number can have a million digits, so it is searched in place
    data = sys.stdin.buffer.read()
    start = data.find(b"1")
    end = len(data)
    while data[end - 1] not in b"01":
        end -= 1
    k = end - start
    if k < SMALL_BITS:
        print(longest(int(data[start:end], 2)))
        return
    # n reaches 2^(k-1) + 7 when a one follows the leading one before the
    # last three bits, or when those bits are all ones
    reached = data.find(b"1", start + 1, end - TAIL) >= 0 or data.endswith(ALL_ONES, 0, end)
    bits = k if reached else k - 1
    print(NUMBERS * bits - 2)


main()
