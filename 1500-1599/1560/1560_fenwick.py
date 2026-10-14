import sys

MOST = 4  # the highest K asked for


def main():
    words = iter(sys.stdin.buffer.read().split())
    n, m, mod = int(next(words)), int(next(words)), int(next(words))
    values = [int(next(words)) % mod for _ in range(n)]
    # trees[j] is a Fenwick tree of the power sums of a^j for j = 1..4; the
    # sums stay unreduced and are only reduced when a query reads them
    trees = [[0] * (n + 1) for _ in range(MOST + 1)]
    for i, a in enumerate(values, 1):
        power = 1
        for j in range(1, MOST + 1):
            power = power * a % mod
            trees[j][i] += power
    for j in range(1, MOST + 1):
        tree = trees[j]
        for i in range(1, n + 1):
            up = i + (i & -i)
            if up <= n:
                tree[up] += tree[i]
    inverse = [0] + [pow(k, mod - 2, mod) for k in range(1, MOST + 1)]
    out = []
    for _ in range(m):
        if next(words) == b"I":
            i, delta = int(next(words)), int(next(words))
            old = values[i - 1]
            new = (old + delta) % mod
            values[i - 1] = new
            po, pn = 1, 1
            for j in range(1, MOST + 1):
                po, pn = po * old % mod, pn * new % mod
                change = pn - po
                tree = trees[j]
                k = i
                while k <= n:
                    tree[k] += change
                    k += k & -k
        else:
            left, right, top = int(next(words)), int(next(words)), int(next(words))
            sums = [0] * (top + 1)
            for j in range(1, top + 1):
                tree = trees[j]
                total = 0
                k = right
                while k:
                    total += tree[k]
                    k -= k & -k
                k = left - 1
                while k:
                    total -= tree[k]
                    k -= k & -k
                sums[j] = total % mod
            # Newton's identities: k e_k = sum of (-1)^(i-1) e_(k-i) p_i
            e = [1] + [0] * top
            for k in range(1, top + 1):
                acc = 0
                for i in range(1, k + 1):
                    term = e[k - i] * sums[i]
                    acc += term if i % 2 else -term
                e[k] = acc % mod * inverse[k] % mod
            out.append(" ".join(map(str, e)))
    sys.stdout.write("\n".join(out) + "\n")


main()
