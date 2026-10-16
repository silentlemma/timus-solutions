import sys

HEX = 16
DIGITS = 4
NIBBLE = 15
BITS = 4
BASE = 10
DECIMAL = "0123456789"


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pins = [0] + [int(w, HEX) for w in data[1:n + 1]]
    # differing hex digits of two pins: nonzero nibbles of their xor
    differ = [0] * (HEX ** DIGITS)
    for x in range(1, HEX ** DIGITS):
        differ[x] = differ[x >> BITS] + (1 if x & NIBBLE else 0)
    count = [0] * (DIGITS + 1)
    longest = len(str(n))
    for i in range(1, n + 1):
        pin = pins[i]
        # each pair is counted from its smaller number: a digit raised in
        # place, which never repeats a number, or a digit inserted
        place, rest = 1, i
        while rest:
            for d in range(rest % BASE + 1, BASE):
                j = i + (d - rest % BASE) * place
                if j > n:
                    break
                count[differ[pin ^ pins[j]]] += 1
            place *= BASE
            rest //= BASE
        s = str(i)
        if len(s) < longest:
            near = {s[:p] + d + s[p:] for p in range(len(s) + 1) for d in DECIMAL}
            for t in near:
                j = int(t)
                if t[0] != "0" and j <= n:
                    count[differ[pin ^ pins[j]]] += 1
    print(" ".join(map(str, count[1:])))


main()
