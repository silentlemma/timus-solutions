"""Check the decision and any five nonempty palindromes reconstructing the input."""

from pathlib import Path
import sys

PARTS = 5


def check(text, reference, answer):
    expected = reference.split()
    words = answer.split()
    if not expected or expected[0] not in (b"YES", b"NO"):
        return False
    if not words or words[0] != expected[0]:
        return False
    if words[0] == b"NO":
        return words == [b"NO"]
    pieces = words[1:]
    return (
        len(pieces) == PARTS
        and b"".join(pieces) == text.strip()
        and all(part and part == part[::-1] for part in pieces)
    )


if __name__ == "__main__":
    input_path, reference_path, output_path = map(Path, sys.argv[1:])
    valid = check(
        input_path.read_bytes(), reference_path.read_bytes(), output_path.read_bytes()
    )
    if not valid:
        print("wrong decision or invalid five-palindrome decomposition")
    sys.exit(0 if valid else 1)
