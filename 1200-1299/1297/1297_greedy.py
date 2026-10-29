import sys


def main():
    text = sys.stdin.buffer.read().strip()
    best_start = best_length = 0
    for end in range(1, len(text) + 1):
        # the best length grows by at most 2 per letter: a longer palindrome ending
        # here would leave a longer one before it once its ends are cut off, so
        # only the lengths best + 2 and best + 1 ending here are checked
        start = end - best_length - 2
        if start >= 0:
            candidate = text[start:end]
            if candidate == candidate[::-1]:
                best_start, best_length = start, best_length + 2
                continue
        start = end - best_length - 1
        if start >= 0:
            candidate = text[start:end]
            if candidate == candidate[::-1]:
                best_start, best_length = start, best_length + 1
    sys.stdout.buffer.write(text[best_start : best_start + best_length] + b"\n")


main()
