import sys

BASE = 10
INF = float("inf")


def main():
    a_str, b_str, c_str = sys.stdin.read().split()
    width = len(c_str)
    if max(len(a_str), len(b_str)) > width:
        print(-1)  # the sum would be longer than C
        return

    def digits(s):
        """The digits from the lowest, padded with zeros to the width of C,
        and the lowest digit each position may take."""
        low = [int(ch) for ch in reversed(s)] + [0] * (width - len(s))
        least = [0] * width
        least[len(s) - 1] = 1  # the first digit may not become zero
        return low, least

    (da, la), (db, lb), (dc, lc) = digits(a_str), digits(b_str), digits(c_str)
    # cost[carry]: the cheapest fix of the lower positions that carries this
    cost = [0, INF]
    for i in range(width):
        nxt = [INF, INF]
        # past its own length a number has only the digit 0
        top_a = BASE - 1 if i < len(a_str) else 0
        top_b = BASE - 1 if i < len(b_str) else 0
        for carry in (0, 1):
            if cost[carry] == INF:
                continue
            for x in range(la[i], top_a + 1):
                for y in range(lb[i], top_b + 1):
                    total = x + y + carry
                    z = total % BASE
                    if z < lc[i]:
                        continue
                    c = cost[carry] + abs(x - da[i]) + abs(y - db[i]) + abs(z - dc[i])
                    if c < nxt[total // BASE]:
                        nxt[total // BASE] = c
        cost = nxt
    print(cost[0] if cost[0] < INF else -1)


main()
