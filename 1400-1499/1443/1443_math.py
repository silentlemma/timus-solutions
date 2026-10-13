import sys

DIGITS = 4  # lengths are given to a tenth of a millimetre


def tenths(text):
    # a length in tenths of a millimetre, read exactly
    whole, _, frac = text.partition(".")
    return int(whole or "0") * 10**DIGITS + int((frac + "0" * DIGITS)[:DIGITS])


def main():
    n, s, rail = sys.stdin.read().split()
    n, s, rail = int(n), tenths(s), tenths(rail)
    full, rest = divmod(s, rail)
    if rest == 0:
        print(n * full)
        return
    # each line takes its full rails and a short piece; a rail holds rail // rest such pieces
    per_rail = rail // rest
    print(n * full + (n + per_rail - 1) // per_rail)


main()
