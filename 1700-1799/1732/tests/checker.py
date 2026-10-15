"""Checker: the failure line exactly when the expected answer has it, and
otherwise the source with some letters turned into underscores, which
reads as the wanted saying once those letters become spaces."""

import sys

FAILED = "I HAVE FAILED!!!"


class Bad(Exception):
    pass


def check(source, expected, output):
    lines = open(source).read().split("\n")
    text, wanted = lines[0].rstrip("\r"), lines[1].rstrip("\r")
    want = open(expected).read().split("\n")[0].rstrip("\r")
    got = open(output).read().split("\n")[0].rstrip("\r")
    if want == FAILED:
        if got != FAILED:
            raise Bad("the saying cannot be made, expected the failure line")
        return
    if len(got) != len(text):
        raise Bad("the output is not the source with letters replaced")
    for c, d in zip(text, got):
        if d != c and not (d == "_" and c != " "):
            raise Bad("only letters may become underscores")
    if " ".join(got.replace("_", " ").split()) != wanted:
        raise Bad("the result does not read as the wanted saying")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
