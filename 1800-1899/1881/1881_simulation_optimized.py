import sys


def main():
    # the input is parsed line by line, and only the length of each word is used
    words = (word for line in sys.stdin.buffer for word in line.split())
    height, width, count = int(next(words)), int(next(words)), int(next(words))
    lines, used = 1, -1
    for _ in range(count):
        length = len(next(words))
        # a word after another one on the line needs a space before it
        if used + 1 + length > width:
            lines += 1
            used = -1
        used += 1 + length
    print((lines + height - 1) // height)


main()
