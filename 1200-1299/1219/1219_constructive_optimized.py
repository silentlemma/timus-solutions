import sys

LETTERS = 26
ORDER = 3
LENGTH = 1000000


def de_bruijn(k, n):
    """a cyclic sequence over k symbols with every word of length n once."""
    a = [0] * (n + 1)
    # each generated symbol is a lowercase latin byte, so one byte per symbol suffices.
    seq = bytearray()
    first_letter = ord("a")

    def gen(t, p):
        if t > n:
            if n % p == 0:
                for i in range(1, p + 1):
                    seq.append(first_letter + a[i])
        else:
            a[t] = a[t - p]
            gen(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                gen(t + 1, t)

    gen(1, 1)
    return seq


def main():
    cycle = de_bruijn(LETTERS, ORDER)
    # repeating the cycle keeps every window of three letters a cyclic window
    # of it, so each triple, pair and letter appears almost equally often
    repeats, tail = divmod(LENGTH, len(cycle))
    out = sys.stdout.buffer
    for _ in range(repeats):
        out.write(cycle)
    out.write(cycle[:tail])
    out.write(b"\n")


main()
