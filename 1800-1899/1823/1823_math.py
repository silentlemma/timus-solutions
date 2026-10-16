import sys

R_NUM = 8314  # the gas constant R = 8.314 as R_NUM / R_DEN
R_DEN = 1000
SCALE = 1000000  # six digits after the point
LINE = 3  # tokens in "X = value"


def print_value(name, numerator, denominator):
    value = (numerator * SCALE + denominator // 2) // denominator
    print(f"{name} = {value // SCALE}.{value % SCALE:06d}")


def main():
    tokens = sys.stdin.read().split()
    # lines "X = value"
    known = {tokens[i]: int(tokens[i + 2]) for i in range(0, len(tokens), LINE)}
    p, n, v, t = (known.get(name) for name in "pnVT")
    # p V = n R T, with V and T strictly positive
    if p is None:
        print_value("p", n * R_NUM * t, R_DEN * v)
    elif n is None:
        print_value("n", p * v * R_DEN, R_NUM * t)
    else:
        # the unknown is V (beside p) or T (beside n R), and both must be
        # positive: a zero factor leaves 0 = 0 or a contradiction
        name, factor, other = ("V", p, n) if v is None else ("T", n, p)
        if factor == 0:
            print("undefined" if other == 0 else "error")
        elif other == 0:
            print("error")
        elif v is None:
            print_value(name, n * R_NUM * t, R_DEN * p)
        else:
            print_value(name, p * v * R_DEN, n * R_NUM)


main()
