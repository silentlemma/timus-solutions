import sys

LOWER_A = ord("a")
LOWER_Z = ord("z")
UPPER_A = ord("A")
UPPER_Z = ord("Z")


def main():
    out = sys.stdout.buffer
    # lines contain at most 255 characters; one bytearray avoids whole-text storage
    # and importing the regular-expression engine. only latin letter runs are reversed.
    for line in sys.stdin.buffer:
        text = bytearray(line)
        start = 0
        for i, c in enumerate(text):
            if LOWER_A <= c <= LOWER_Z or UPPER_A <= c <= UPPER_Z:
                continue
            if i - start > 1:
                text[start:i] = text[start:i][::-1]
            start = i + 1
        text[start:] = text[start:][::-1]
        out.write(text)


main()
