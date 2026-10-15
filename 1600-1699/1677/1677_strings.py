import sys


def main():
    data = sys.stdin.read().split()
    n, word = int(data[0]), data[1]
    size = len(word)
    # prefix function: pi[i] is the longest border of word[:i + 1]
    pi = [0] * size
    for i in range(1, size):
        j = pi[i - 1]
        while j and word[i] != word[j]:
            j = pi[j - 1]
        if word[i] == word[j]:
            j += 1
        pi[i] = j
    # the expected time is the sum of n^k over the lengths k of the word's
    # borders, the whole word included: a number whose base-n digits are 0
    # and 1, built by Horner's rule from the top digit down
    border = [0] * (size + 1)
    k = size
    while k:
        border[k] = 1
        k = pi[k - 1]
    total = 0
    for k in range(size, 0, -1):
        total = total * n + border[k]
    total *= n
    sys.set_int_max_str_digits(0)
    print(total)


main()
