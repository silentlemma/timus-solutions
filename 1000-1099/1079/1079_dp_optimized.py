import sys
from array import array

TOP = 99999
LAST_PARENT = (TOP + 1) // 2


def main():
    # n < 2^17 bounds every stern value by fibonacci(19) = 4181, fitting 16 bits.
    a = array("H", [0]) * (LAST_PARENT + 1)
    best = array("H", [0]) * (TOP + 1)
    a[1] = best[1] = 1
    largest = 1
    for i in range(2, TOP + 1):
        half = i // 2
        value = a[half] if i % 2 == 0 else a[half] + a[half + 1]
        # later terms only refer to indices in the first half.
        if i <= LAST_PARENT:
            a[i] = value
        if value > largest:
            largest = value
        best[i] = largest
    out = []
    for n in map(int, sys.stdin.buffer.read().split()):
        if n == 0:
            break
        out.append(str(best[n]))
    print("\n".join(out))


main()
