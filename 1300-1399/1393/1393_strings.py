import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    text = data[1][:n]
    # the shortest period p of the cyclic string: T is u repeated n / p times
    pi = [0] * n
    for i in range(1, n):
        k = pi[i - 1]
        while k and text[i] != text[k]:
            k = pi[k - 1]
        pi[i] = k + (text[i] == text[k])
    p = n - pi[-1]
    if n % p:
        p = n
    del pi
    # sort the rotations of u by doubling, all of them distinct
    letters = {c: i for i, c in enumerate(sorted(set(text[:p])))}
    cls = [letters[c] for c in text[:p]]
    order = sorted(range(p), key=cls.__getitem__)
    length = 1
    while True:
        # class of the doubled prefix, numbered in sorted order
        key = [cls[i] * (p + 1) + cls[(i + length) % p] for i in range(p)]
        order.sort(key=key.__getitem__)
        new = [0] * p
        count = 0
        for a, b in zip(order, order[1:]):
            if key[b] != key[a]:
                count += 1
            new[b] = count
        cls = new
        if count == p - 1:
            break
        length *= 2
    # Kasai: the common prefix with the previous rotation drops by at most one per step
    total = h = 0
    doubled = text[:p] * 2
    for i in range(p):
        r = cls[i]
        if r == 0:
            h = 0
            continue
        j = order[r - 1]
        while h < p and doubled[i + h] == doubled[j + h]:
            h += 1
        total += h
        if h:
            h -= 1
    # each rotation of u appears n / p times in a row, with common prefixes of n
    total += p * (n // p - 1) * n
    print("%.3f" % (total / (n - 1)))


main()
