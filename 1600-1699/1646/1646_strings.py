import sys

MOD = 10**9 + 7
SAMPLES = 2  # the two first samples come before the count


def occurrences(text, pattern):
    return sum(1 for i in range(len(text) - len(pattern) + 1) if text.startswith(pattern, i))


def main():
    data = sys.stdin.read().split()
    pattern = data[0]
    edge = len(pattern) - 1  # letters kept at each end of a sample

    def head(s):
        return s[:edge]

    def tail(s):
        return s[max(0, len(s) - edge) :]

    # a sample: its count mod MOD and its first and last letters; the full
    # string can be 2^100 long
    samples = [(occurrences(s, pattern), head(s), tail(s)) for s in data[1 : 1 + SAMPLES]]
    days = iter(int(w) - 1 for w in data[2 + SAMPLES :])
    for i, j in zip(days, days):
        a, b = samples[i], samples[j]
        # every new occurrence crosses the seam, so it lies in these letters
        seam = occurrences(a[2] + b[1], pattern)
        samples.append(((a[0] + b[0] + seam) % MOD, head(a[1] + b[1]), tail(a[2] + b[2])))
    print(samples[-1][0])


main()
