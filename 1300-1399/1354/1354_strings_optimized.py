from array import array
import sys


def main():
    word = sys.stdin.buffer.readline().strip()
    pattern = word[::-1]
    n = len(word)
    # n <= 10000; unsigned shorts store all prefix lengths without integer objects.
    border = array("H", [0]) * n
    for i in range(1, n):
        k = border[i - 1]
        while k and pattern[i] != pattern[k]:
            k = border[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        border[i] = k
    longest = 0
    # match only the proper tail, so a palindrome still gets a nonempty addition.
    for i in range(1, n):
        while longest and word[i] != pattern[longest]:
            longest = border[longest - 1]
        if word[i] == pattern[longest]:
            longest += 1
    sys.stdout.buffer.write(word + pattern[longest:] + b"\n")


main()
