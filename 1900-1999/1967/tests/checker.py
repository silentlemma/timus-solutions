"""Check input, expected, candidate: legal cuts and the exact exchange optimality certificate."""
from pathlib import Path
import sys


DECIMAL_BASE = 10


def check(bits, candidate):
    lines = candidate.splitlines()
    if len(lines) != 2:
        return False
    try:
        count_values = list(map(int, lines[0].split()))
        lengths = list(map(int, lines[1].split()))
    except ValueError:
        return False
    if len(count_values) != 1 or count_values[0] != len(lengths) or not lengths:
        return False
    if any(length <= 0 for length in lengths) or sum(lengths) != len(bits):
        return False
    powers = []
    power = 1
    position = 0
    for number, length in enumerate(lengths):
        if bits[position] != '1':
            return False
        end = position + length
        index = 0
        cheap = False
        while True:
            if index == len(powers):
                power *= DECIMAL_BASE
                powers.append(bin(power)[2:])
            threshold = powers[index]
            suffix_length = len(threshold)
            if suffix_length > length:
                break
            start = end - suffix_length
            if bits[start] == '1' and bits[start:end] < threshold:
                if suffix_length < length:
                    return False
                cheap = True
            if suffix_length == length:
                break
            index += 1
        if number and not cheap:
            return False
        position = end
    return True


def main():
    data = Path(sys.argv[1]).read_text().split()
    if len(data) != 1:
        print('Invalid input')
        return 1
    maximum = int(data[0])
    bits = ''.join(bin(value)[2:] for value in range(1, maximum + 1))
    candidate = Path(sys.argv[3]).read_text()
    if not check(bits, candidate):
        print('Expected legal bit lengths with no strictly improving split or merge')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
