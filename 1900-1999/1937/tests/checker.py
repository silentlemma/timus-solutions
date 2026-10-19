"""Directly verify witnesses; certify No with exact doubling ranks, without SAM or Manacher."""

from array import array
from pathlib import Path
import sys


def find_by_ranks(first, second):
    first_size, second_size = len(first), len(second)
    middle_size = first_size - second_size
    reversed_second = second[::-1]
    pattern = reversed_second + reversed_second[:-1]
    doubled = first + first
    text = pattern + b"#" + doubled + b"$" + doubled[::-1]
    first_offset = len(pattern) + 1
    reverse_offset = first_offset + len(doubled) + 1
    small_power = 1 << (second_size.bit_length() - 1)
    middle_power = 1 << (middle_size.bit_length() - 1)
    needed = {small_power, middle_power}
    rank = array("i", (letter for letter in text))
    levels = {}
    span = 1
    if span in needed:
        levels[span] = rank
    shift = max(len(text), max(text)).bit_length()
    while span < max(needed):
        classes = {}
        following = array("i", [0]) * (len(text) - 2 * span + 1)
        for start in range(len(following)):
            key = (rank[start] << shift) | rank[start + span]
            number = classes.get(key)
            if number is None:
                number = len(classes)
                classes[key] = number
            following[start] = number
        rank = following
        span *= 2
        if span in needed:
            levels[span] = rank
    small_rank = levels[small_power]
    middle_rank = levels[middle_power]
    # Two overlapping power-of-two blocks cover a complete window exactly.
    rotations = {}
    for start in range(second_size):
        key = (small_rank[start] << shift) | small_rank[
            start + second_size - small_power
        ]
        rotations.setdefault(key, start)
    for start in range(first_size):
        middle_start = first_offset + start + second_size
        mirror_start = reverse_offset + first_size - start
        if (
            middle_rank[middle_start] != middle_rank[mirror_start]
            or middle_rank[middle_start + middle_size - middle_power]
            != middle_rank[mirror_start + middle_size - middle_power]
        ):
            continue
        begin = first_offset + start
        key = (small_rank[begin] << shift) | small_rank[
            begin + second_size - small_power
        ]
        rotation = rotations.get(key)
        if rotation is not None:
            return start, (-rotation) % second_size
    return None


def check(first, second, output):
    tokens = output.split()
    if tokens == ["No"]:
        if find_by_ranks(first, second) is not None:
            return False, "a pair of valid rotations exists"
        return True, "no valid rotations exist"
    if len(tokens) != 3 or tokens[0] != "Yes":
        return False, "expected No or Yes followed by two indices"
    try:
        first_start, second_start = int(tokens[1]) - 1, int(tokens[2]) - 1
    except ValueError:
        return False, "noninteger rotation index"
    if not (0 <= first_start < len(first) and 0 <= second_start < len(second)):
        return False, "rotation index out of range"
    whole = (
        first[first_start:]
        + first[:first_start]
        + second[second_start:]
        + second[:second_start]
    )
    if whole != whole[::-1]:
        return False, "rotated concatenation is not a palindrome"
    return True, "valid palindrome rotations"


if __name__ == "__main__":
    left, right = Path(sys.argv[1]).read_bytes().split()
    accepted, reason = check(left, right, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
