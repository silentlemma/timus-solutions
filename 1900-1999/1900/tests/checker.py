from pathlib import Path
import sys


def check(input_text, expected_text, output_text):
    n, k, *weights = map(int, input_text.split())
    try:
        result = list(map(int, output_text.split()))
    except ValueError:
        return "the output must contain integers"
    if len(result) != k + 1:
        return "expected the maximum coverage and exactly k spans"
    value, cuts = result[0], result[1:]
    if cuts != sorted(set(cuts)) or not 1 <= cuts[0] <= cuts[-1] < n:
        return "spans must be distinct, increasing and in range"
    if value != int(expected_text.split()[0]):
        return "the passenger count is not optimal"
    selected = [0] * n
    for cut in cuts:
        selected[cut] = 1
    for index in range(1, n):
        selected[index] += selected[index - 1]
    total, position = 0, 0
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            if selected[right - 1] != selected[left - 1]:
                total += weights[position]
            position += 1
    if value != total:
        return "the reported count does not match the chosen spans"
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
