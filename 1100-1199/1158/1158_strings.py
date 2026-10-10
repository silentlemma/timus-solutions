import sys
from collections import deque


def main():
    # letters may be any bytes above 32, so the input is read as bytes
    lines = [line.strip() for line in sys.stdin.buffer.read().split(b"\n")]
    n, m, p = map(int, lines[0].split())
    letters = lines[1]
    index = {c: k for k, c in enumerate(letters)}
    words = [w for w in lines[2:] if w][:p]
    # Aho-Corasick automaton over the forbidden words; a state is bad when
    # some word ends there
    goto, bad = [[-1] * n], [False]
    for w in words:
        s = 0
        for c in w:
            if goto[s][index[c]] < 0:
                goto[s][index[c]] = len(goto)
                goto.append([-1] * n)
                bad.append(False)
            s = goto[s][index[c]]
        bad[s] = True
    fail = [0] * len(goto)
    queue = deque()
    for c in range(n):
        if goto[0][c] < 0:
            goto[0][c] = 0
        else:
            queue.append(goto[0][c])
    while queue:
        s = queue.popleft()
        bad[s] = bad[s] or bad[fail[s]]
        for c in range(n):
            t = goto[s][c]
            if t < 0:
                goto[s][c] = goto[fail[s]][c]
            else:
                fail[t] = goto[fail[s]][c]
                queue.append(t)
    # count the sentences letter by letter, never stepping into a bad state
    ways = [1] + [0] * (len(goto) - 1)
    for _ in range(m):
        step = [0] * len(goto)
        for s, w in enumerate(ways):
            if w:
                for t in goto[s]:
                    if not bad[t]:
                        step[t] += w
        ways = step
    print(sum(ways))


main()
