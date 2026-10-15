import sys


def main():
    text = sys.stdin.buffer.readline().strip()
    # a letter equal to the one before it cancels that one: removing the
    # inserted pairs in any order leaves the same text
    stack = bytearray()
    for c in text:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    sys.stdout.write(stack.decode() + "\n")


main()
