import sys

LIMIT = 1 << 16  # N < 65536


def main():
    data = sys.stdin.buffer.read().split()
    # smallest prime factor of every number below the limit
    spf = list(range(LIMIT))
    i = 2
    while i * i < LIMIT:
        if spf[i] == i:
            for j in range(i * i, LIMIT, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    known = {}
    out = []
    for token in data[1 : 1 + int(data[0])]:
        p = int(token)
        if p not in known:
            # g is a primitive root when no g^((p-1)/q) is 1 for a prime q | p-1
            phi, rest, quotients = p - 1, p - 1, []
            while rest > 1:
                q = spf[rest]
                quotients.append(phi // q)
                while rest % q == 0:
                    rest //= q
            g = p - 1
            while any(pow(g, e, p) == 1 for e in quotients):
                g -= 1
            known[p] = g
        out.append(known[p])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
