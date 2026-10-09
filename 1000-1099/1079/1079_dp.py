import sys

TOP = 99999


def main():
    a = [0] * (TOP + 1)
    a[1] = 1
    for i in range(2, TOP + 1):
        half = i // 2
        a[i] = a[half] if i % 2 == 0 else a[half] + a[half + 1]
    best = a[:]
    for i in range(1, TOP + 1):
        best[i] = max(best[i - 1], a[i])
    out = []
    for n in map(int, sys.stdin.read().split()):
        if n == 0:
            break
        out.append(str(best[n]))
    print("\n".join(out))


main()
