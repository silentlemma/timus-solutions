from os import _exit, write

LETTERS = 26
FIRST = ord("a")
SHIFT = 5


def decode(encoded):
    word = bytearray(encoded)
    # Work backward so the previous encrypted byte is still unchanged.
    for i in range(len(word) - 1, 0, -1):
        word[i] = FIRST + (word[i] - word[i - 1]) % LETTERS
    word[0] = FIRST + (word[0] - FIRST - SHIFT) % LETTERS
    word.append(ord("\n"))
    return word


def main():
    answer = decode(open(0, "rb", buffering=0).readline().strip())
    write(1, answer)
    _exit(0)


main()
