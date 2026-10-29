import sys

INPUT_BUFFER_SIZE = 4096


def main():
    # the text is read in 4 KB blocks and walked as bytes, skipping anything
    # that is not a lowercase letter, so the line is never held whole
    first_letter, last_letter = ord("a"), ord("z")
    stack = bytearray()
    append = stack.append
    pop = stack.pop
    read = sys.stdin.buffer.read
    while chunk := read(INPUT_BUFFER_SIZE):
        for ch in chunk:
            if ch < first_letter or ch > last_letter:
                continue
            # a letter equal to the one before it cancels that one: removing the
            # inserted pairs in any order leaves the same text
            if stack and stack[-1] == ch:
                pop()
            else:
                append(ch)
    sys.stdout.buffer.write(stack)
    sys.stdout.buffer.write(b"\n")


main()
