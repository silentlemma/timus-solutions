import sys

R = 8.314
LINE = 3  # tokens in "X = value"


def main():
    tokens = sys.stdin.read().split()
    # lines "X = value"
    known = {tokens[i]: int(tokens[i + 2]) for i in range(0, len(tokens), LINE)}
    p, n, v, t = (known.get(name) for name in "pnVT")
    # p V = n R T, with V and T strictly positive
    if p is None:
        print(f"p = {n * R * t / v:.6f}")
    elif n is None:
        print(f"n = {p * v / (R * t):.6f}")
    else:
        # the unknown is V (beside p) or T (beside n R), and both must be
        # positive: a zero factor leaves 0 = 0 or a contradiction
        name, factor, other = ("V", p, n * R * t) if v is None else ("T", n * R, p * v)
        if factor == 0:
            print("undefined" if other == 0 else "error")
        elif other == 0:
            print("error")
        else:
            print(f"{name} = {other / factor:.6f}")


main()
