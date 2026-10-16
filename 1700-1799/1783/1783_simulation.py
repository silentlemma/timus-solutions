import sys


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    plan = [int(v) for v in data[2:2 + n + m - 1]]
    stock = 0
    orders = []
    for i in range(n):
        # after t months of the same change x the stock is stock + t x, which
        # must reach the plan of that month; x is rounded up, also below zero
        x = max(-((stock - plan[i + t - 1]) // t) for t in range(1, m + 1))
        orders.append(x)
        stock += x
    print(" ".join(map(str, orders)))


main()
