"""Print the table RICH of the solutions: the number of binary rich words of
every length from 1 to 61 (OEIS A216264 up to 60), one "length count" line
each.

    python 2061_strings_bruteforce_table.py [LONGEST]

The search described in the write-up: every prefix of a rich word is rich,
so a depth-first search extends rich words one letter at a time, keeping an
eertree of the current word, and cuts a branch as soon as a letter adds no
new palindrome. Words starting with 1 mirror those starting with 0. Very
slow for the full table (about 10^13 words); a smaller LONGEST checks the
first entries quickly.
"""

import sys

LONGEST = 61


def main():
    longest = int(sys.argv[1]) if len(sys.argv) > 1 else LONGEST
    sys.setrecursionlimit(10000)
    # eertree nodes: 0 is the root of length -1, 1 the empty palindrome
    length = [-1, 0]
    link = [0, 0]
    child = [[0, 0], [0, 0]]  # 0 means no edge
    word = []
    counts = [0] * (longest + 1)

    def suffix_with(node, c):
        """The longest palindromic suffix from node that c can extend on both sides."""
        i = len(word)
        while True:
            span = length[node]
            if span == -1 or (i - 1 - span >= 0 and word[i - 1 - span] == c):
                return node
            node = link[node]

    def extend(last):
        counts[len(word)] += 1
        if len(word) == longest:
            return
        for c in (0, 1):
            cur = suffix_with(last, c)
            if child[cur][c]:
                continue  # no new palindrome: the longer word is not rich
            new = len(length)
            length.append(length[cur] + 2)
            if length[new] == 1:
                link.append(1)
            else:
                link.append(child[suffix_with(link[cur], c)][c])
            child.append([0, 0])
            child[cur][c] = new
            word.append(c)
            extend(new)
            word.pop()
            child[cur][c] = 0
            child.pop()
            link.pop()
            length.pop()

    # the words starting with 0; swapping the letters gives the others
    word.append(0)
    length.append(1)
    link.append(1)
    child.append([0, 0])
    child[0][0] = 2
    extend(2)
    for n in range(1, longest + 1):
        print(n, 2 * counts[n], flush=True)


main()
