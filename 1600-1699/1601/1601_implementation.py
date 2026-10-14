import sys

ENDS = b".!?"  # marks that end a sentence


def main():
    text = bytearray(sys.stdin.buffer.read())
    start = True  # the next letter opens a sentence
    for i, c in enumerate(text):
        if ord("A") <= c <= ord("Z"):
            if not start:
                text[i] = c + ord("a") - ord("A")
            start = False
        elif c in ENDS:
            start = True
    sys.stdout.buffer.write(bytes(text))


main()
