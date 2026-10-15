import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, d, buyers = data[0], data[1], data[2:]
    # sell to everyone who can be served: by the end of month i at most
    # i * d yachts exist, so the running total of sales is capped there
    sales = []
    total = 0
    for i, a in enumerate(buyers, 1):
        new = min(total + a, i * d)
        sales.append(new - total)
        total = new
    # build every yacht as late as possible: going backwards, whatever a
    # month cannot build is built earlier and waits one month per boundary
    carry = storage = 0
    for sold in reversed(sales):
        storage += carry
        carry = max(0, sold + carry - d)
    print(total, storage)


main()
