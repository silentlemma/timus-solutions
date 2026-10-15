import math
import sys

BITS = 8  # bits of a character, the lowest first
ONE_FREQ = 2  # a one is sin(2 pi k / t), a zero sin(4 pi k / t)
ZERO_FREQ = 4


def main():
    data = sys.stdin.read().split()
    n, t = int(data[0]), int(data[1])
    samples = [float(w) for w in data[2:2 + n]]
    # over whole periods the two waves are orthogonal to each other and to a
    # constant, so a bit's correlation with each picks the one sent; the zero
    # level and the amplitude cancel out
    one = [math.sin(ONE_FREQ * math.pi * k / t) for k in range(t)]
    zero = [math.sin(ZERO_FREQ * math.pi * k / t) for k in range(t)]
    bits = []
    for start in range(0, n, t):
        block = samples[start:start + t]
        to_one = sum(x * y for x, y in zip(block, one))
        bits.append(to_one > sum(x * y for x, y in zip(block, zero)))
    text = []
    for start in range(0, len(bits), BITS):
        text.append(chr(sum(bits[start + j] << j for j in range(BITS))))
    print("".join(text))


main()
