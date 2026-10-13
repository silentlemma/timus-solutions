import sys


def main():
    word = sys.stdin.readline().strip()
    # the added part is never empty, so look for the longest palindromic
    # suffix of the word without its first letter
    tail = word[1:]
    text = tail[::-1] + "#" + tail
    border = [0] * len(text)
    for i in range(1, len(text)):
        k = border[i - 1]
        while k and text[i] != text[k]:
            k = border[k - 1]
        if text[i] == text[k]:
            k += 1
        border[i] = k
    longest = border[-1] if tail else 0
    print(word + word[: len(word) - longest][::-1])


main()
