import sys


PERCENT = 100
OUTPUT_SCALE = 10**8
NO_SHARE = (0, 1)
FULL_SHARE = (1, 1)


def share(n, deadline, records):
    children = [[] for _ in range(n)]
    days = [0]
    for node, (parent, delay) in enumerate(zip(records, records), 1):
        children[parent - 1].append(node)
        days.append(delay)

    order = [0]
    for node in order:
        for child in children[node]:
            days[child] += days[node]
            order.append(child)

    limits = [NO_SHARE] * n
    for node in reversed(order):
        if days[node] > deadline:
            continue
        direct = children[node]
        if not direct:
            limits[node] = FULL_SHARE
            continue
        count = len(direct)
        # At rank r, both r/count and the r-th child's limit bound the share.
        # Distinct fractions here are separated by at least 1/(n-1)^2.
        ranked = sorted(
            (limits[child] for child in direct), key=lambda f: f[0] / f[1], reverse=True
        )
        for rank, (num, den) in enumerate(ranked, 1):
            if rank * den >= num * count:
                limits[node] = (num, den) if (rank - 1) * den < num * count else (rank - 1, count)
                break
        else:
            limits[node] = FULL_SHARE
    return limits[0]


def main():
    tokens = map(int, sys.stdin.buffer.read().split())
    n, deadline = next(tokens), next(tokens)
    num, den = share(n, deadline, tokens)
    value = (num * PERCENT * OUTPUT_SCALE + den // 2) // den
    print(f"{value // OUTPUT_SCALE}.{value % OUTPUT_SCALE:08d}")


if __name__ == "__main__":
    main()
