"""Independently solve the mixture equations with rational Gauss-Jordan."""

from fractions import Fraction
from pathlib import Path
import re
import sys

PERCENT = 100
ACCURACY_DENOMINATOR = 1000
EPSILON = Fraction(1, ACCURACY_DENOMINATOR)
NUMBER = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")


def expected(text):
    recipes = {}
    for line in text.splitlines():
        if line.strip():
            name, body = line.split(":")
            tokens = body.split()
            recipes[name.strip()] = {
                tokens[i]: int(tokens[i + 1]) for i in range(0, len(tokens), 2)
            }
    names = sorted(recipes)
    bases = sorted({part for row in recipes.values() for part in row} - set(names))
    n = len(names)
    matrix = []
    for i, name in enumerate(names):
        left = [PERCENT * (i == j) - recipes[name].get(other, 0) for j, other in enumerate(names)]
        right = [recipes[name].get(base, 0) for base in bases]
        matrix.append(list(map(Fraction, left + right)))
    for col in range(n):
        pivot = next((row for row in range(col, n) if matrix[row][col]), None)
        if pivot is None:
            raise ValueError("Input must have a unique expansion")
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        divisor = matrix[col][col]
        matrix[col] = [value / divisor for value in matrix[col]]
        for row in range(n):
            if row != col:
                factor = matrix[row][col]
                matrix[row] = [x - factor * y for x, y in zip(matrix[row], matrix[col])]
    return names, bases, [[PERCENT * value for value in row[n:]] for row in matrix]


def validate(text, output):
    names, bases, wanted = expected(text)
    lines = [line for line in output.splitlines() if line.strip()]
    if len(lines) != len(names):
        raise ValueError("Wrong number of recipes")
    for name, line, reference in zip(names, lines, wanted):
        sides = line.split(":")
        if len(sides) != 2 or sides[0].strip() != name:
            raise ValueError("Recipe names must be in lexicographic order")
        tokens = sides[1].split()
        if len(tokens) != 2 * len(bases) or tokens[::2] != bases:
            raise ValueError("Every base must occur in lexicographic order, including zeros")
        if any(NUMBER.fullmatch(value) is None for value in tokens[1::2]):
            raise ValueError("Expected decimal percentages")
        values = list(map(Fraction, tokens[1::2]))
        if any(value < 0 for value in values):
            raise ValueError("Negative percentage")
        for value, target in zip(values, reference):
            if abs(value - target) > EPSILON * max(1, abs(target)):
                raise ValueError("Incorrect percentage")
        if abs(sum(values) - PERCENT) > EPSILON * PERCENT:
            raise ValueError("Percentage total is not 100 within the output tolerance")


def main():
    try:
        validate(Path(sys.argv[1]).read_text(), Path(sys.argv[3]).read_text())
    except (ValueError, OSError) as error:
        print(error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
