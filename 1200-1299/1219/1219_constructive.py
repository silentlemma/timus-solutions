import sys

LETTERS = 26
ORDER = 3
LENGTH = 1000000


def de_bruijn(k, n):
    """A cyclic sequence over k symbols with every word of length n once."""
    a = [0] * (k * n)
    seq = []

    def gen(t, p):
        if t > n:
            if n % p == 0:
                seq.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            gen(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                gen(t + 1, t)

    gen(1, 1)
    return seq


def main():
    cycle = "".join(chr(ord("a") + d) for d in de_bruijn(LETTERS, ORDER))
    # repeating the cycle keeps every window of three letters a cyclic window
    # of it, so each triple, pair and letter appears almost equally often
    reps = -(-LENGTH // len(cycle))
    sys.stdout.write((cycle * reps)[:LENGTH] + "\n")


main()
