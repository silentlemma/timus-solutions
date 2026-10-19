from itertools import permutations, product

COUNT = 3


def apply(x, op, y):
    if op == "*":
        return x * y
    return x + y if op == "+" else x - y


def evaluate(x, op1, y, op2, z):
    # multiplication first
    if op2 == "*" and op1 != "*":
        return apply(x, op1, y * z)
    return apply(apply(x, op1, y), op2, z)


def main():
    v = [int(input()) for _ in range(COUNT)]
    best = sum(v)
    for x, y, z in permutations(v):
        for a, b in product("+-*", repeat=2):
            best = min(best, evaluate(x, a, y, b, z))
    print(best)


main()
