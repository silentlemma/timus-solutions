import sys


def main():
    lines = sys.stdin.read().split("\n")
    n, m = map(int, lines[0].split())
    text = lines[1].rstrip("\r")
    # run[i]: how many letters and spaces start at position i
    run = [0] * (len(text) + 1)
    for i in range(len(text) - 1, -1, -1):
        if text[i].isalpha() or text[i] == " ":
            run[i] = run[i + 1] + 1
    # the farthest reach never moves back, so the longest message each time is best
    pos = count = 0
    while pos < len(text):
        pos += max(n, min(m, run[pos]))
        count += 1
    print(count)


main()
