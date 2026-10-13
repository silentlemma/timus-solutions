def main():
    n = int(input())
    # a[k]: rooted trees with k vertices; s[k]: the sum of d a[d] over divisors d of k
    a = [0, 1]
    s = [0, 1]
    for m in range(1, n):
        # a(m + 1) = (s(1) a(m) + s(2) a(m - 1) + ... + s(m) a(1)) / m
        a.append(sum(s[k] * a[m - k + 1] for k in range(1, m + 1)) // m)
        s.append(sum(d * a[d] for d in range(1, m + 2) if (m + 1) % d == 0))
    print(a[n])


main()
