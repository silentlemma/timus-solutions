import sys


def main():
    words = iter(sys.stdin.read().split())
    h, w, n = int(next(words)), int(next(words)), int(next(words))
    lines, used = 1, -1
    for _, word in zip(range(n), words):
        # a word after another one on the line needs a space before it
        if used + 1 + len(word) > w:
            lines += 1
            used = -1
        used += 1 + len(word)
    print(-(-lines // h))


main()
