import sys
from collections import deque


def main():
    tok = list(map(int, sys.stdin.buffer.read().split()))
    m = tok[0]
    values = tok[1 : tok.index(-1)]
    # indices of the window whose values decrease from front to back: the
    # front is the maximum, and a value never matters once a later one is larger
    window = deque()
    out = []
    for i, v in enumerate(values):
        while window and values[window[-1]] <= v:
            window.pop()
        window.append(i)
        if window[0] <= i - m:
            window.popleft()
        if i >= m - 1:
            out.append(values[window[0]])
    print("\n".join(map(str, out)))


main()
