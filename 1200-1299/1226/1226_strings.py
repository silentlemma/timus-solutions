import re
import sys

WORD = re.compile(rb"[A-Za-z]+")


def main():
    text = sys.stdin.buffer.read()
    # every run of Latin letters is reversed in place; everything else stays
    sys.stdout.buffer.write(WORD.sub(lambda m: m.group()[::-1], text))


main()
