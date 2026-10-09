import sys
from itertools import permutations

DIVISOR = 7
KEY = "1234"


def main():
    tok = sys.stdin.read().split()
    # the 24 orders of 1, 2, 3, 4 leave every remainder modulo 7
    orders = ["".join(p) for p in permutations(KEY)]
    out = []
    for number in tok[1 : 1 + int(tok[0])]:
        rest = list(number)
        for d in KEY:
            rest.remove(d)
        # zeros go to the end, where they do not change divisibility by 7
        head = "".join(d for d in rest if d != "0")
        zeros = "0" * (len(rest) - len(head))
        for order in orders:
            if int(head + order) % DIVISOR == 0:
                out.append(head + order + zeros)
                break
    sys.stdout.write("\n".join(out) + "\n")


main()
