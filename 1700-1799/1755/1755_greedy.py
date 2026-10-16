def main():
    a1, b1, a2, b2 = (int(v) for v in input().split())
    n, m = (int(v) for v in input().split())
    # Karlsson leaves the piece he likes no more than half, so the best is
    # the piece of greatest worth to Little Boy within half of Karlsson's total:
    # a fractional knapsack where each ingredient is taken by worth per cost
    goods = [(a1, a2, n, 0), (b1, b2, m, 1)]
    # zero-cost goods first, then by worth over cost, highest first
    if goods[1][0] * goods[0][1] > goods[0][0] * goods[1][1]:
        goods.reverse()
    room = (a2 * n + b2 * m) / 2
    piece = [0.0, 0.0]
    for _, cost, amount, slot in goods:
        take = amount if cost * amount <= room else room / cost
        piece[slot] = take
        room -= take * cost
    print("%.8f %.8f" % (piece[0], piece[1]))


main()
