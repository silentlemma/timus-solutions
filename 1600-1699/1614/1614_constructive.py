def main():
    n = int(input())
    stops = 2 * n
    for k in range(n):
        # k, k + 1, k - 1, k + 2, k - 2, ..., k + n around the circle of stops:
        # its neighbouring pairs are exactly those with sum 2k or 2k + 1
        route = [k]
        for j in range(1, n + 1):
            route.append((k + j) % stops)
            if j < n:
                route.append((k - j) % stops)
        print(" ".join(str(x + 1) for x in route))


main()
