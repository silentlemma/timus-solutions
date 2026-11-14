import sys


ERASE = bytes.maketrans(b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", b"_" * 52)
FAILED = b"I HAVE FAILED!!!\n"


def main():
    source = sys.stdin.buffer.readline().rstrip(b"\r\n")
    wanted = sys.stdin.buffer.readline().split()
    answer = bytearray(source.translate(ERASE))
    start = 0
    for target in wanted:
        found = source.find(target, start)
        if found < 0:
            sys.stdout.buffer.write(FAILED)
            return
        end = found + len(target)
        answer[found:end] = target
        # Latin-letter words cannot span an original space. Advance over one
        # separator, which is either an original space or an erased letter.
        start = end + 1
    answer.extend(b"\n")
    sys.stdout.buffer.write(answer)


if __name__ == "__main__":
    main()
