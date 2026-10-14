import sys


def main():
    data = sys.stdin.read().split()
    a, b = data[1], data[2]
    # suffix automaton of a: every state is a class of substrings with the
    # same end positions; length is the longest of them, link the suffix link
    nxt, link, length = [{}], [-1], [0]
    last = 0
    for ch in a:
        cur = len(nxt)
        nxt.append({})
        link.append(0)
        length.append(length[last] + 1)
        p = last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]
        if p != -1:
            q = nxt[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = len(nxt)
                nxt.append(dict(nxt[q]))
                link.append(link[q])
                length.append(length[p] + 1)
                while p != -1 and nxt[p].get(ch) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = link[cur] = clone
        last = cur
    # walk b through the automaton, keeping the longest suffix of the read
    # part of b that occurs in a
    state, run, best, end = 0, 0, 0, 0
    for i, ch in enumerate(b):
        while state and ch not in nxt[state]:
            state = link[state]
            run = length[state]
        if ch in nxt[state]:
            state = nxt[state][ch]
            run += 1
        if run > best:
            best, end = run, i + 1
    print(b[end - best : end])


main()
