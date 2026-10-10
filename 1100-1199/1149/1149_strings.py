def sine(n):
    # sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for odd k
    inner = "".join("sin(%d%s" % (k, "" if k == n else "-+"[k % 2 == 0]) for k in range(1, n + 1))
    return inner + ")" * n


def main():
    n = int(input())
    parts = ["(" * (n - 1)]
    for i in range(1, n + 1):
        parts.append("%s+%d%s" % (sine(i), n - i + 1, ")" if i < n else ""))
    print("".join(parts))


main()
