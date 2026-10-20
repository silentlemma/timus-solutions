import sys

FRIEND = ord("1")
TRIANGLE_SIZE = 3


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    graph = [b"".join(data[start : start + n]) for start in range(1, n * n + 1, n)]
    del data

    used = bytearray(n)
    pairs = []
    for u in range(n):
        if used[u]:
            continue
        row = graph[u]
        for v in range(n):
            if not used[v] and row[v] == FRIEND:
                used[u] = used[v] = 1
                pairs.append((u, v))
                break

    unmatched = [u for u in range(n) if not used[u]]
    # Unmatched vertices are independent, so a short augmentation always exists.
    for pos in range(0, len(unmatched) - 1, 2):
        u, v = unmatched[pos : pos + 2]
        row_u, row_v = graph[u], graph[v]
        for i, (a, b) in enumerate(pairs):
            if row_u[a] == FRIEND and row_v[b] == FRIEND:
                pairs[i] = (u, a)
                pairs.append((v, b))
                break
            if row_u[b] == FRIEND and row_v[a] == FRIEND:
                pairs[i] = (u, b)
                pairs.append((v, a))
                break

    triangle = -1
    extra = -1
    if len(unmatched) % 2:
        extra = unmatched[-1]
        row = graph[extra]
        # Its degree exceeds the number of pairs, so one pair completes a triangle.
        for i, (a, b) in enumerate(pairs):
            if row[a] == FRIEND and row[b] == FRIEND:
                triangle = i
                break

    answer = ["YES", str(len(pairs))]
    for i, (a, b) in enumerate(pairs):
        if i == triangle:
            answer.append(f"{TRIANGLE_SIZE} {a + 1} {b + 1} {extra + 1}")
        else:
            answer.append(f"2 {a + 1} {b + 1}")
    sys.stdout.write("\n".join(answer) + "\n")


if __name__ == "__main__":
    main()
