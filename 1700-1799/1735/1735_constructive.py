import math


def main():
    n, k, _, _ = map(int, input().split())
    # the scale shows x times all the bars plus y - x times the platinum
    # ones, so the counts must have pairwise different subset sums; the
    # Conway-Guy sets u_n - u_i do, with the smallest largest count known
    u = [0, 1]
    for m in range(1, n):
        u.append(2 * u[m] - u[m - round(math.sqrt(2 * m))])
    if u[n] > k:
        print("NO")
        return
    print("YES")
    print(" ".join(str(u[n] - u[i]) for i in range(n)))


main()
