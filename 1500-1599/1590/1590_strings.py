import sys

LETTERS = 26


def main():
    s = sys.stdin.read().split()[0]
    most = 2 * len(s) + 1
    # suffix automaton: every state is a class of substrings with the same
    # end positions, from link-length + 1 up to length characters long
    length = [0] * most
    link = [-1] * most
    nxt = [-1] * (most * LETTERS)
    size = 1
    last = 0
    for ch in s:
        c = ord(ch) - ord("a")
        cur = size
        size += 1
        length[cur] = length[last] + 1
        p = last
        while p != -1 and nxt[p * LETTERS + c] == -1:
            nxt[p * LETTERS + c] = cur
            p = link[p]
        if p == -1:
            link[cur] = 0
        else:
            q = nxt[p * LETTERS + c]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                # split q: the clone keeps the shorter strings
                clone = size
                size += 1
                length[clone] = length[p] + 1
                link[clone] = link[q]
                nxt[clone * LETTERS : (clone + 1) * LETTERS] = nxt[q * LETTERS : (q + 1) * LETTERS]
                while p != -1 and nxt[p * LETTERS + c] == q:
                    nxt[p * LETTERS + c] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur
    print(sum(length[v] - length[link[v]] for v in range(1, size)))


main()
