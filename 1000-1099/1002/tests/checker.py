"""Checker: each output line is a shortest word sequence for its test, or
"No solution." exactly when the expected answer is."""

import sys

KEYPAD = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344115566070778889990")
NO_SOLUTION = "No solution."
END_OF_INPUT = "-1"


def tests(path):
    tokens = open(path).read().split()
    pos = 0
    while tokens[pos] != END_OF_INPUT:
        phone, n = tokens[pos], int(tokens[pos + 1])
        yield phone, set(tokens[pos + 2 : pos + 2 + n])
        pos += 2 + n


def main():
    inp, expected, output = sys.argv[1:4]
    want = open(expected).read().split("\n")
    got = open(output).read().split("\n")
    for i, (phone, words) in enumerate(tests(inp)):
        line = got[i].strip() if i < len(got) else ""
        if want[i].strip() == NO_SOLUTION:
            if line != NO_SOLUTION:
                print("test %d: expected %s" % (i + 1, NO_SOLUTION))
                sys.exit(1)
            continue
        used = line.split()
        if line == NO_SOLUTION or any(w not in words for w in used):
            print("test %d: %r is not a sequence of dictionary words" % (i + 1, line))
            sys.exit(1)
        if "".join(used).translate(KEYPAD) != phone:
            print("test %d: the words do not spell the number" % (i + 1))
            sys.exit(1)
        if len(used) != len(want[i].split()):
            print(
                "test %d: %d words, the shortest has %d" % (i + 1, len(used), len(want[i].split()))
            )
            sys.exit(1)


main()
