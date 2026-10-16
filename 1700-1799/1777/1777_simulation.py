def main():
    piles = sorted(int(v) for v in input().split())
    asked = 0
    while True:
        asked += 1
        # the closest two piles differ least among neighbours in sorted order
        gap = min(b - a for a, b in zip(piles, piles[1:]))
        if gap == 0:
            break
        piles.append(gap)
        piles.sort()
    print(asked)


main()
