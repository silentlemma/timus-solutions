import sys


def main():
    n, s, t, *_ = sys.stdin.buffer.read().split()
    n = int(n)
    # t is s turned left by k, that is right by n - k: find it in s + s
    k = (s + s).find(t)
    print(-1 if k < 0 else (n - k) % n)


main()
