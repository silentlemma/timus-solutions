"""Checker: -1 exactly when the expected answer is -1; otherwise as many
phrases as expected, at most 100, that build the word from the empty
one."""

import sys

MOST = 100
DOUBLE = str.maketrans({"0": "01", "1": "10"})


class Bad(Exception):
    pass


def check(source, expected, output):
    word = open(source).read().split()[0]
    want = open(expected).read().split("\n")
    got = [line.strip() for line in open(output).read().strip().split("\n")]
    if want[0].strip() == "-1":
        if got != ["-1"]:
            raise Bad("the word needs more than %d phrases, expected -1" % MOST)
        return
    if not got or not got[0].isdigit():
        raise Bad("expected the number of phrases")
    k = int(got[0])
    if k != int(want[0]) or k > MOST or len(got) != k + 1:
        raise Bad("expected %s phrases" % want[0].strip())
    built = ""
    for line in got[1:]:
        if line == "double":
            built = built.translate(DOUBLE)
        elif line in ("front 0", "front 1"):
            built = line[-1] + built
        elif line in ("back 0", "back 1"):
            built = built + line[-1]
        else:
            raise Bad("unknown phrase %r" % line)
        if len(built) > len(word):
            raise Bad("the word grows longer than the one on the fence")
    if built != word:
        raise Bad("the phrases build another word")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
