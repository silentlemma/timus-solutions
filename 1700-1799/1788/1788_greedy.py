import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    girls = sorted(data[2:2 + n])
    boys = sorted(data[2 + n:2 + n + m])
    # with k pairs the k most sensitive girls stay dry, and the k most
    # sensitive boys walk with them
    print(min(sum(girls[:n - k]) + sum(boys[:m - k]) * k
              for k in range(min(n, m) + 1)))


main()
