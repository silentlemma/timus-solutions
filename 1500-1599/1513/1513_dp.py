import sys


def main():
    n, k = map(int, sys.stdin.read().split())
    # count[i + 1]: lines of i words with no more than k lemons in a row,
    # with count[0] = 1 standing for length -1
    count = [1, 1]
    for i in range(1, n + 1):
        # a valid line of i words is a valid line of i - 1 words plus a word,
        # except those ending in exactly k + 1 lemons after a banana
        drop = count[i - k - 1] if i > k else 0
        count.append(2 * count[i] - drop)
    print(count[n + 1])


main()
