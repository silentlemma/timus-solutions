import sys


def main():
    text = sys.stdin.readline().rstrip("\r\n")
    n = len(text)
    out = [""] * n
    # the encoded text lists the middle of a range, then its left part,
    # then its right part: replay that order and put each letter back
    stack = [(0, n - 1)]
    at = 0
    while stack:
        lo, hi = stack.pop()
        if lo > hi:
            continue
        mid = (lo + hi) // 2
        out[mid] = text[at]
        at += 1
        stack.append((mid + 1, hi))
        stack.append((lo, mid - 1))
    print("".join(out))


main()
