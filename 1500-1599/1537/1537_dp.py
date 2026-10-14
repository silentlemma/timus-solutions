from array import array


def main():
    k, p = map(int, input().split())
    # an ent with w words teaches an old ent who ends with w + 1 words and a
    # young one who ends with 2w, so with g(m) ents knowing 2m (or 2m + 1)
    # words: g(1) = 1 and g(m) = g(m - 1) + g(m // 2)
    if k < 2:
        print(0)
        return
    top = k // 2
    half = top // 2  # only these values are looked up again
    g = array("q", [0]) * (half + 1)
    cur = 1 % p
    if half >= 1:
        g[1] = cur
    for m in range(2, top + 1):
        cur = (cur + g[m >> 1]) % p
        if m <= half:
            g[m] = cur
    print(cur)


main()
