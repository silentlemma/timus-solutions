import sys


def main():
    tokens = (int(word) for line in sys.stdin.buffer for word in line.split())
    n = next(tokens)
    parent = list(range(n))
    size = [1] * n
    parity = [0] * n

    def find(v):
        if parent[v] != v:
            old = parent[v]
            parent[v] = find(old)
            parity[v] ^= parity[old]
        return parent[v]

    # parity[v] is color(v) XOR color(parent(v)); an edge requires XOR=1.
    for a in range(n):
        b = next(tokens)
        while b:
            b -= 1
            ra, rb = find(a), find(b)
            if ra == rb:
                if parity[a] == parity[b]:
                    print(-1)
                    return
            else:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                parity[rb] = parity[a] ^ parity[b] ^ 1
                size[ra] += size[rb]
            b = next(tokens)
    find(0)
    first = parity[0]
    answer = []
    for v in range(n):
        find(v)
        answer.append(str(parity[v] ^ first))
    print("".join(answer))


main()
