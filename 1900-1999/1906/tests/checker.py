"""Check a maximal prefix and arbitrary bounded modular-recurrence parameters."""

from pathlib import Path
import sys

PARAMETER_LIMIT = 2_000_000_000_000_000_000


def check(input_text, expected_text, output_text):
    try:
        result = list(map(int, output_text.split()))
    except ValueError:
        return "the output must contain integers"
    if len(result) != 3:
        return "expected length, modulus and multiplier"
    length, modulus, multiplier = result
    count, *values = map(int, input_text.split())
    if not 1 <= length <= count:
        return "the prefix length is out of range"
    if length != int(expected_text.split()[0]):
        return "the prefix length is not maximal"
    if not 1 <= modulus <= PARAMETER_LIMIT or not 0 <= multiplier <= PARAMETER_LIMIT:
        return "the recurrence parameters are out of bounds"
    if any(value >= modulus for value in values[:length]):
        return "an observed remainder is not below the modulus"
    if any(
        values[i] * multiplier % modulus != values[i + 1] for i in range(length - 1)
    ):
        return "the parameters do not reproduce the chosen prefix"
    return None


def main():
    input_path, expected_path, output_path = map(Path, sys.argv[1:])
    error = check(
        input_path.read_text(), expected_path.read_text(), output_path.read_text()
    )
    if error is not None:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
