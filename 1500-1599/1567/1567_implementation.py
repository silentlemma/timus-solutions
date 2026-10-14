import sys

# the characters of each key in the order of presses; the space has a key
# of its own
KEYS = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " "]
PRESSES = {c: i + 1 for key in KEYS for i, c in enumerate(key)}


def main():
    # the whole first line, spaces included; anything else costs nothing
    line = sys.stdin.readline()
    print(sum(PRESSES.get(c, 0) for c in line))


main()
