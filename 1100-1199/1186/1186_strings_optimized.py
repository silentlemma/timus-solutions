import sys

OPEN = ord("(")
CLOSE = ord(")")
ZERO = ord("0")
NINE = ord("9")
LOWER_A = ord("a")
LOWER_Z = ord("z")
DECIMAL = 10
BYTE_BITS = 8


def totals(formula):
    counts = {}
    for term in formula.split(b"+"):
        start = 0
        factor = 0
        while ZERO <= term[start] <= NINE:
            factor = factor * DECIMAL + term[start] - ZERO
            start += 1
        product = factor if start else 1
        parents = []
        index = len(term) - 1
        # Reading backwards gives each group's multiplier before its atoms.
        while index >= start:
            count, place = 0, 1
            while ZERO <= term[index] <= NINE:
                count += (term[index] - ZERO) * place
                place *= DECIMAL
                index -= 1
            if place == 1:
                count = 1
            token = term[index]
            if token == CLOSE:
                parents.append(product)
                product *= count
            elif token == OPEN:
                product = parents.pop()
            else:
                symbol = token
                if LOWER_A <= token <= LOWER_Z:
                    index -= 1
                    symbol += term[index] << BYTE_BITS
                counts[symbol] = counts.get(symbol, 0) + product * count
            index -= 1
    return counts


def main():
    left, _, *right_sides = sys.stdin.buffer.read().split()
    expected = totals(left)
    for right in right_sides:
        sign = b"==" if totals(right) == expected else b"!="
        sys.stdout.buffer.write(left + sign + right + b"\n")


if __name__ == "__main__":
    main()
