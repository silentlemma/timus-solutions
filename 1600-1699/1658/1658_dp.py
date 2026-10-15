import sys

LONGEST = 100  # digits allowed in the answer
DIGITS = range(1, 10)  # a shortest number never needs a zero


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    # reach[k][s1]: bit s2 set when k nonzero digits can sum to s1 with
    # squares summing to s2
    reach = [[1]]
    for k in range(1, LONGEST + 1):
        prev = reach[-1]
        row = []
        for s1 in range(max(DIGITS) * k + 1):
            bits = 0
            for d in DIGITS:
                if 0 <= s1 - d < len(prev):
                    bits |= prev[s1 - d] << (d * d)
            row.append(bits)
        reach.append(row)

    def can(k, s1, s2):
        return 0 <= s1 < len(reach[k]) and s2 >= 0 and reach[k][s1] >> s2 & 1

    out = []
    for q in range(t):
        s1, s2 = data[1 + 2 * q], data[2 + 2 * q]
        size = next((k for k in range(1, LONGEST + 1) if can(k, s1, s2)), 0)
        if not size:
            out.append("No solution")
            continue
        # the smallest digit first that still leaves a way to finish; the
        # digits come out sorted, so each search starts at the last one
        digits = []
        d = min(DIGITS)
        for left in range(size - 1, -1, -1):
            while not can(left, s1 - d, s2 - d * d):
                d += 1
            digits.append(str(d))
            s1, s2 = s1 - d, s2 - d * d
        out.append("".join(digits))
    print("\n".join(out))


main()
