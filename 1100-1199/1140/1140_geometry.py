import sys


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    total = {"X": 0, "Y": 0, "Z": 0}
    for k in range(n):
        total[data[1 + 2 * k]] += int(data[2 + 2 * k])
    # a step along Y is a step along X and one along Z, so the walk ends at
    # a X + b Z; going back with m steps along Y costs |a - m| + |m| + |b - m|,
    # which is smallest at the median of a, 0 and b
    a = total["X"] + total["Y"]
    b = total["Z"] + total["Y"]
    m = sorted((a, 0, b))[1]
    back = [("X", m - a), ("Y", -m), ("Z", m - b)]
    back = [(d, k) for d, k in back if k]
    print(len(back))
    for d, k in back:
        print(d, k)


main()
