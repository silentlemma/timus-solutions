DIGITS = 9  # numbers below 10^9 have at most nine digits
BASE = 10


def main():
    target = int(input())
    ways = [1]  # ways[s]: digit strings of the current length with digit sum s
    for _ in range(DIGITS):
        nxt = [0] * (len(ways) + BASE - 1)
        for s, w in enumerate(ways):
            for d in range(BASE):
                nxt[s + d] += w
        ways = nxt
    # 10^9 itself has digit sum 1; zero is not counted since S >= 1
    print(ways[target] + (target == 1))


main()
